def solution(bd, k, ax, ay):
    answer = 999999
    b = len(bd)
    k += 1

    def out_of_range(x):
        if x < 0 or b <= x:
            return True
        else:
            return False

    def bomb(x, y):
        bd[x][y] = 2
        for i in range(x + 1, x + k):
            if out_of_range(i) or bd[i][y] == 2:
                break
            if bd[i][y] == 0:
                bd[i][y] = 3
        for i in range(x - 1, x - k, -1):
            if out_of_range(i) or bd[i][y] == 2:
                break
            if bd[i][y] == 0:
                bd[i][y] = 3
        for i in range(y + 1, y + k):
            if out_of_range(i) or bd[x][i] == 2:
                break
            if bd[x][i] == 0:
                bd[x][i] = 3
        for i in range(y - 1, y - k, - 1):
            if out_of_range(i) or bd[x][i] == 2:
                break
            if bd[x][i] == 0:
                bd[x][i] = 3


    for i in range(b):
        for j in range(b):
            if bd[i][j] == 1:
                bomb(i, j)

    visited = [[False for _ in range(b)] for _ in range(b)]
    visited[ax][ay] = -1

    stack = [[ax, ay, 0]]
    while stack:
        p = stack.pop(0)
        if bd[p[0]][p[1]] == 0:
            if p[2] < answer:
                answer = p[2]
            continue
        arr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for a in arr:
            new_stack = [p[0] + a[0], p[1] + a[1], p[2] + 1]
            x = new_stack[0]
            y = new_stack[1]
            if not out_of_range(x) and not out_of_range(y):
                if bd[x][y] == 2:
                    continue
                elif not visited[x][y] or new_stack[2] < visited[x][y]:
                    stack.append(new_stack)
                    visited[x][y] = new_stack[2]

    for i in bd:
        print(i)
    for v in visited:
        print(v)

    if answer == 999999:
        return -1

    return answer


print(solution([[0, 0, 1, 0, 0, 0], [0, 2, 0, 0, 0, 1], [0, 0, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0]], 2, 1, 2))

print(solution([[0,0,0,1],[0,2,0,1],[2,0,0,1],[0,2,0,1]], 2, 2, 1))