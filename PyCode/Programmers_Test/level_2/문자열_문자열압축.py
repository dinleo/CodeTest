# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
def solution(s):
    answer = len(s)
    for n in range(1,int(len(s)/2) + 1) :

        a = [s[i:i+n] for i in range(0,len(s),n)]
        new_s = ""
        pattern = a[0]
        count = 1
        for i in range(1,len(a)):
            if a[i] != pattern:
                if count == 1:
                    new_s += pattern
                    pattern = a[i]
                else:
                    new_s += str(count) + pattern
                    pattern = a[i]
                    count = 1
            else:
                count += 1
        if count == 1:
            new_s += pattern
        else:
            new_s += str(count) + pattern

        #print(n,new_s)
        answer = min(answer,len(new_s))

    return answer





#print(solution("aa"), 2)
print(solution("aabbaccc"), 7)
print(solution("ababcdcdababcdcd"), 9)
print(solution("abcabcdede"), 8)
print(solution("abcabcabcabcdededededede"), 14)
print(solution("xababcdcdababcdcd"), 17)
print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"),5)
print(solution("acacacbacacac" ),9)
print(solution("acacacacacacbacacacacacac"), 9)
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), 4)
