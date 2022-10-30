# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3
from itertools import product


def solution(user_id, banned_id):
    d = []
    ld = len(banned_id)
    for i in range(len(banned_id)):
        b = banned_id[i]
        d.append([])
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
    pro = list(product(*d))
    set_pro = []
    for p in pro:
        s = set(p)
        if (len(s) == ld) and (s not in set_pro):
            set_pro.append(s)

    return len(set_pro)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
