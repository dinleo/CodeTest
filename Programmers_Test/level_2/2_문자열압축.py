# 너무 중구난방한 코드 추후 복습
def solution(s):
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2
    answer = len(case_n_is_1(s))
    for n in range(2, len(s)):
        new_s = ""
        ss = s
        pattern = ss[:n]
        count = 1
        ss = ss[n:]
        while 1:
            if ss == "":
                if count == 1:
                    new_s += pattern
                    break
                else:
                    new_s += str(count) + pattern
                    break
            if pattern == ss[:n]:
                count += 1
                ss = ss[n:]
            elif count == 1:
                new_s += pattern
                pattern = ss[:n]
                ss = ss[n:]
            else:
                new_s += str(count) + pattern
                pattern = ss[:n]
                ss = ss[n:]
                count = 1

        answer = min(answer, len(new_s))
    return answer


def case_n_is_1(s):
    new_s = ""
    ss = s
    pattern = ss[0]
    ss = ss[1:]
    count = 1
    while 1:
        if ss == "":
            if count == 1:
                new_s += pattern
                break
            else:
                new_s += str(count) + pattern
                break
        if pattern == ss[0]:
            count += 1
            ss = ss[1:]
        elif count == 1:
            new_s += pattern
            pattern = ss[0]
            ss = ss[1:]
        else:
            new_s += str(count) + pattern
            pattern = ss[0]
            ss = ss[1:]
            count = 1
    return new_s


print(solution("aa"), 2)
print(solution("aabbaccc"), 7)
print(solution("ababcdcdababcdcd"), 9)
print(solution("abcabcdede"), 8)
print(solution("abcabcabcabcdededededede"), 14)
print(solution("xababcdcdababcdcd"), 17)
print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"),
      5)

print(solution("acacacbacacac" ),9)
print(solution("acacacacacacbacacacacacac"), 9)
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), 4)
