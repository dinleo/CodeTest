# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3


def solution(jobs):
    times = []  # 처리시간을 담을 배열
    jobs.sort()
    min_index = 0
    t = 0  # 현재시간
    # 시행할 수 있는 작업중 가장 짧은 처리시간을 갖는 작업을 우선으로 시행후, times 에 처리시간을 추가
    while jobs:
        # 남은 작업중 첫 작업(jobs[0])의 요청시간이 현재시간보다 뒤면, 무조건 첫 작업 시행
        if t <= jobs[0][0]:
            p = jobs.pop(0)
            t = p[0] + p[1]
            times.append(t - p[0])
        # 이전 작업을 완료 후, 요청시간이 현재시간보다 앞쪽에 있는 작업들 중 가장 짧은 처리시간을 갖는 작업을 시행
        else:
            p = jobs.pop(min_index)
            t = t + p[1]
            times.append(t - p[0])
        min_index = 0
        min_val = 1000
        # 요청시간이 현재시간보다 앞쪽에 있는 작업들 중 가장 짧은 처리시간을 갖는 작업의 index 를 찾는다.
        for i in range(len(jobs)):
            if t <= jobs[i][0]:
                break
            if jobs[i][1] < min_val:
                min_index = i
                min_val = jobs[i][1]
    return int(sum(times)/len(times))


print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)