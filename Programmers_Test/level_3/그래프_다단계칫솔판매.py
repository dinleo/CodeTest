# https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3
import collections


def solution(enroll, referral, seller, amount):
    # 수익을 받을 노드이름과 수익금이 주어지면, 수익금이 10원미만이 되거나 상위노드가 없을때까지, 수익금을 자신과 상위노드로 분배하는 함수
    def distribute(person, money):
        if money < 10:
            money_dict[person] += money
            return
        money_dict[person] += money - money // 10
        if ref_dict[person] != "-":
            distribute(ref_dict[person], money // 10)

    # 이름을 key 로, 추천인과 money 를 val 로 갖는 dict 생성 (index 사용하는것보다 시간이 단축됨)
    ref_dict = collections.defaultdict(str)
    money_dict = collections.defaultdict(str)
    for i in range(len(enroll)):
        ref_dict[enroll[i]] = referral[i]
    for i in enroll:
        money_dict[i] = 0

    # 분배 시행
    for i in range(len(seller)):
        distribute(seller[i], amount[i]*100)

    answer = []
    for i in enroll:
        answer.append(money_dict[i])
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]), [360, 958, 108, 0, 450, 18, 180, 1080])
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]), [0, 110, 378, 180, 270, 450, 0, 0])
