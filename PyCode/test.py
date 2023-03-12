def IC(a):
    return int(a)


m = map(IC, input("좌표를 입력해 주세요 : ").split(","))
x = m.__next__()

try:
    y = m.__next__()
except:
    y = "없음처리"

print(x, y)
a = 'test'