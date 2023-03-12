import math


def solution(record):
    d = dict()
    medal_rec = []
    l = len(record)
    for medal in record:
        key = []
        name = medal.split(":")[0]
        rec = medal.split(":")[1].split(",")
        m_rec = [name]
        m_rec.extend(rec)
        medal_rec.append(m_rec)
        count = 0
        diff = 1
        s = 0
        for i in range(len(rec)):
            s += int(rec[i])
            if 0 < int(rec[i]):
                count += 1
                diff = i+1
        key.append(-count)
        key.append(-diff)
        key.extend([0,0,0])
        key.append(s)
        key.append(name)
        d[name] = key

    for n in range(5):
        medal = []
        for i in range(l):
            m = []
            if medal_rec[i][n+1] == '0':
                m.append(20001)
            else:
                m.append(int(medal_rec[i][n+1]))
            m.append(medal_rec[i][0])
            medal.append(m)
        medal.sort()
        gold = math.ceil(l/12)
        silver = math.ceil(l/4)
        bronze = math.ceil(l/2)

        for l in range(1, l+1):
            if l <= gold:
                d[medal[l][1]][2] += 1
            elif l <= silver:
                d[medal[l][1]][3] += 1
            elif l <= bronze:
                d[medal[l][1]][4] += 1
    a = []
    answer = []
    for key in d:
        a.append(d[key])
    a.sort()
    for i in range(len(a)):
        answer.append(a[i][-1])
    return answer


print(solution(
    ["jack:9,10,13,9,15", "jerry:7,7,14,10,17", "jean:0,0,11,20,0", "alex:21,2,7,11,4", "kevin:8,4,5,0,0", "brown:3,5,16,3,18", "ted:0,8,0,0,8", "lala:0,12,0,7,9", "hue:17,16,8,6,10", "elsa:11,13,10,4,13"]))