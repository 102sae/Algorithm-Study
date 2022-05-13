def solution(s):
    answer = ''
    numbers = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    eng =''
    for num in s:
        if num.isdigit():
            answer += num
        else :
            eng += num
            if eng in numbers.keys():
                answer += str(numbers[eng])
                eng =''         
    return int(answer)

