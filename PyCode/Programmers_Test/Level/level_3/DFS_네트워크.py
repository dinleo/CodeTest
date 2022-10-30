# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        computers[i][i] = 0
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)

    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer +=1
    return answer




print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 2)
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4)
print(solution(6, [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]),1)

print(solution(3, [[1,1,0],[0,1,0],[0,1,1]]))