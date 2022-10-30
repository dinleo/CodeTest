# https://programmers.co.kr/learn/courses/30/lessons/87946?language=python3
from itertools import permutations

def solution(k, dungeons):
    d = len(dungeons)
    num = list(permutations(range(d)))
    ans_list = set()
    for n in num:
        k_temp = k
        count = 0
        for i in n:
            if dungeons[i][0] <= k_temp:
                k_temp -= dungeons[i][1]
                count += 1
        ans_list.add(count)
    answer = max(ans_list)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))