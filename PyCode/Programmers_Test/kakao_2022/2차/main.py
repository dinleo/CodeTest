from http_json import http_method as ht

# auth_key = '7da66c91-3745-40f0-a8ac-1e89a0e3508f'
#
# res = ht('GET', '/waiting_line')
# print(res)
# res2 = ht('GET', '/game_result')
# print(res2)
# res3 = ht('GET', '/user_info')
# print(res3)
# res4 = ht('PUT', '/match', data={"pairs": [[1, 2], [9, 7], [11, 49]]})
# print(res4)
res5 = ht('GET', '/score')
print(res5)