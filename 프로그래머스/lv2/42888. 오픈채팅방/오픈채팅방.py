def solution(record):
    record_lst = []
    for rec in record:
        record_lst.append(list(map(str,rec.split())))
        
    
    nickname_hash = {}
    answer = []
    
    for i in record_lst:
        if len(i) == 3 and i[0] == "Enter":
            answer.append((i[1],"Enter"))
            nickname_hash[i[1]] = i[2]
        elif len(i) == 2 and i[0] == "Leave":
            answer.append((i[1],"Leave"))
        else:
            nickname_hash[i[1]] = i[2]
            
    ans = []
    
    for user_id, status in answer:
        if status == "Enter":
            ans.append(f"{nickname_hash[user_id]}님이 들어왔습니다.")
        else:
            ans.append(f"{nickname_hash[user_id]}님이 나갔습니다.")

    return ans