curl -X 'POST' \
  'https://api.baobab.klaytn.net:8651/txpool/content' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "txpool_content",
  "id": 1,
  "jsonrpc": "2.0",
  "params": []
}'
