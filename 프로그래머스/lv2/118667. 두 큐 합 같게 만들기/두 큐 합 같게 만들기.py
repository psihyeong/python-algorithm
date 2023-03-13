from collections import deque

def solution(queue1, queue2):
    answer = 0
    # 큐 자료구조로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    
    
    while True:      
        if q1_sum == q2_sum:
            break
        elif q1_sum > q2_sum:
            tmp = q1.popleft()
            q2.append(tmp)
            q1_sum -= tmp
            q2_sum += tmp
            answer += 1
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            q2_sum -= tmp
            q1_sum += tmp
            answer += 1
        
        if answer >= len(queue1)*4:     # queue의 길이의 4배가 최대 경우의 수
            answer = -1
            break
    
        
    return answer
