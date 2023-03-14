def solution(k, dungeons):
    answer = -1
    
    L = len(dungeons)
    v = [0 for _ in range(L)]       # 던전의 방문여부를 담는 배열
    
    # 완전탐색을 위한 dfs
    def dfs(explore_cnt,depth,tired):
        nonlocal answer             # 비전역변수 answer와 바인딩하기 위한 nonlocal 키워드
        answer = max(answer,explore_cnt)  # 최댓값 갱신
        
        for i in range(L):
            if not v[i]:
                if tired >= dungeons[i][0]:     # 던전을 방문할 수 있으면,
                    # 전처리
                    tired -= dungeons[i][1]
                    v[i] = 1
                    dfs(explore_cnt+1,depth+1,tired)    # 방문처리 후 탐색
                    # 후처리
                    v[i] = 0
                    tired += dungeons[i][1]
            
    dfs(0,0,k)
    
    return answer