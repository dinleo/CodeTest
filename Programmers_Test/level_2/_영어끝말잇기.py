# https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3

def solution(n, words):
    answer = []
    used_words = [words[0]]
    for i in range(1,len(words)):
        if words[i] in used_words or words[i-1][-1] != words[i][0]:
            return [(i%n)+1,(i)//n+1]
        used_words.append(words[i])

    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))