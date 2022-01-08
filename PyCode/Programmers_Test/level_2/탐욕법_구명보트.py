# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
def solution(people, limit):
    if len(people) == 1:
        return 1
    answer = 0
    people.sort(reverse=True)
    p = people
    i = 0
    j = -1
    # 소팅 후 첫번째 사람과 마지막 사람이 같이 탈수 있으면 태움, 이터레이터 이용
    while 1:
        if p[i] + p[j] <= limit:
            j -= 1
        i += 1
        answer += 1
        if i == len(p):
            break
        # 만약 다음으로 태울 사람이 limit의 절반보다 이하라면 남은 인원은 모두 보트에 2명씩 탈 수 있다.
        if p[i] <= limit/2:
            answer += round((len(p) - i + j + 1) / 2 + 0.1)
            break
    return answer