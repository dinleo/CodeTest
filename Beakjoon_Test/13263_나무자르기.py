N = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

first_root = []

is_best = [1] * (N - 1)
# 각 루트를 시작루트로 정했을때 드는 비용 first_root
for i in range(1, N):
    first_root.append(b[0] * a[i])

answer_list = [sum(first_root)]


# 현재 루트까지 오는데 드는비용 cost, 현재루트 i
# 마지막 루트에 도착할 때 까지 재귀함수, 마지막루트에 도착하면 총 비용 answer에저장
def find_root(cost, i):
    if cost > min(answer_list):
        return
    if i == N - 1:
        answer_list.append(cost)
        return
    temp = []
    for j in range(i + 1, N):
        temp.append(cost + b[i] * a[j])

    for j in range(len(temp)):
        if j == len(temp) - 1:
            if temp[j] < min(answer_list):
                answer_list.append(temp[j])
            return
        elif temp[j] > first_root[i + j]:
            pass
        else:
            # 시작루트로 굳이 고를 필요 없다면 best 시작루트에서 제외
            is_best[i + j] = 0
            find_root(temp[j], i + j + 1)


# best 시작루트만 검사
for i in range(N - 1):
    if is_best[i] == 1:
        find_root(first_root[i], i + 1)

print(is_best)
print(min(answer_list))
