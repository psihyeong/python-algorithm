# BOJ 2630번 색종이 만들기

def cut(y,x,n):
    # 종이 크기가 1이면 바로 result에 추가
    if n == 1:
        result[paper[y][x]] += 1
        return
    # 검사할 색
    check = paper[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            # 같은 색이 아니면
            if paper[i][j] != check:
                # 4등분
                for ni in range(2):
                    for nj in range(2):
                        cut(y+ni*n//2,x+nj*n//2,n//2)
                # 함수 종료해주면서 result에 추가 못하게 막기
                return
    # 검사통과하면 result에 추가
    result[check] += 1

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
result = [0,0]

cut(0,0,N)
for i in result:
    print(i)
