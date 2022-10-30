# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3
def solution(routes):
    answer = 0
    s_routes = sorted(routes)
    # 맨 처음구간을 루트에서 꺼내 r에 담은 후, 루트에서 제거하고 카메라 갯수 +1
    # 루트의 다음 요소 중 r구간과 겹치는 요소가 있으면 루트에서 제거후, r을 중복된 구간으로 변경
    while 1:
        r = s_routes[0]
        del s_routes[0]
        answer += 1
        while 1:
            if s_routes == []:
                break
            elif s_routes[0][0] <= r[1]:
                r[0] = max(r[0],s_routes[0][0])
                r[1] = min(r[1],s_routes[0][1])
                del s_routes[0]
            else:
                break
        if s_routes == []:
            break
    return answer