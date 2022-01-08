# https://programmers.co.kr/learn/courses/30/lessons/43236
def solution(distance, rocks, n):
    if n == len(rocks):
        return distance

    r = len(rocks)
    rocks.sort();
    answer = 0

    start = 1
    end = distance

    while start <= end:
        rock_cnt = 0
        mid = (start+end) // 2
        last_rock = 0
        for i in range(r - 1):
            if mid <= rocks[i] - last_rock:
                rock_cnt += 1
                last_rock = rocks[i]
        if mid <= rocks[r-1] - last_rock and mid <= distance - rocks[r-1]:
            rock_cnt += 1
        if rock_cnt < r - n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer

print(solution(25, [2, 11, 14, 17, 21], 3))
