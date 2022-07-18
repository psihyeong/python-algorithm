from collections import deque

def bfs(queue):
    global a
    a = max(queue)   #return을 사용하면 함수가 종료됨으로 변수를 사용
    nextque = deque()
    while queue:
        v = queue.popleft()
        for i in node[v]:
            if visited[i] == 0:
                nextque.append(i)
                visited[i] = 1
    if nextque:
        bfs(nextque)

for tc in range(1,11):
    N, start = map(int,input().split())
    visited = [0]*N
    node = []
    for _ in range(N):
        temp = []
        node.append(temp)

    numberin = list(map(int,input().split()))
    for i in range(0,N,2):
        node[numberin[i]].append(numberin[i+1])
    
    a = 0
    visited[start] = 1
    queue = deque([start])
    bfs(queue)
    print(f"#{tc} {a}")