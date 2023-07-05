from web3 import Web3
from web3py_ext import extend

host = "https://api.baobab.klaytn.net:8651"

blockTag = "0x1b4"
boolean = True

w3 = Web3(Web3.HTTPProvider(host))
klay_response = w3.klay.get_block_by_number(blockTag, boolean)

print(klay_response)
