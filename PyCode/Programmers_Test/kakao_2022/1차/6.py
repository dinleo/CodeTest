def solution(n, m, x, y, r, c, k):
    answer = ''
    a_hor = abs(x - r)
    a_ver = abs(c - y)
    a_tot = a_ver + a_hor

    if k < a_tot or (k - a_tot) % 2 == 1:
        return "impossible"

    while k != 0:
        hor = x - r
        ver = c - y
        tot = abs(ver) + abs(hor)

        if hor < 0 or (tot + 2 <= k and x < n):
            answer += 'd'
            x += 1
        elif ver < 0 or (tot + 2 <= k and 1 < y):
            answer += 'l'
            y -= 1
        elif ver!=0 or (tot != k and x==n and y==1):
            answer += 'r'
            y += 1
        else:
            answer += 'u'
            x -= 1
        k -= 1

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
