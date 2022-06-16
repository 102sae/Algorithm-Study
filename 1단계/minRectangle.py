def solution(sizes):
    answer = 0
    #모든 명함을 가로가 길도록 배치
    width = []
    height = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            width.append(sizes[i][1])
            height.append(sizes[i][0])
        else :
            width.append(sizes[i][0])
            height.append(sizes[i][1])
    width.sort(reverse = True)   
    height.sort(reverse = True)
    
    answer = width[0]*height[0]
    return answer

    """
    다른 사람 풀이

    
2
3
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

가로 세로 중에 큰거 중에 제일 큰거 * 가로 세로 중에 작은거 중에 제일 큰거
    """