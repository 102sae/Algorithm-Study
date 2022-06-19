from itertools import combinations  

def isPrime(n):
    if n == 0 or n ==1 :
        return False
    else:
        for i in range(2,(n//2)+1):
            if n%i == 0 :
                return False
    return True
            
def solution(nums):
    answer = 0
    list_of_nums = list(combinations(nums,3))
    for li in list_of_nums:
        if isPrime(sum(li)):
            answer += 1
    return answer