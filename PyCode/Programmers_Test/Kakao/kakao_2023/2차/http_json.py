import requests
# 출처: https://github.com/cpm0722/kakao-2022-round2/blob/master/http_json.py

base_url = 'https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api'
x_auth_key = 'f08efca7a3a4dd17163985b27dfea7d3'


def http_method(method: str, sub_url: str, token="", data={}, start=False):
    assert method in ["GET", "POST", "PUT"]
    headers = {'Accept': "application/json", 'Content-Type': "application/json"}
    if start is True:
        headers['X-Auth-Token'] = x_auth_key
    else:
        headers['Authorization'] = token

    if method == "GET":
        response = requests.get(base_url + sub_url, headers=headers)
    elif method == "POST":
        response = requests.post(base_url + sub_url, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(base_url + sub_url, headers=headers, json=data)
    else:
        return {}
    status_code = response.status_code
    res = {}
    if status_code == 200:
        res = response.json()
    # print(status_code, res)
    return res
