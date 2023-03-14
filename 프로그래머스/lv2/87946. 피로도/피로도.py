def solution(k, dungeons):
    answer = -1
    
    L = len(dungeons)
    v = [0 for _ in range(L)]
    def dfs(explore_cnt,depth,tired):
        nonlocal answer
    
        for i in range(L):
            if not v[i]:
                if tired >= dungeons[i][0]:
                    tired -= dungeons[i][1]
                    v[i] = 1
                    answer = max(answer,explore_cnt+1)
                    dfs(explore_cnt+1,depth+1,tired)
                    v[i] = 0
                    tired += dungeons[i][1]
            
    dfs(0,0,k)
    
    return answer