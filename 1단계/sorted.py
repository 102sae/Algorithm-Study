def solution(strings, n):
    sorted = []
    for i in strings:
        sorted.append(i[n]+i)
    sorted.sort()
    answer = []
    
    for i in sorted:
        answer.append(i[1:])

    return answer

    """
    다른 사람 풀이
    def solution(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요''' 
        sorted(sorted(strings), key=lambda x:x[n])
    """