# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
from collections import defaultdict


def solution(user_id, banned_id):
    d = defaultdict(list)
    for i in range(len(banned_id)):
        b = banned_id[i]
        for u in user_id:
            catch = True
            if len(b) != len(u):
                continue
            ln = len(b)
            for j in range(ln):
                if b[j] != "*":
                    if b[j] != u[j]:
                        catch = False
                        break
            if catch:
                d[i].append(u)

    answer = 0
    return d


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
