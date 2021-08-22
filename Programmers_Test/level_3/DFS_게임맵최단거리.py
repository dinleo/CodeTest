# https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
def solution(maps):
    global n, m, map, route_count, min_route, save_point
    n, m = len(maps), len(maps[0])
    map = maps
    route_count = []  # 목적지 도달시 각 경로로 걸린 count 를 저장 할 배열
    min_route = [[-1 for _ in range(m)] for _ in range(n)]
    save_point = []  # 재귀 깊이가 약 500을 도달 했을 때를 대비한 save_point (ex, [[i,j,count],[...],...])

    # 시작점에 대해 next_step 시행
    next_step(0, 0, 1, 0)

    # save_point 가 존재한다면 save_point 부터 다시 시행
    while save_point:
        s = save_point.pop(0)
        next_step(s[0], s[1], s[2], 0)

    if route_count:
        return min(route_count)
    else:
        return -1


def next_step(i, j, count, new_count):  # 상하좌우로 캐릭터를 움직이며 길을 찾는 함수
    if new_count == 10:  # 깊이 약 10의 재귀 도달시 save_point 에 저장
        save_point.append([i, j, count])
        return
    # 목적지 도달시 걸음 수를 route_count 에 추가
    if i == n - 1 and j == m - 1:
        route_count.append(count)
    # 다른 경로에서 이미 더 적은 count 로 올 수 있다면 함수 종료
    if min_route[i][j] != -1:
        if min_route[i][j] <= count:
            return
    min_route[i][j] = count
    # 벽이 아니면 상하좌우에 대해 재귀시행
    if i != n - 1 and map[i + 1][j] != 0:
        next_step(i + 1, j, count + 1, new_count + 1)
    if j != m - 1 and map[i][j + 1] != 0:
        next_step(i, j + 1, count + 1, new_count + 1)
    if i != 0 and map[i - 1][j] != 0:
        next_step(i - 1, j, count + 1, new_count + 1)
    if j != 0 and map[i][j - 1] != 0:
        next_step(i, j - 1, count + 1, new_count + 1)


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
