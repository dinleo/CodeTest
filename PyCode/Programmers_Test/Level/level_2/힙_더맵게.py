# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq


def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q,i)

    while 1:
        a = heapq.heappop(q)
        if a >= K:
            break
        if len(q) == 0:
            return -1
        b = heapq.heappop(q)
        heapq.heappush(q, a+b*2)
        answer += 1
    return answer