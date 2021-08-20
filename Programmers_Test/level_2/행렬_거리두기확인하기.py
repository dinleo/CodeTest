# https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3
def solution(places):
    global place
    answer = [0 for _ in range(5)]
    place = places
    for p in range(5):
        answer[p] = check_p(p)
    return answer


def check_p(p):
    # p번째 방에서 첫 "P"를 찾으면 check("P"의좌표")시행, 거리두기 안지킨걸 발견하면 0반환후 종료
    for i in range(5):
        for j in range(5):
            if place[p][i][j] == "P":
                if check([i, j], p, i, j, 0) != 0:
                    return 0
    return 1


def check(arr, p, i, j, c):
    # 규격을 초과하거나 X를 만나면 0반환
    if (c == 3) or (i < 0) or (4 < i) or (j < 0) or (4 < j):
        return 0
    if place[p][i][j] == "X":
        return 0
    # 시작점의 좌표인 arr의 "P"가 아닌 "P"를 만나면 1반환
    if place[p][i][j] == "P":
        if (c != 0) and (arr != [i, j]):
            return 1
    # 기준점 [i,j]로부터 4방향을 모두 확인
    return check(arr, p, i - 1, j, c + 1) + check(arr, p, i, j - 1, c + 1) + check(arr, p, i + 1, j, c + 1) + check(arr, p, i, j + 1, c + 1)


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))