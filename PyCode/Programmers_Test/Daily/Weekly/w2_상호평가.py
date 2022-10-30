# https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3
def solution(scores):
    # 전치행렬
    l = len(scores)
    n_scores = [[scores[i][j] for i in range(l)] for j in range(l)]

    # max ro min 일때 일단 pop한 뒤, 안에 같은 값이 있으면 다시 넣어 줌
    for i in range(l):
        if n_scores[i][i] == max(n_scores[i]) or n_scores[i][i] == min(n_scores[i]):
            pop_score = n_scores[i][i]
            del n_scores[i][i]
            if pop_score in n_scores[i]:
                n_scores[i].append(pop_score)

    grade = [get_grade((sum(i) / len(i))) for i in n_scores]

    return "".join(grade)


def get_grade(s):
    if 90 <= s: return 'A'
    elif 80 <= s: return 'B'
    elif 70 <= s: return 'C'
    elif 50 <= s: return 'D'
    else: return 'F'


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
