def solution(a, b, g, s, w, t):
    n = len(g)
    gold = [[0,i] for i in range(n)]
    silver = [[0,i] for i in range(n)]

    for i in range(n):
        gold[i][0] = max(g[i], w[i])/t[i]
        silver[i][0] = max(s[i], w[i])/t[i]
    gold.sort()
    silver.sort()
    answer = -1
    return answer





print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))