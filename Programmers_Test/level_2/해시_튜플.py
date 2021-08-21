from collections import defaultdict


def solution(s):
    answer = []
    arr = [i.split(",") for i in s.strip("{").strip("}").split("},{")]
    di = defaultdict(list)
    for i in arr:
        di[len(i)] = i
    for i in range(1, len(arr) + 1):
        answer.append("".join(set(di[i]) - set(answer)))

    return list(map(int,answer))


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
