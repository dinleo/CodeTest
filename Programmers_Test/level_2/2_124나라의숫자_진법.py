# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3
def solution(n):
    number = n-1
    T = "124"
    i, j = divmod(number, 3)

    if i == 0:
        return T[j]
    else:
        return solution(i, 3) + T[j]

