import requests

base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
auth_key = '7da66c91-3745-40f0-a8ac-1e89a0e3508f'


def http_method(method: str, sub_url: str, data={}, token="", init=False):
    assert method in ["GET", "POST", "PUT"]
    headers = {'Accept': "application/json", 'Content-Type': "application/json"}
    if init is True:
        headers['X-Auth-Token'] = token
    else:
        headers['Authorization'] = auth_key

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
