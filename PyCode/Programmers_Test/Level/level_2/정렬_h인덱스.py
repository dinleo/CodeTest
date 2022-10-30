# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i in range(n):
        if citations[i] < i+1:
            return i
    if citations[0] == 0 or citations[0] == 1:
        return citations[0]
    return n


print(solution([3, 0, 6, 1, 5]))
