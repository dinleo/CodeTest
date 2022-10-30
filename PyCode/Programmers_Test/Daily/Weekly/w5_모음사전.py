# https://programmers.co.kr/learn/courses/30/lessons/84512?language=python3
from itertools import product


def solution(word):
    dic = []
    for i in range(1, 6):
        dic.extend("".join(j) for j in product("AEIOU", repeat=i))
    dic.sort()
    return dic.index(word) + 1


print(solution("AAAAE"))
print(solution("EIO"))
