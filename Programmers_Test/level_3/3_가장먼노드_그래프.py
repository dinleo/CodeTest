def solution(n, edge):
    import collections
    check = [1]+[0]*(n-1)
    vec = [[]for i in range(n)]
    que = collections.deque([1])
    for i in edge:
        vec[i[0]-1].append(i[1])
        vec[i[1]-1].append(i[0])

    # que에는 차례대로 다음 노드집합(단, 이미 지난 노드(check) 제외)가 담김. ex) [1] -> [2,3] -> [6,4,5]
    # 다음으로 갈수 있는 노드가 없어서 que가 null이 되면 종료.
    # l에는 마지막으로 담겼던 que의 length. ex) 3
    while que:
        l = len(que)
        for i in range(l):
            q = que.popleft()
            for e in vec[q-1]:
                if check[e-1] == 0:
                    check[e-1] = 1
                    que.append(e)
    return l

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))