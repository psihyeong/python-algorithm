# SWEA 1210번 Ladder1
for _ in range(1,11):
    # 왼쪽, 오른쪽, 위
    dx = [-1,1,0]
    dy = [0,0,-1]
    tc = int(input())
    graph1 = []
    for _ in range(100):
        temp = list(map(int,input().split()))
        graph1.append(temp)
        
    start = 0
    # 2인 x좌표 출발점
    for i in range(100):
        if graph1[99][i] == 2:
            start = i
    
    visited = [[0 for i in range(100)] for i in range(100)]
    result = []
    # 아래서부터 위로
    y = 99
    x = start
        
    while True:
        visited[y][x] = 1
            
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if nx >= 0 and ny >= 0 and nx <= 99 and ny <= 99 :     
                if graph1[ny][nx] == 1 and visited[ny][nx] == 0:
                    x = nx
                    y = ny

        if y == 0:
            break
        
    print(f'#{tc} {x}')
