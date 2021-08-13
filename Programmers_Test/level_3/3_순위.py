def solution(n, results):
    if n == 1:
        return 1
    g_win = [[] for i in range(n)]
    g_lose = [[] for i in range(n)]
    g_count = [0 for i in range(n)]
    for i in results:
        i[0] -= 1
        i[1] -= 1

    # r[0]승자 r[1]패자
    for r in results:
        win_count = 1
        lose_count = 1
        # 승리시, 패자 아래있는 인원수까지 count +=
        for i in g_win[r[1]]:
            if i not in g_win[r[0]]:
                win_count += 1
        # 패배시, 승자 위있는 인원수까지 count +=
        for i in g_lose[r[0]]:
            if i not in g_lose[r[1]]:
                lose_count += 1
        g_count[r[0]] += win_count
        g_count[r[1]] += lose_count

        g_lose[r[1]].append(r[0])
        g_win[r[0]].append(r[1])

    answer = g_count.count(n - 1)
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
