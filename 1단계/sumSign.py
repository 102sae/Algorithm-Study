def solution(absolutes, signs):
    answer = 0
    real = []
    for i,j in zip(absolutes,signs):
        if j == False:
            real.append( -i)

        else :
            real.append(i)
    answer = sum(real)
    
    return answer