# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
def solution(triangle):
    triangle.reverse()
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])-1):
            triangle[i+1][j] += max(triangle[i][j],triangle[i][j+1])

    return triangle[-1][0]



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))