def solution(nums):
    answer = 0
    n = set(nums)
    if len(nums)/2 < len(n):
        answer = len(nums)/2
    else:
        answer = len(n)
    return answer

"""
다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
"""