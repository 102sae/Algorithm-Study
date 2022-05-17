def solution(numbers):
    answer = -1
    inNumber = [0,1,2,3,4,5,6,7,8,9]
    for n in numbers:
        if n in inNumber:
            inNumber.remove(n)
        answer = sum(inNumber)
    return answer

#충격적인 다른 사람 풀이..
def sol(numbers):
    return 45 - sum(numbers)