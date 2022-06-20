def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        if s.isdigit() == False:
            answer = False
    else:
        answer = False
    return answer

"""
다른 사람 풀이
def soluion(s):
    return s.isdigit() and len(s) in (4,6)
"""