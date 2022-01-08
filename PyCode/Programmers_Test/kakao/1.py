from collections import defaultdict


def solution(id_list, report, k):
    # 신고당한사람을 key, 신고한사람을 value set 으로 갖는 dict
    reported = defaultdict(set)
    for i in report:
        r = i.split(" ")
        reported[r[1]].add(r[0])

    # 메일을 받는 횟수를 count 하는 dict
    id_dict = defaultdict(int)
    for i in id_list:
        id_dict[i] = 0

    # 신고한 사람이 2명이상인 경우 신고한사람들에게 메일을 보낸다.
    for i in id_list:
        reported_set = reported[i]
        if k <= len(reported_set):
            for s in reported_set:
                id_dict[s] += 1

    answer = [id_dict[i] for i in id_list]
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution())