from http_json import http_method as ht


def start_api_key(problem):
    """
    :param problem: 1 or 2
    """
    res = ht('POST', '/start', data={'problem': problem}, start=True)
    return res['auth_key']


def get_new_req(auth_key):
    """
    :return: [{"id": 453217, "amount": 10, "check_in_date": 104, "check_out_date": 110},]
    """
    res = ht('GET', '/new_requests', token=auth_key)
    return res['reservations_info']


def reply(auth_key, reply_arr):
    """
    :param reply_arr:[{ "id": 412424, "reply": "accepted"},]
    :return: 10
    """
    res = ht('PUT', '/reply', token=auth_key, data={'replies': reply_arr})
    return res['day']


def simulate(auth_key, assign_arr):
    """
    :param assign_arr:[{ "id": 707981, "room_number": 2023},]
    :return:(108, 5)
    """
    res = ht('PUT', '/simulate', token=auth_key, data={'room_assign': assign_arr})
    return res['day'], res['fail_count']


def get_score(auth_key):
    res = ht('GET', '/score', token=auth_key)
    return res
