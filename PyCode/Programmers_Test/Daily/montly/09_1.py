def solution(numbers):
    numbers = list({1,2,3,4,5,6,7,8,9} - set(numbers))
    return sum(numbers)

print(solution([1,2,3,4,6,7,8,0]))
