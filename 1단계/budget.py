def solution(d, budget):
    d.sort()
    while sum(d)>budget: #합이 예산보다 작거나 같으면 종료
        d.pop()
        
    return len(d)

"""
다른 사람 풀이
def solution(d, budget):
    d.sort()
    cnt = 0

    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    
    return cnt
    """