from sys import stdin

N = stdin.readline().split(' ')
if N == 1:
    print(0)
    exit(0)
k = int(N[1])
m = list(map(int, stdin.readline().split(' ')))

arr = []
for i in range(len(m)-1):
    arr.append(abs(m[i+1] - m[i]))
H = list(set(arr))

for h in H:
    exh = 0
    bef = False
    for a in arr:
        if h < a:
            exh += 1
            if not bef:
                exh += 1
            bef = True
        else:
            bef = False
        if k < exh:
            break
    if exh <= k:
        print(h)
        exit(0)
