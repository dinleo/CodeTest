# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        orders_com = []  # 손님들의 주문을 c개의 단품 조합으로 분해해 저장한 리스트 (ex. {'A','C'},{'A','B'},...)
        orders_set = []  # orders_com 에서 중복을 제거한 리스트. 가능한 모든 조합
        orders_count = []  # 각 조합이 출현한 횟수를 저장한 리스트
        for o in orders:
            orders_com.extend(list(map(set, (combinations(o, c)))))
        for o in orders_com:
            if o not in orders_set:
                orders_set.append(o)
        # orders_set 의 각 조합이 order_com 에 출현한 횟수를 order_count 에 담는다
        for o in orders_set:
            orders_count.append(orders_com.count(o))

        # 최소 2번 이상 주문된 조합중 가장 많이 주문된 조합을 정답에 추가
        if orders_count:
            max_count = max(orders_count)
            if 2 <= max_count:
                for a in range(len(orders_count)):
                    if orders_count[a] == max_count:
                        answer.append("".join(sorted(list(orders_set[a]))))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]), ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]), ["WX", "XY"])
