curl -X 'POST' \
  'https://api.baobab.klaytn.net:8651/admin/getSpamThrottlerThrottleList' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "admin_getSpamThrottlerThrottleList",
  "id": 1,
  "jsonrpc": "2.0",
  "params": []
}'
