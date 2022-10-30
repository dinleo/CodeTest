def solution(a):
    def rule(s):
        print(s)
        if 'b' not in s:
            return True
        s = s.strip('a')
        if 'a' not in s:
            return False
        print(s)
        n = min(s.find('a'), len(s) - s.rfind('a') - 1)
        if n == s.count('a'):
            return rule(s[n:-n])
        else:
            return False

    answer = []
    for i in a:
        print("================")
        answer.append(rule(i))

    return answer

print(solution(["abab","bbaa","bababa","bbbabababbbaa","bbbbbaabbabbb","abbbaababbbbaa","bb","ab","a","b"]))