def solution(rows, columns, queries):
    
    def rotate(y1,x1,y2,x2):
        up_left = graph[y1][x1]
        down_left = graph[y2][x1]
        up_right = graph[y1][x2]
        down_right = graph[y2][x2]

        for i in range(x2,x1,-1):
            graph[y1][i] = graph[y1][i-1]

        for i in range(y1,y2):
            graph[i][x1] = graph[i+1][x1]

        for i in range(x1,x2):
            graph[y2][i] = graph[y2][i+1]

        for i in range(y2,y1,-1):
            graph[i][x2] = graph[i-1][x2]

        graph[y1+1][x2] = up_right
    
        min_res = int(1e9)
        for i in range(y1,y2+1):
            min_res = min(min_res,graph[i][x1],graph[i][x2])
            
        for i in range(x1,x2+1):
            min_res = min(min_res,graph[y1][i],graph[y2][i])
            
        return min_res

    answer = []
    graph = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = ((i)*(columns)+j+1)
    
    for lst in queries:
        res = rotate(lst[0]-1, lst[1]-1, lst[2]-1, lst[3]-1)
        answer.append(res)
        
    return answer

