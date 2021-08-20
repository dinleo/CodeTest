# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
from collections import defaultdict


def solution(numbers):
    answer = ""
    # 조건에 맞는 순서사전인 n_arr를 생성 [999 99 9 998 ... 769 768 767 76 766 ... 102 101 10 100]
    arr = [[[i * 100 + j * 10 + k for k in range(9, -1, -1)] for j in range(9, -1, -1)] for i in range(9, 0, -1)]
    for i in range(9, 0, -1):
        for j in range(9, -1, -1):
            num = i * 10 + j
            if j <= i:
                arr[9 - i][9 - j].insert(9 - i + 1, num)
            else:
                arr[9 - i][9 - j].insert(9 - i, num)
        arr[9 - i][9 - i].insert(9 - i + 2, i)
    n_arr = []
    for i in arr:
        for j in i:
            n_arr += [k for k in j]
    n_arr.append(1000)
    n_arr.append(0)

    # dict을 통해 중복요소 처리후 join
    d = defaultdict(list)
    for n in numbers:
        d[n_arr.index(n)].append(str(n))

    for i in range(len(n_arr)):
        if d.get(i):
            answer += "".join(d.get(i))
    if int(answer) == 0:
        return '0'
    return answer


# print(solution([3, 30, 34, 5, 9, 9]))
# print(solution([1000, 0, 5, 99, 100]))
# print(solution([0, 0, 0, 0, 0]))
# print(solution([0, 5, 10, 15, 20]))
# print(solution([12, 121]))
# print(solution([21, 212]))
print(solution([90,908,89,898,10,101,1,8,9]))
print(solution([0,0,0,0]))
