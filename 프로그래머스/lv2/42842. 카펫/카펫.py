def solution(brown, yellow):
    answer = []
    
    # 노란색 격자가 몇 줄이냐를 완전 탐색하는 문제
    
    for yellow_row in range(1,yellow+1):            # 최소 1줄부터 최대 yellow줄까지
        if yellow % yellow_row == 0:                # 직사각형일 경우
            yellow_col = yellow // yellow_row       # 너비를 구하고
            if yellow_row*2 + yellow_col*2 + 4 == brown:   # 갈색 격자 개수가 일치하면
                answer = [yellow_col+2,yellow_row+2]       # 정답
                break
        
    return answer