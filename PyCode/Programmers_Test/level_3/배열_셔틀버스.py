# https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3
def solution(n, t, m, timetable):
    current_time = 540
    timetable = [int(i.split(":")[0])*60 + int(i.split(":")[1]) for i in timetable]
    timetable.sort()

    # 마지막 버스가 아닌 버스는 모두 먼저 태워 보내준다.
    while n != 1:
        c = m
        while timetable and c != 0:
            p = timetable.pop(0)
            if current_time < p:
                timetable.insert(0, p)
                break
            c -= 1
        n -= 1
        current_time += t

    # 마지막 버스에 탈 수 있는 인원만 last_table 에 저장
    last_table = []
    while timetable and len(last_table) < m:
        p = timetable.pop(0)
        if current_time < p:
            break
        last_table.append(p)

    # 마지막버스에 자리가 충분하면, 마지막 버스시간에 도착
    if len(last_table) != m:
        answer = current_time
    else:
        # 자리가 충분하지 않으면, 남은 크루들 중 가장 늦게 도착한 크루보다 1분 먼저 도착
        answer = last_table[0] - 1

    return "{0:0>2d}:{1:0>2d}".format(answer // 60, answer % 60)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(1, 1, 1, ["09:00", "09:05"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01", "00:02", "00:03", "00:04"]))
print(solution(10, 1, 5, ["09:00", "09:00", "09:00", "09:00", "09:00"]))
print(solution(2, 10, 3, ["09:05", "09:09", "09:13"]))
print(solution(4, 120, 2, ["09:10", "09:09", "08:00", "24:00","05:33","12:11","17:59","15:00","11:33","15:00"]))
print(solution(1,1,1,["24:00"]))
