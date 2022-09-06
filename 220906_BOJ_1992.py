# BOJ 1992번 쿼드트리

def zip(y,x,n):
    # 영상 크기가 1이면 바로 result에 추가
    if n == 1:
        result.append(movie[y][x])
        return
    # 검사할 영상
    check = movie[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            # 같은 영상이 아니면
            if movie[i][j] != check:
                # 4등분하기전에 괄호 열어주고
                result.append('(')
                for ni in range(2):
                    for nj in range(2):
                        zip(y+ni*n//2,x+nj*n//2,n//2)
                # 4등분 끝내고 괄호 닫아주기
                result.append(')')
                # 함수 종료해주면서 result에 추가 못하게 막기
                return
    # 검사통과하면 result에 추가
    result.append(movie[y][x])

N = int(input())
movie = [list(input()) for _ in range(N)]
result = []

zip(0,0,N)
print(''.join(result))
