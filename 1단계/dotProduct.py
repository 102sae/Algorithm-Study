def solution(a, b):
    answer = 0
    for i, j in zip(a,b):
        answer += i*j
    return answer

"""
다른 사람 풀이
solution = lambda x, y: sum(a*b for a, b in zip(x, y))
"""