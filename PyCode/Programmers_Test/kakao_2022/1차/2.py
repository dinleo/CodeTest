def solution(cap, n, deliveries, pickups):
    answer = 0
    end_idx = [n - 1, n - 1]

    while end_idx != [-1, -1]:
        while end_idx[0] != -1 and deliveries[end_idx[0]] == 0:
            end_idx[0] -= 1
        while end_idx[1] != -1 and pickups[end_idx[1]] == 0:
            end_idx[1] -= 1

        answer += max(end_idx[0] + 1, end_idx[1] + 1)
        c = cap
        while -1 < end_idx[0] and c != 0:
            if deliveries[end_idx[0]] == 0:
                end_idx[0] -= 1
            else:
                if c - deliveries[end_idx[0]] < 0:
                    deliveries[end_idx[0]] -= c
                    break
                else:
                    c -= deliveries[end_idx[0]]
                    deliveries[end_idx[0]] = 0
                    end_idx[0] -= 1

        c = cap
        while -1 < end_idx[1] and c != 0:
            if pickups[end_idx[1]] == 0:
                end_idx[1] -= 1
            else:
                if c - pickups[end_idx[1]] < 0:
                    pickups[end_idx[1]] -= c
                    break
                else:
                    c -= pickups[end_idx[1]]
                    pickups[end_idx[1]] = 0
                    end_idx[1] -= 1

    return answer*2


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
