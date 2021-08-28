# https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3
from collections import defaultdict


def solution(N, road, K):
    def deliver(n,count):
        if visited[n] is not None:
            if visited[n] <= count:
                return
        if K < count:
            return
        visited[n] = count
        for i in node[n].keys():
            deliver(i, count + node[n][i])
        return

    visited = [None for _ in range(N + 1)]
    node = [defaultdict(int) for _ in range(N + 1)]
    for r in road:
        if node[r[0]][r[1]]:
            node[r[0]][r[1]] = min(node[r[0]][r[1]],r[2])
        else:
            node[r[0]][r[1]] = r[2]
        if node[r[1]][r[0]]:
            node[r[1]][r[0]] = min(node[r[1]][r[0]],r[2])
        else:
            node[r[1]][r[0]] = r[2]
    deliver(1, 0)
    answer = len(visited) - visited.count(None)

    return answer

print(solution(5,[[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6,[[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
