from web3 import Web3
from web3py_ext import extend

host = "https://api.baobab.klaytn.net:8651"

target = 3

w3 = Web3(Web3.HTTPProvider(host))
debug_response = w3.debug.set_vm_log_target(target)

print(debug_response)
