# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
def solution(a, b):
    return [a / 4 + 1 + ((a / 4 + 1) ** 2 - (b + a)) ** 0.5, a / 4 + 1 - ((a / 4 + 1) ** 2 - (b + a)) ** 0.5]


print(solution(10, 2))
print(solution(8, 1))
