# https://programmers.co.kr/learn/courses/30/lessons/84325?language=python3
def solution(table, languages, preference):
    # table 의 첫원소(직업군)만 jobs 에 저장후 reverse
    for i in range(len(table)):
        arr = table[i].split(" ")
        arr.reverse()
        table[i] = arr
    jobs = [i.pop(-1) for i in table]
    score = [0 for _ in jobs]
    # 언어가 table[j] 에 있으면 점수 * 선호도 를 score[j] 에 더해줌
    for i in range(len(languages)):
        for j in range(len(table)):
            if languages[i] in table[j]:
                score[j] += (table[j].index(languages[i])+1) * preference[i]
    # 최고 점수를 갖는 직업들을 추출해 sort 후 pop(0)
    recomends_jobs = [jobs[i] for i in range(len(score)) if score[i] == max(score)]
    recomends_jobs.sort()
    return recomends_jobs[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5]))