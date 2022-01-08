import itertools

def solution(dice):
    nums = []
    dice = [[str(j) for j in i] for i in dice]
    com = []
    for i in range(len(dice)+1):
        com.extend(itertools.combinations(range(len(dice)),i))
    for c in com:
        arr = []
        for cc in c:
            arr.append(dice[int(cc)])
        nums.extend(list(itertools.product(*arr)))

    numbers = []
    for n in nums:
        numbers.extend(list(itertools.permutations(n,len(n))))
    numbers.sort()
    for i in range(10000):
        if tuple(str(i)) not in numbers:
            return i



print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))
print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))