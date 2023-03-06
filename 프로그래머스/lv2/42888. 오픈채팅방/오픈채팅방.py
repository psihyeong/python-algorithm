def solution(record):
    name_dict = {}
    log = []
    
    for rec in record:
        i = list(map(str,rec.split()))
        if len(i) == 3 and i[0] == "Enter":
            name_dict[i[1]] = i[2]
            log.append((i[1], "님이 들어왔습니다."))
        elif len(i) == 2 and i[0] == "Leave":
            log.append((i[1], "님이 나갔습니다."))
        else:
            name_dict[i[1]] = i[2]
                          
    answer = []
    for user_id, status in log:
        answer.append(name_dict[user_id]+status)
        
    return answer