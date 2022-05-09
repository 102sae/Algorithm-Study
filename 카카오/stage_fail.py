#입력 예시
#[2,1,2,6,2,4,3,3]
#출력 예시
#[3,4,2,1,5]
#1,2,3,4,5 반복 
#1실패율 [1/8]
#2실패율 [3/7]
#3실패율 [2/4]
#4실패율 [1/2]
#5실패율 [0/1]

def solution(N,stages):
    answer = {}
    player = len(stages) 
    for i in range(1,N+1):
        if player !=1:
            failer = stages.count(i) 
            answer[i] = failer/player 
            player -= failer 
        else:
            anwer[i] = 0
    answer = sorted(answer,key = answer.get,reverse = True)
    #value 기준 정렬 & key값 출력
    #dict = sorted(dict, key=dict.get)

        
    return answer 