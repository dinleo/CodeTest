# https://programmers.co.kr/learn/courses/30/lessons/87377?language=python3
from itertools import combinations


def solution(line):
    n = list(combinations(range(len(line)), 2))
    dots = []
    for i in n:
        eq1, eq2 = line[i[0]], line[i[1]]
        a, b, e = eq1[0], eq1[1], eq1[2]
        c, d, f = eq2[0], eq2[1], eq2[2]
        if (a * d - b * c) != 0:
            x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
        if x % 1 == 0 and y % 1 == 0:
            dots.append([int(x), int(y)])
    dots.sort()
    x_min, x_max = dots[0][0], dots[-1][0]
    dots.sort(key = lambda x:x[1])
    y_min, y_max = dots[0][1], dots[-1][1]
    board = [["." for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)]
    for d in dots:

        board[y_max-d[1]][d[0]+(-x_min)] = "*"
    answer = ["".join(i) for i in board]
    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
