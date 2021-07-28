def solution(n, edge):
    node = [[]]*(n+1)
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
    for i in node:
        if 1 in i:
            i.remove(1)

    def check(n):
        a = 0
        if node[n] == []:
            return 1
        else:
            for i in node[n]:
                for j in range(n + 1, len(node)):
                    if i in node[j]:
                        node[j].remove(i)
            for i in node[n]:
                a += check(i)
            return a

    return check(1)



print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))