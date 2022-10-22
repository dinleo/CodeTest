import req_solution as rs
import pro_solution as ps


def run_day(problem, room, floor, max_day):
    hotel = [[0 for _ in range(room)] for _ in range(floor)]
    request_stack = [[] for _ in range(max_day + 1)]
    reserve_stack = [[] for _ in range(max_day + 1)]
    key = rs.start_api_key(problem)
    print('Problem:[{}]\nkey{}'.format(problem, key))

    for today in range(1, max_day + 1):
        ps.stack_req(key, request_stack, today)
        ps.handle_request(key, hotel, request_stack, reserve_stack, today, problem)

        s = rs.simulate(key, reserve_stack[today])
        print(s)
    res = rs.get_score(key)
    print(res)
    return res
