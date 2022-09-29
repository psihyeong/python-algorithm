# BOJ 14889번 스타트와 링크
def dfs(depth,beginwith,start_lst):
    # 스타트 팀을 다 짰다면
    if depth == N//2:
      # 링크 팀을 구하고
        tmp = team[::]
        for i in start_lst:
            tmp.remove(i)
        # 능력치의 차이를 result에 삽입
        result.append(abs(point(start_lst)-point(tmp)))
    else:
        for i in range(beginwith+1,N+1):
            start_lst.append(i)
            dfs(depth+1,i,start_lst)
            start_lst.pop()
            
# 팀의 능력치를 반환하는 함수
def point(lst):
    res = 0
    for i in lst:
        for j in lst:
            res += info[i-1][j-1]
    return res

N = int(input())
info = [list(map(int,input().split())) for _ in range(N)]
# 팀원 번호 리스트
team = []
for i in range(1,N+1):
    team.append(i)
    
start = []
result = []
dfs(0,0,start)
# 최소 능력치 차이 출력
print(min(result))
