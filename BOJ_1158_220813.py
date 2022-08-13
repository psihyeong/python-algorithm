# BOJ 1158번 요세푸스 문제

from collections import deque
N, K = map(int,input().split())

que = deque()
# 1부터 N까지 삽입된 큐
for i in range(1,N+1):
    que.append(i)

result = []

# 큐가 빌 때까지
while que:
    # K-1번째 사람까지 빼서 맨 뒤로 보내고
    for _ in range(K-1):
        tmp = que.popleft()
        que.append(tmp)
    # K번째 사람은 빼서 결과 리스트에 삽입
    kth_num = que.popleft()
    result.append(kth_num)

print('<',end='')
for i in range(N-1):
    print(f'{result[i]}, ',end='')
print(f'{result[N-1]}>')
