# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
def solution(info, query):
    answer = [0 for _ in range(len(query))]

    # str -> list 로 변형
    info = [info[i].split(" ") for i in range(len(info))]
    query = [[j for j in query[i].split(" ") if j != "and"] for i in range(len(query))]

    # [[score, {key}], ...] 형식으로 변환
    info = [[int(info[i][-1])] + [set(info[i][:4])] for i in range(len(info))]
    # [[score, {key}, query_index1], ...] 형식으로 변환 (key 에서 "-" 제외)
    query = [[int(query[i][-1])] + [set(j for j in query[i][:4] if j != "-")]+[i] for i in range(len(query))]

    query.sort()
    for i in info:
        for q in query:
            # 지원자의 점수가 요구점수보다 낮아진 순간 순회 break 후, 다음 지원자 탐색
            if i[0] < q[0]:
                break
            # query 의 key_set 이 지원자의 key_set 의 부분집합이면, q[2](sort 전 query 인덱스)를 참조해 answer 증가
            if q[1] <= i[1]:
                answer[q[2]] += 1
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
