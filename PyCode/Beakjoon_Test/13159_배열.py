# 13159
import sys

NQ = list(map(int, input().split()))
N = NQ[0]
Q = NQ[1]
a = []
Pb = [0]*Q
a = [i for i in range(1,N+1)]

for i in range(Q):
    Pb[i] = list(map(int,sys.stdin.readline().rstrip().split()))


def p1(t, r):
    temp = a[t - 1:r]
    min = temp[0]
    max = temp[0]
    sum = 0
    for i in temp:
        if i < min: min = i
        if i > max: max = i
        sum += i
    print(min,max,sum)
    j = 0
    for i in range(r - 1, t - 2, -1):
        a[i] = temp[j]
        j += 1


def p2(t, r, x):
    temp = a[t - 1:r]
    min = temp[0]
    max = temp[0]
    sum = 0
    for i in temp:
        if i < min: min = i
        if i > max: max = i
        sum += i
    print(min, max, sum)
    if 0 <= x:
        shift = x
    else:
        shift = r - t + 1 + x
    j = 0
    for i in range(t - 1, t + shift - 1):
        a[i] = temp[-shift + j]
        j += 1

    j = 0
    for i in range(t + shift - 1, r):
        a[i] = temp[j]
        j += 1


def p3(t):
    print(a[t - 1])


def p4(x):
    print(a.index(x) + 1)


for i in range(Q):
    Pb_q = Pb[i]
    if Pb_q[0] == 1:
        p1(Pb_q[1], Pb_q[2])
    if Pb_q[0] == 2:
        p2(Pb_q[1], Pb_q[2], Pb_q[3])
    if Pb_q[0] == 3:
        p3(Pb_q[1])
    if Pb_q[0] == 4:
        p4(Pb_q[1])

for i in range(N):
    print(a[i], end=" ")
