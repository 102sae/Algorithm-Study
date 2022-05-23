def solution(left, right):
    answer = 0
    numberOfMeasure = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j == 0:
                print(j,'는',i,'의약수')
                numberOfMeasure += 1
            else:
                continue
        if numberOfMeasure%2 == 0:
            answer += i
            print(i,'의 약수는 짝수 더해')
        else :
            answer -= i
        numberOfMeasure = 0
        
    return answer


'''
제곱근이 아닌 수는 약수가 짝수라는 것을 이용한 
다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''
