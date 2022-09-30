# BOJ 1759번 암호 만들기

# 암호의 조합을 만드는 dfs
def dfs(depth,startwith,val):
    if depth == N:
        if cnt_mo_and_ja(val):
            print(val)
        return
    for i in range(startwith,M):
        new_val = val + alpha[i]
        dfs(depth+1,i+1,new_val)

def cnt_mo_and_ja(str):
    mo, ja = 0, 0
    # 암호의 자음과 모음의 개수를 구해서
    for al in str:
        if al in ['a','e','i','o','u']:
            mo += 1
        else:
            ja += 1
    # 조건을 만족하면
    if mo >= 1 and ja >= 2:
        return True

N, M = map(int,input().split())
# 알파벳 사전순 정렬
alpha = sorted(list(map(str,input().split())))
password = []
dfs(0,0,'')
