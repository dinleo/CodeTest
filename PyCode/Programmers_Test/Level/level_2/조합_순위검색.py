# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
from collections import defaultdict
import bisect
import heapq


def solution(info, query):
    answer = []
    # [[keys, score], ...] 형식으로 변환
    query = [[j for j in query[i].split(" ") if j != "and"] for i in range(len(query))]
    query = [["".join(query[i][0:4])] + [int(query[i][-1])] for i in range(len(query))]

    # "javabackendjuniorpizza" 등을 key 로 갖고 점수를 value 로 갖는 dic 생성
    dic = defaultdict(list)
    for i in info:
        person = i.split(" ")
        for j in range(16):
            # bin 을 이용해 "-"를 포함해 나올 수 있는 모든 keys 경우의 수에 점수 추가 (ex, "----","---pizza",...,"javabackendjuniorpizza")
            s = ""
            bin_code = "{0:0>4s}".format(bin(j).split("b")[-1])
            for k in range(4):
                if bin_code[k] == "0":
                    s += "-"
                else:
                    s += person[k]
            bisect.insort(dic[s], int(person[-1]))

    # score 기준을 넘기는 인원이 몇 명인지 count
    for q in query:
        arr = dic[q[0]]
        if not arr:
            answer.append(0)
            continue
        answer.append(len(arr) - bisect.bisect_left(arr, q[1]))

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
