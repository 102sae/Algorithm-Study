def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if(seoul[i]=="Kim"):
            answer = i
            return "김서방은 {0}에 있다".format(answer)

"""
다른 사람 풀이
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

index함수..

"""