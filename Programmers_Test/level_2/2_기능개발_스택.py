def solution(progresses, speeds):
    answer = []
    while progresses != []:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        while (progresses != []) and (progresses[0] >= 100) :
            del progresses[0]
            del speeds[0]
            count += 1
        if count != 0:
            answer.append(count)

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
