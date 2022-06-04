# https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3
import collections


def solution(n, s, a, b, fares):
    s = str(s)
    a = str(a)
    b = str(b)
    graph = collections.defaultdict(dict)
    for i in fares:
        graph[str(i[0])][str(i[1])] = i[2]
        graph[str(i[1])][str(i[0])] = i[2]

    def find_best_path_and_cost(path, goal):
        start = path[-1]
        if start == goal:
            return path, 0
        path_stack = collections.defaultdict(dict)
        best_cost_to_node = collections.defaultdict(int)
        best_path = ''
        path_stack[path] = 0

        while path_stack:
            cur = path_stack.popitem()
            cur_path = cur[0]
            cur_cost = cur[1]
            cur_node = cur_path[-1]
            if cur_node == goal:
                best_path = cur_path
                continue
            for next_node in graph[cur_node]:
                if next_node not in path:
                    next_cost = cur_cost + graph[cur_node][next_node]
                    if next_node not in best_cost_to_node:
                        best_cost_to_node[next_node] = next_cost
                        path_stack[cur_path + next_node] = next_cost
                    elif next_cost < best_cost_to_node[next_node]:
                        best_cost_to_node[next_node] = next_cost
                        path_stack[cur_path + next_node] = next_cost

        if goal not in best_cost_to_node:
            return '', 999999999999999999
        return best_path, best_cost_to_node[goal]

    stack = [s]
    visited = [s]
    best_cost = 999999999999999999

    while stack:
        node = stack.pop(0)
        path, cost = find_best_path_and_cost(s, node)
        _, cost_a = find_best_path_and_cost(path, a)
        _, cost_b = find_best_path_and_cost(path, b)
        cost_sum = cost + cost_a + cost_b
        if cost_sum < best_cost:
            best_cost = cost_sum
        for next_n in graph[node]:
            if (next_n not in visited) and (next_n not in stack):
                stack.append(next_n)
        visited.append(node)

    return best_cost


# print(solution(6, 4, 6, 2,
#                [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
#                 [1, 6, 25]]))
# print(solution(7, 3, 4, 1,
#                [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6,
               [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))