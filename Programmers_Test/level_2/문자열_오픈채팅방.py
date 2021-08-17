# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
def solution(record):
    answer = []
    record2 = []
    ID = {}

    for i in record:
        record2.append(list(i.split(" ")))

    for i in record2:
        if i[0] != "Leave":
            ID[i[1]] = i[2]

    for i in record2:
        if i[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % (ID[i[1]]))
        elif i[0] == "Leave":
            answer.append("%s님이 나갔습니다." % (ID[i[1]]))
    return answer