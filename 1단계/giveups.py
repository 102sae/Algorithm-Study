def solution(answers):
    answer = []
    p1 = [1,2,3,4,5] #5
    p2 = [2,1,2,3,2,4,2,5] #8
    p3 = [3,3,1,1,2,2,4,4,5,5] #10
    score = [0,0,0]
    
    for i, a in enumerate(answers):
        if a == p1[i%5]:
            score[0]+= 1

        if a ==p2[i%8]:
            score[1]+=1

        if a == p3[i%10]:
            score[2]+=1

    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer

"""
enumerate() -> 결과 튜플
딕셔너리 정렬
sorted(score.items(),key=lambda x:x[1],reverse=True)
elif 로 하면 안되고 다 if 
"""

"""
다른 사람 코드
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
"""
