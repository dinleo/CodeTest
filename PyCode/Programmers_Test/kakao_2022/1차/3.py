from itertools import product


def solution(users, emoticons):
    disc = [10, 20, 30, 40]
    pdct = list(product(disc, repeat=len(emoticons)))
    max_plus_user = 0
    max_margin = 0
    for p in pdct:
        plus_user = 0
        margin = 0
        for u in users:
            total_cost = 0
            for i in range(len(p)):
                if u[0] <= p[i]:
                    price = emoticons[i] * ((100 - p[i]) / 100)
                    total_cost += price
                if u[1] <= total_cost:
                    total_cost = 0
                    plus_user += 1
                    break
            margin += total_cost
        if max_plus_user < plus_user:
            max_plus_user = plus_user
            max_margin = margin
        elif max_plus_user == plus_user:
            if max_margin < margin:
                max_margin = margin

    return [max_plus_user, int(max_margin)]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
               [1300, 1500, 1600, 4900]))
