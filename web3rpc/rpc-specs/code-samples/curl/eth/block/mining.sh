curl -X 'POST' \
  'https://api.baobab.klaytn.net:8651/eth/mining' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "eth_mining",
  "id": 1,
  "jsonrpc": "2.0",
  "params": []
}'