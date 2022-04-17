import random


chromosome = [[0, bin(random.randint(0, 255))[2:].zfill(8)] for _ in range(4)]


# a와 b를 교배해 생성된 str 을 return
def cross(a, b):
    a_pow, a_str = a[0], a[1]
    b_pow, b_str = b[0], b[1]
    # a와 b의 각각의 pow 에 비례해 crossbreeding 에 추가
    crossbreeding = a_str * a_pow + b_str * b_pow
    crossbreeding_len = len(crossbreeding)
    output = ''
    for _ in range(8):
        # 생성된 crossbreeding 에서 랜덤하게 하나씩 8번 추출
        output += crossbreeding[random.randint(0, crossbreeding_len-1)]

    return output


print('           [#], [chromosome]')

for n in range(10):
    for i in range(4):
        chromosome[i][0] = chromosome[i][1].count('1')
    chromosome.sort(reverse=True)

    print(str(n) + '번째 교배: ' + str(chromosome))

    temp = [[0, cross(chromosome[0], chromosome[1])], [0, cross(chromosome[0], chromosome[2])],
            [0, cross(chromosome[0], chromosome[3])], [0, cross(chromosome[1], chromosome[2])]]

    chromosome = temp



