# https://programmers.co.kr/learn/courses/30/lessons/86048?language=python3
from collections import defaultdict


def solution(enter, leave):
    n, e, l = len(enter), 0, 0
    seat = []
    meat = defaultdict(set)  # 만난 사람을 담은 dict

    while l != n:
        # 다음으로 퇴장하는 사람이 나올때 까지 입장시킨다.
        while e != n and enter[e] != leave[l]:
            seat.append(enter[e])
            e += 1
        seat.append(enter[e])
        e += 1
        # 현재 자리에 있는 모든 사람끼리는 만났다고 count
        for i in seat:
            for j in seat:
                meat[i].add(j)
        # 현재 자리에 있는 사람들 중 퇴장시킬 수 있는 사람을 모두 퇴장시킨다.
        while l != n and leave[l] in seat:
            seat.remove(leave[l])
            l += 1
    answer = [len(meat[i + 1]) - 1 for i in range(n)]
    return answer


print(solution([1, 3, 2], [1, 2, 3]))
print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
print(solution([3, 2, 1], [2, 1, 3]))
print(solution([3, 2, 1], [1, 3, 2]))
print(solution([1, 4, 2, 3], [2, 1, 4, 3]))
