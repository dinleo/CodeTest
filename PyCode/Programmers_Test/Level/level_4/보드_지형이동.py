# https://programmers.co.kr/learn/courses/30/lessons/62050?language=python3
import heapq


def solution(land, height):
    # 방문한 land 중에서 항상 최소한의 사다리를 사용해 방문하지 않은곳을 가는 Greedy 재귀 알고리즘 사용
    def explore(i, j, c):
        # maximum recursion 방지
        if c == 10:
            heapq.heappush(next_exp, [0, i, j])
            return
        # [i, j]에서 출발해 갈 수 있는 land 는 visited, 갈 수 없는 land 는 next_exp 에 [높이차이,i좌표,j좌표] 추가
        h = land[i][j]
        visited[i][j] = 1

        if 0 < i and not visited[i - 1][j]:
            h_gap = abs(land[i - 1][j] - h)
            if h_gap <= height:
                explore(i - 1, j, c + 1)
            else:
                heapq.heappush(next_exp, [h_gap, i - 1, j])
        if 0 < j and not visited[i][j - 1]:
            h_gap = abs(land[i][j - 1] - h)
            if h_gap <= height:
                explore(i, j - 1, c + 1)
            else:
                heapq.heappush(next_exp, [h_gap, i, j - 1])
        if i < n - 1 and not visited[i + 1][j]:
            h_gap = abs(land[i + 1][j] - h)
            if h_gap <= height:
                explore(i + 1, j, c + 1)
            else:
                heapq.heappush(next_exp, [h_gap, i + 1, j])

        if j < n - 1 and not visited[i][j + 1]:
            h_gap = abs(land[i][j + 1] - h)
            if h_gap <= height:
                explore(i, j + 1, c + 1)
            else:
                heapq.heappush(next_exp, [h_gap, i, j + 1])

    n = len(land)
    answer = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    next_exp = []
    heapq.heappush(next_exp, [0, 0, 0])

    while 1:
        # next_exp 에 들어있는 land 중, 높이차이가 최소인 land 부터 뽑아 방문하지 않은 land 발견시 explore 시행
        finish = 1
        while 1:
            p = heapq.heappop(next_exp)
            if not visited[p[1]][p[2]]:
                break
        explore(p[1], p[2], 0)
        # 모든 land 를 방문하였으면 종료
        for v in visited:
            if 0 in v:
                finish = 0
                break
        # 그렇지 않으면 answer 에 사용한 사다리 추가 후 계속 탐험
        answer += p[0]
        if finish:
            break

    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
