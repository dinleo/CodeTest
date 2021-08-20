# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
def solution(n, results):
    if n == 1:
        return 1
    answer = 0
    global next_n
    global prev_n
    next_n = [[] for i in range(n + 1)]
    prev_n = [[] for i in range(n + 1)]

    for i in results:
        next_n[i[1]].append(i[0])
        prev_n[i[0]].append(i[1])

    print(next_n)
    print(prev_n)
    for i in range(1, n + 1):
        for j in next_n[i]:
            add_next(i, j)
        for j in prev_n[i]:
            add_prev(i, j)

    for i in range(1, n + 1):
        if len(next_n[i]) + len(prev_n[i]) == n - 1:
            answer += 1
    print(next_n)
    print(prev_n)
    return answer


def add_next(self, i):
    # '자신보다 next인 선수'보다 next인 선수들을 모두 추가
    if not next_n:
        if i not in next_n[self]:
            next_n[self].append(i)
        return
    for j in next_n[i]:
        if j not in next_n[self]:
            next_n[self].append(j)
            add_next(self, j)


def add_prev(self, i):
    # '자신보다 prev인 선수'보다 prev인 선수들을 모두 추가
    if not prev_n:
        if i not in prev_n[self]:
            prev_n[self].append(i)
        return
    for j in prev_n[i]:
        if j not in prev_n[self]:
            prev_n[self].append(j)
            add_prev(self, j)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
