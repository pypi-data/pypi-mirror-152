from .base import TLObject
from .types import InputKeyRegular, AccountAddress, ActionMsg, WalletV3InitialAccountState, \
    Internal_TransactionId
from ..utils.base import str_b64encode
from typing import Union

class CreateNewKey(TLObject):
    def __init__(self, mnemonic_password: str=None, random_extra_seed: str=None, local_password: str=None):
        self.type = 'createNewKey'
        self.mnemonic_password = str_b64encode(mnemonic_password)
        self.random_extra_seed = str_b64encode(random_extra_seed)
        self.local_password = str_b64encode(local_password)

class GetAccountAddress(TLObject):
    def __init__(self, initial_account_state, revision: int=0, workchain_id: int=0):
        self.type = 'getAccountAddress'
        self.initial_account_state = initial_account_state
        self.revision = revision
        self.workchain_id = workchain_id

class Raw_GetAccountState(TLObject):
    def __init__(self, account_address: Union[AccountAddress, str]):
        if type(account_address) == str:
            account_address = AccountAddress(account_address)

        self.type = 'raw.getAccountState'
        self.account_address = account_address

class GetAccountState(TLObject):
    def __init__(self, account_address: Union[AccountAddress, str]):
        if type(account_address) == str:
            account_address = AccountAddress(account_address)

        self.type = 'getAccountState'
        self.account_address = account_address

class CreateQuery(TLObject):
    def __init__(
            self,
            private_key: InputKeyRegular,
            initial_account_state: WalletV3InitialAccountState,
            address: AccountAddress,
            action: Union[ActionMsg],
            timeout: int = 300
    ) -> object:
        self.type = 'createQuery'
        self.private_key = private_key
        self.initial_account_state = initial_account_state
        self.address = address
        self.action = action
        self.timeout = timeout

class QuerySend(TLObject):
    def __init__(self, id: int):
        self.type = 'query.send'
        self.id = id

class Raw_GetTransactions(TLObject):
    def __init__(self, account_address: Union[AccountAddress, str], from_transaction_id: Internal_TransactionId):
        self.type = 'raw.getTransactions'
        self.account_address = account_address
        self.from_transaction_id = from_transaction_id

class ExportKey(TLObject):
    def __init__(self, input_key: InputKeyRegular):
        self.type = 'exportKey'
        self.input_key = input_key

class ImportKey(TLObject):
    def __init__(self, exported_key, mnemonic_password, local_password=None):
        self.type = 'importKey'
        self.exported_key = exported_key
        self.mnemonic_password = str_b64encode(mnemonic_password)
        self.local_password = str_b64encode(local_password)

class SetLogVerbosityLevel(TLObject):
    def __init__(self, level: int):
        self.type = 'setLogVerbosityLevel'
        self.new_verbosity_level = level