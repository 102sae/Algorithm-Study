def solution(n):
    answer = ""
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    answer = int(answer,3) #n진수 -> 10진수
    
    
    return answer