def solution(topping):
    answer = 0
    hash = {}
    
    for i in topping:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
            
    opp_set = set()
    for i in topping:
        hash[i] -= 1
        opp_set.add(i)
        if hash[i] == 0:
            hash.pop(i)
        
        if len(hash) == len(opp_set):
            answer += 1
    
    return answer