# https://school.programmers.co.kr/learn/courses/30/lessons/77887

def solution(values, edges, queries):
    n = len(values)
    answer = []
    parents = [0 for _ in range(n + 1)]
    children = [[] for _ in range(n + 1)]
    sum_v = [0 for _ in range(n + 1)]
    have_parents = [False for _ in range(n+1)]
    have_parents[1] = True
    values.insert(0, 0)

    edges.sort()
    while edges:
        e = edges.pop(0)
        if have_parents[e[0]]:
            parents[e[1]] = e[0]
            children[e[0]].append(e[1])
            have_parents[e[1]] = True
        elif have_parents[e[1]]:
            parents[e[0]] = e[1]
            children[e[1]].append(e[0])
            have_parents[e[0]] = True
        else:
            edges.append(e)

    stack = [1]
    while stack:
        p = stack[-1]
        u = False
        if sum_v[p] == 0:
            if not children[p]:
                sum_v[p] = values[p]
                u = True
            else:
                for c in children[p]:
                    if sum_v[c] == 0:
                        stack.append(c)
                    else:
                        sum_v[p] += sum_v[c]
                        u = True
                if u:
                    sum_v[p] += values[p]
        if u:
            stack.pop()
    for q in queries:
        q1 = q[0]
        q2 = q[1]
        if q2 == -1:
            answer.append(sum_v[q1])
        else:
            s = q1
            while s != 0:
                s_p = parents[s]
                s_c = children[s]
                sums = 0
                for c in s_c:
                    sums += sum_v[c]
                sum_v[s] = sums + values[s_p]
                values[s] = values[s_p]
                s = s_p
            sum_v[1] += q2
            values[1] = q2

    return answer


# print(solution([1, 10, 100, 1000, 10000], [[1, 2], [1, 3], [2, 4], [2, 5]],[[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [4, 1000], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [2, 1], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1]]))
print(solution([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096], [[10, 11], [13, 11], [12, 10], [10, 9], [8, 9], [1, 2], [2, 4], [2, 3], [5, 3], [6, 5], [5, 8], [7, 5]],[[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1], [7, -1], [8, -1], [9, -1], [10, -1], [11, -1], [12, -1], [13, -1]]))