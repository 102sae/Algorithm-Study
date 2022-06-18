def solution(s):
    answer = list(s)
    answer = sorted(answer,reverse=True)
    answer = "".join(answer)
    return answer
"""
다른 사람 풀이
def solution(s):
    return "".join(sorted(s,reverse=True))
"""