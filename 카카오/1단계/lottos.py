def solution(lottos, win_nums):
    answer = []
    rnkH = 7
    rnkL = 7
    
    for lt in lottos:      
        if lt in win_nums:
            rnkL -= 1
            rnkH -= 1

        if lt == 0:
            rnkH -= 1

        
    if rnkL == 7 :
        rnkL -= 1

    if rnkH == 7:
        rnkH -= 1

    answer.append(rnkH)
    answer.append(rnkL)
      
        
    return answer
