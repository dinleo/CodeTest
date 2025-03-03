# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict


def solution(S):
    c_log = defaultdict(int)

    for line in S.split("\n"):
        dur, p_num = line.strip().split(",")
        dur = dur.strip()
        p_num = p_num.strip()
        hh, mm, ss = map(int, dur.split(":"))
        total_sec = hh * 3600 + mm * 60 + ss
        c_log[p_num] += total_sec

    max_dur = max(c_log.values())
    max_numbers = [number for number, duration in c_log.items() if duration == max_dur]
    max_numbers.sort()
    max_num = max_numbers[0]

    answer = 0
    for p_num, dur in c_log.items():
        if p_num == max_num:
            continue
        if dur < 300:
            answer += dur * 3
        else:
            answer += ((dur + 59) // 60) * 150

    return answer


print(solution("00:01:07,400-234-090\n00:06:00,701-080-080\n00:05:00,400-234-090"))
