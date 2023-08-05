from abc import ABC, abstractmethod

from nile.signer import Signer
from pontis.core.const import NETWORK, ORACLE_CONTROLLER_ADDRESS
from starknet_py.contract import Contract
from starknet_py.net import Client
from starkware.crypto.signature.signature import sign
from starkware.starknet.public.abi import get_selector_from_name

MAX_FEE = 0


class PontisBaseClient(ABC):
    def __init__(
        self,
        account_private_key,
        account_contract_address,
        network=None,
        oracle_controller_address=None,
        max_fee=None,
        n_retries=None,
    ):
        if network is None:
            network = NETWORK
        if oracle_controller_address is None:
            oracle_controller_address = ORACLE_CONTROLLER_ADDRESS

        self.network = network
        self.oracle_controller_address = oracle_controller_address
        self.oracle_controller_contract = None
        self.account_contract_address = account_contract_address
        self.account_contract = None

        assert type(account_private_key) == int, "Account private key must be integer"
        self.account_private_key = account_private_key
        self.signer = Signer(self.account_private_key)

        self.client = Client(self.network, n_retries=n_retries)

        self.max_fee = MAX_FEE if max_fee is None else max_fee
        self.nonce = None

    @abstractmethod
    async def _fetch_contracts(self):
        pass

    async def get_nonce(self):
        await self._fetch_contracts()

        result = await self.account_contract.functions["get_nonce"].call()
        nonce = result.res
        # If we have sent of tx recently, use that nonce because state won't have been updated yet
        if self.nonce is not None and self.nonce >= nonce:
            nonce = self.nonce + 1

        self.nonce = nonce
        return nonce

    async def _fetch_base_contracts(self):
        if self.oracle_controller_contract is None:
            self.oracle_controller_contract = await Contract.from_address(
                self.oracle_controller_address,
                self.client,
            )

        if self.account_contract is None:
            self.account_contract = await Contract.from_address(
                self.account_contract_address, self.client
            )

    async def send_transaction(self, to_contract, selector_name, calldata):
        return await self.send_transactions([(to_contract, selector_name, calldata)])

    async def send_transactions(self, calls):
        nonce = await self.get_nonce()

        call_array = []
        offset = 0
        for i in range(len(calls)):
            call_array.append(
                {
                    "to": calls[i][0],
                    "selector": get_selector_from_name(calls[i][1]),
                    "data_offset": offset,
                    "data_len": len(calls[i][2]),
                }
            )
            offset += len(calls[i][2])

        calldata = [x for call in calls for x in call[2]]
        prepared = self.account_contract.functions["__execute__"].prepare(
            call_array=call_array,
            calldata=calldata,
            nonce=nonce,
            max_fee=self.max_fee,
        )
        signature = sign(prepared.hash, self.account_private_key)
        invocation = await prepared.invoke(signature, max_fee=self.max_fee)

        return invocation
