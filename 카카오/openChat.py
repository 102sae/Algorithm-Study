def solution(record):
    answer = []
    user_info = {}
    
    for i in record:
        re =i.split()
        if len(re)==3:
            user_info[re[1]] = re[2]
    
    for i in record:
        re =i.split()
        if re[0] == "Enter":
            answer.append(user_info[re[1]] +"님이 들어왔습니다.")
        elif re[0]=="Leave":
            answer.append(user_info[re[1]]+"님이 나갔습니다.")

    
    return answer