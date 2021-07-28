def solution(n, edge):
    if n == 1:
        return 0
    if n == 2:
        return 1
    node = [[]] * (n + 1)
    cost = [20000] * (n + 1)
    cost[0] = 0
    cost[1] = 0
    edge.sort()
    for i in edge:
        temp = node[i[0]].copy()
        if i[1] not in temp:
            temp.append(i[1])
        node[i[0]] = temp
        temp = node[i[1]].copy()
        if i[0] not in temp:
            temp.append(i[0])
        node[i[1]] = temp

    def check(j, c):
        for i in node[j]:
            if cost[i] > c + 1:
                cost[i] = c + 1
        for i in node[j]:
            if cost[i] == c + 1:
                check(i, c + 1)
        return

    check(1, 0)
    for i in range(n + 1):
        if cost[i] == 20000:
            cost[i] = 0
    max_cost = max(cost)
    print(cost)
    return cost.count(max_cost)


print(solution(7, [[1, 2], [1, 3], [2, 3], [3, 5], [5, 7], [7, 1]]))
