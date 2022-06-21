def solution(price, money, count):
    while(count!=0):
        money -= count*price
        count -= 1
    if money>0:
        return 0
    return abs(money)

"""
다른 사람 풀이
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
"""