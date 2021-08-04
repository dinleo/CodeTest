import math

def solution(price, money, count):
    fee = int(price*math.fsum(i for i in range(1,count+1)))
    if money < fee:
        return fee - money
    else:
        return 0

print(solution(3,20,4))