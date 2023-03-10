def solution(enroll, referral, seller, amount):
    answer = []
    res = {}
    ref = {}
    for i in range(len(enroll)):
        ref[enroll[i]] = referral[i]
        res[enroll[i]] = 0
    
    def distribute(person, money):
        # 분배금 구하기
        m_lst = []
        while True:
            distribution = money // 10
            m_lst.append(money-distribution)
            money = distribution
            if money == 0:
                break
            
        p_lst = []
        p_lst.append(person)
        p = person
        
        while True:
            if ref[p] == "-":
                break
            else:
                p_lst.append(ref[p])
                p = ref[p]
            
            if len(m_lst) == len(p_lst):
                break
                
        for i in range(len(p_lst)):
            res[p_lst[i]] += m_lst[i]
            
            
    for i in range(len(seller)):
        distribute(seller[i], amount[i]*100)
        
    for val in res.values():
        answer.append(val)
        
    return answer