# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
def solution(bridge_length, weight, truck_weights):
    answer = 0
    l = bridge_length
    w = weight
    t = truck_weights
    # 각 트럭이 다리위에서 있는 시간을 담은 리스트, bridge에는 현재 다리위에 있는 트럭의 무게의 합
    t_t = [0]*len(t)
    bridge = 0
    # 인덱스, i번째부터 j번째 트럭까지 현재 다리 위에 있다.
    i = 0
    j = -1
    while 1:
        answer += 1
        print("=========",answer,"초 ============")
        if j + 1 < len(t):
            if bridge + t[j+1] <= w:
                j += 1
                bridge += t[j]
        for k in range(i,j+1):
            t_t[k] += 1
        if t_t[i] == l:
            bridge -= t[i]
            i += 1
        print(i, j, answer, t_t)
        if t_t[len(t)-1] == l:
            break
    return answer + 1


solution(2,10,[7,4,5,6])