# https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3
import collections


def solution(n, s, a, b, fares):

    cost_dict = collections.defaultdict(dict)
    for i in fares:
        cost_dict[str(i[0])][str(i[1])] = i[2]
        cost_dict[str(i[1])][str(i[0])] = i[2]

    def find_best_cost(start, goal):
        stack = [start]
        best_cost = {start: 0}
        while stack:
            p = stack.pop(0)
            if p == goal:
                continue
            p_cost = best_cost[p]
            near_nodes = list(cost_dict[p].keys())
            for node in near_nodes:
                node_cost = p_cost + cost_dict[p][node]
                if node not in best_cost.keys() or node_cost < best_cost[node]:
                    best_cost[node] = node_cost
                    if node not in stack:
                        stack.append(node)

        if goal not in best_cost:
            return 999999999999

        return best_cost[goal]

    nodes = [str(i+1) for i in range(n)]
    answer = 999999999999
    s = str(s)
    a = str(a)
    b = str(b)

    for i in nodes:
        if i == s:
            continue
        with_cost = find_best_cost(s, i)
        a_cost = find_best_cost(i, a)
        b_cost = find_best_cost(i, b)
        total_cost = with_cost + a_cost + b_cost
        if total_cost < answer:
            answer = total_cost

    return answer



print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1,
               [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6,
               [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
