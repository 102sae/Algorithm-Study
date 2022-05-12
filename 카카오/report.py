def solution(id_list, report, k):
    answer = [0]*len(id_list) # 각 id마다 메일 수 저장
    report_dic = { x:0 for x in id_list}
    # id 값을 key로 갖는 딕셔너리 생성, 신고당한 횟수 저장

    #신고당한 사람 val 값 올리기 
    for r in set(report): #set으로 중복값 제거
        report_dic[r.split()[1]] += 1 #신고한 당한 사람==key의 val +1
    
    for r in set(report):
        #신고 당한 횟수가 정지기준보다 높으면
        if report_dic[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
            #answer == 신고한 사람이 정지 됐을 경우 메일 전송 횟수
            #정지 당한 사람을 신고한 사람의 answer +1
    return answer

# 리스트 생성하기
# list = [val] * 원하는 길이
# 딕셔너리 key를 list 안에 값으로 만들기 
# 딕셔너리  = {x: val for x in list)
# set을 사용하면 중복값 제거
# .index는 리스트 중 특정 원소가 몇번째에 처음 등장하는지 알려줌

