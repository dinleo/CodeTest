# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
def solution(n, times):
    answer = 0
    start = 0
    end = min(times)*n

    while start <= end:
        mid = (start+end)//2
        p = 0
        for i in times:
            p += mid//i
            if n <= p:
                answer = mid
                end = mid - 1
                break
        if p < n:
            start = mid + 1

    return answer