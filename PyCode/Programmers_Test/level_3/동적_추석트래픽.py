# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
def solution(lines):
    answer = 0
    log = []
    for i in lines:
        log.append(get_sec(i))
    # 모든 처리의 시작, 끝 구간을 기준으로 1초 체크
    for times in log:
        for t in times:
            t_end = round(t + 0.999, 3)
            count = 0
            for i in log:
                if (t <= i[0] <= t_end) or (t <= i[1] <= t_end):
                    count += 1
                elif (i[0] <= t) and (t_end <= i[1]):
                    count += 1
            if answer < count:
                answer = count
    print(log)
    return answer


def get_sec(s):
    # 로그를 초로 바꿔주는 함수 (0~86400초)
    times = s.split(" ")
    sec_arr = list(map(float, times[1].split(":")))
    sec = sec_arr[0] * 3600 + sec_arr[1] * 60 + sec_arr[2]
    arr = [round(sec - float(times[2].strip('s')) + 0.001, 3), round(sec, 3)]
    return arr


print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
