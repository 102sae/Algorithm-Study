
def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1,arr2):
        a12 = bin(i|j)[2:] #요소끼리 bit or연산 후 0b제외 저장
        a12 = a12.rjust(n,"0")
        a12 = a12.replace("1","#")
        a12 = a12.replace("0"," ")
        answer.append(a12)
         
    return answer

#zip() iterable 자료형이 개수가 동일할 때 사용
#iterable 자료형의 각각의 요소를 나눈후 순서대로 묶어서
#요소 개수만큼 새로운 iterable 자료형 생성(리스트, 튜플같은)

#rjust : 오른쪽 정렬
#"".rjust(5,"0") -> 길이는 5 0으로 채움

