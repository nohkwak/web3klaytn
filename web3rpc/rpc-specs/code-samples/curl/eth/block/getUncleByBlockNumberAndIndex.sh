curl -X 'POST' \
  'https://api.baobab.klaytn.net:8651/eth/getUncleByBlockNumberAndIndex' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "eth_getUncleByBlockNumberAndIndex",
  "id": 1,
  "jsonrpc": "2.0",
  "params": ["0xe8", "0x1"]
}'
