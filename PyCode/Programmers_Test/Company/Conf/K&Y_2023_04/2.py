from sys import stdin

N = int(stdin.readline())
m = list(map(int, stdin.readline().split(' ')))
m.sort()

even_min = -1
odd_min = -1

for i in range(N-1):
    dis = m[i+1] - m[i]
    if dis % 2 == 0:
        if even_min == -1 or dis < even_min:
            even_min = dis
    else:
        if odd_min == -1 or dis < odd_min:
            odd_min = dis

print('{0} {1}'.format(even_min, odd_min))
