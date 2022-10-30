from collections import defaultdict
import math

def solution(fees, records):
    # 입출차 시간을 담은 dict park, 차량번호를 담은 list car
    park = defaultdict(list)
    car = []
    fees = list(map(int,fees))
    for i in records:
        r = i.split(" ")
        park[r[1]].append(int(r[0].split(":")[0])*60 + int(r[0].split(":")[1]))
        if r[1] not in car:
            car.append(r[1])

    car.sort()

    # 주차장에 있던 시간을 담을 dict
    t = defaultdict(int)
    for c in car:
        t[c] = 0

    # 요금계산
    answer = []
    car.sort()
    for c in car:
        n = len(park[c])
        if n%2 == 1:
            park[c].append(1439)
        for i in range(0,n,2):
            t[c] += park[c][i+1]-park[c][i]
        if t[c] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((t[c]-fees[0])/fees[2])*fees[3])

    return answer


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))