curl -X 'POST' \
  'https://api.baobab.klaytn.net:8651/debug/startGoTrace' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "debug_startGoTrace",
  "id": 1,
  "jsonrpc": "2.0",
  "params": ["go.trace"]
}'
