import time

import requests, json

header = {'Content-Type': 'application/json', 'Authorization': 'Basic S0FTS1JOSFpGV0pVRFRXRzk0Tkk2U01WOi1KdGJWbHBYT0RxeTlKS21CQUtfdk5SZDBpeEd1SDZkT3FPM0Z5Mk8=', 'x-chain-id': '8217'}

data ={"jsonrpc":"2.0","method":"klay_blockNumber","params":[],"id":1}
while 1:
    r = requests.post('https://node-api.klaytnapi.com/v1/klaytn', headers=header, data=json.dumps(data))
    j = r.json()

    print(int(j['result'],16))
    time.sleep(0.5)
