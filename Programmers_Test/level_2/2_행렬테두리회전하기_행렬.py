def solution(rows, columns, queries):
    answer = []
    arr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    for q in queries:
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        cir_arr = []

        # x1,y1부터 시계방향으로 cir_arr에 담음
        for y in range(y1, y2 + 1):
            cir_arr.append(arr[x1][y])
        for x in range(x1 + 1, x2 + 1):
            cir_arr.append(arr[x][y2])
        for y in range(y2 - 1, y1 - 1, -1):
            cir_arr.append(arr[x2][y])
        for x in range(x2 - 1, x1, -1):
            cir_arr.append(arr[x][y1])

        answer.append((min(cir_arr)))
        i = -1

        # cir_arr[-1]부터 arr에 다시 담음
        for y in range(y1, y2 + 1):
            arr[x1][y] = cir_arr[i]
            i += 1
        for x in range(x1 + 1, x2 + 1):
            arr[x][y2] = cir_arr[i]
            i += 1
        for y in range(y2 - 1, y1 - 1, -1):
            arr[x2][y] = cir_arr[i]
            i += 1
        for x in range(x2 - 1, x1, -1):
            arr[x][y1] = cir_arr[i]
            i += 1

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
