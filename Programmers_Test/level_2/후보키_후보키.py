# https://programmers.co.kr/learn/courses/30/lessons/42890?language=python3
from itertools import combinations


def solution(relation):
    global rel
    rel = relation
    answer = 0
    # 후보키가 될수 있는 모든 속성군 조합을 생성
    com = []
    for i in range(1,len(rel[0])+1):
        com.extend(list(map(set, combinations([i for i in range(len(rel[0]))],i))))
    # 모든 속성군 조합에 대해 후보키인지 검사
    while com:
        attribute = com.pop(0)
        # 후보키인 속성군을 발견하면 answer +1 해준 후, 해당속성군을 부분집합으로 갖는 모든 속성군을 검사대상에서 제외
        if is_candidate(attribute):
            answer += 1
            temp = []
            for i in com:
                if not attribute <= i:
                    temp.append(i)
            com = temp

    return answer


def is_candidate(attribute):
    # attribute (ex, {0,2,3}) 의 속성군이 후보키면 True 를 리턴하는 함수
    temp = []
    for i in range(len(rel)):
        temp_temp = ""
        for j in attribute:
            temp_temp += rel[i][j]
        temp.append(temp_temp)
    if len(temp) == len(set(temp)):
        return True
    else:
        return False


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
