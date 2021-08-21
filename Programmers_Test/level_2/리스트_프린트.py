def solution(priorities, location):
    answer = 1
    while 1:
        m = max(priorities)
        if priorities[0] == m:
            priorities.pop(0)
            if location == 0:
                break
            else:
                answer += 1
                location -= 1
                if location == -1:
                    location = len(priorities) - 1
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            location -= 1
            if location == -1:
                location = len(priorities) - 1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
