S = input()
k = 'KOREA'
k_i = 0
y = 'YONSEI'
y_i = 0

for s in S:
    if s == k[k_i]:
        k_i += 1
    if k_i == 5:
        print(k)
        break
    if s == y[y_i]:
        y_i += 1
    if y_i == 6:
        print(y)
        break
