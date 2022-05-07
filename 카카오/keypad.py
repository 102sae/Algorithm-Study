def getDistance(current_posL,current_posR,next_pos):
    distanceR = abs(current_posR[0]-next_pos[0]) + abs(current_posR[1]-next_pos[1])
    distanceL = abs(current_posL[0]-next_pos[0]) + abs(current_posL[1]-next_pos[1])
    
    if distanceR > distanceL:
        return 'L'
    elif distanceL > distanceR:
        return 'R'
    else:
        return 'same'
    
def solution(numbers, hand):
    answer = ''
    keypad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    posR = [3,2]
    posL = [3,0]
    
    for num in numbers:
        if num in [1, 4, 7]:
            posL = keypad[num]
            answer+='L'
        elif num in [3, 6, 9]:
            posR = keypad[num]
            answer+="R"
        else:
            result = getDistance(posL,posR,keypad[num])
            if(result=='same'): 
                print(result)
                if(hand == 'right'): 
                    answer += 'R'
                    posR = keypad[num]
                else :
                    answer += 'L'
                    posL = keypad[num]
            elif result == 'R':
                answer += result
                posR = keypad[num]
            else:
                answer += result
                posL = keypad[num]
                
    return answer

