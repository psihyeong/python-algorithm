def solution(numbers, target):
    
    answer = 0
    N = len(numbers)
    
    def dfs(depth,num):
        nonlocal answer
        if depth == N:
            if num == target:
                answer += 1
            return
        else:
            dfs(depth+1, num+numbers[depth])
            dfs(depth+1, num-numbers[depth])
            
    dfs(1,-numbers[0])
    dfs(1,numbers[0])
    
    return answer