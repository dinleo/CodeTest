# https://programmers.co.kr/learn/courses/30/lessons/12985
import math


def solution(n, a, b):
    aa, bb = min(a, b), max(a, b)
    a, b = aa, bb
    # n/2 를 기준으로 왼쪽조, 오른쪽조로 나누었을때 서로 다른조에 속해 있다면 최대 경기값을 return
    if a <= n / 2 < b:
        return int(math.log(n, 2))
    # 같은조에 속해 있다면 n/2명의 경기로 번호를 다시 부여 후 재귀시행
    if b <= n / 2:
        return solution(int(n / 2), a, b)
    else:
        return solution(int(n / 2), a-int(n/2), b-int(n/2))



# print(solution(8, 1, 5))
print(solution(8, 2, 3))
print(solution(8, 4, 7))

# 모범 답안
