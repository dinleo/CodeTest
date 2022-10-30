# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])