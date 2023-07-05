
from web3py_ext import extend
from web3 import Web3
from eth_account import Account
from web3py_ext.transaction.transaction import (
    empty_tx,
    fill_transaction,
    TX_TYPE_SMART_CONTRACT_EXECUTION
)
from web3py_ext.utils.klaytn_utils import to_pretty
from cytoolz import merge

w3 = Web3(Web3.HTTPProvider('https://public-en-baobab.klaytn.net'))

def web3_smart_contract_execution_sign_recover():
    user = Account.from_key('0x8b0164c3a59d2b1a00a9934f85ae77c14e21094132c34cc3daacd9e632c90807') 

    smart_contract_execution_tx = empty_tx(TX_TYPE_SMART_CONTRACT_EXECUTION)
    smart_contract_execution_tx = merge(smart_contract_execution_tx, {
        'from' : user.address,
        'to' : '0x108bF12b50c9ef65525F0495C721aEc55015e111', # already deployed contract for test before
        'data' : '0x3d7403a30000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000c48656c6c6f204b6c6179746e0000000000000000000000000000000000000000',
    })
    smart_contract_execution_tx = fill_transaction(smart_contract_execution_tx, w3)

    # sign the klaytn specific transaction type with web3py
    signed_tx = Account.sign_transaction(smart_contract_execution_tx, user.key)
    print("\nraw transaction of signed tx:", signed_tx.rawTransaction.hex())

    recovered_tx = Account.recover_transaction(signed_tx.rawTransaction)
    print("\nrecovered sender address", recovered_tx)
    
    decoded_tx = Account.decode_transaction(signed_tx.rawTransaction)
    print("\ndecoded transaction:", to_pretty(decoded_tx))

    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print('tx hash: ', tx_hash, 'receipt: ', tx_receipt)

web3_smart_contract_execution_sign_recover()