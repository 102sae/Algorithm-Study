def solution(board, moves):
    answer = 0
    stk = []
    for m in moves:
        doll = 0 #뽑는 인형 번호

        for b in range(len(board)):
            if board[b][m-1] != 0:
                #인형이 있을 경우
                doll = board[b][m-1]
                board[b][m-1] = 0
                break
            
        if doll == 0 :
            continue
        
        if stk and stk[-1]==doll :
            stk.pop()
            print(doll)
            answer += 2
        else :
            stk.append(doll)
                
    return answer

