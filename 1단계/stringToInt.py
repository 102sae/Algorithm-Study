def solution(s):
    answer = 0
    if (s[0]=="-"):
        answer = -int(s[1:])
    elif (s[0]=="+"):
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer

    """
    부호 인식 안될줄 알았는데 되는거 알고 다시 품
def solution(s):
    answer = int(s)
    return answer

파이썬 짱이다
    """