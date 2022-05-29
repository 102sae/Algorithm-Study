def solution(array, commands):
    answer = []
    sliced = []
    for i,j,k in commands:
        sliced = array[i-1:j]
        sliced.sort()
        answer.append(sliced[k-1]) 
    return answer

"""
다른 사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

"""
