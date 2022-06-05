def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = []
    j=0
    for i in participant:
        if i != completion[j]:
            answer.append(i)
        else:
            if len(completion)-1 == j:
                continue
            else: 
                j +=1
        
    return answer[0]


""" 다른 사람 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p 같지 않은 값이 있으면 바로 멈춤
    return participant[-1] for돌고도 미완주자를 못 찾아서 마지막 값이 미완주자
"""

"""
해시이용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
"""
