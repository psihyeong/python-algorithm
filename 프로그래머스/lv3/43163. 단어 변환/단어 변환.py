def solution(begin, target, words):
    answer = 0
    
    word_length = len(begin)            # 단어의 길이
    
    # DFS
    stack = []
    stack.append((begin, 0))
    visited = [0 for i in range(len(words))]       # 최소 과정이기 때문에 이전 단어로 돌아갈 일이 없도록 visited 설정 
    
    while stack:
        now_word, cnt = stack.pop()
        if now_word == target:                     # target이면 return
            return cnt
        else:
            for idx, check_word in enumerate(words):
                if not visited[idx]:               # 변환되지 않았던 단어면
                    # 한 개의 알파벳만 다른지 확인
                    diff_cnt = 0                  
                    for i in range(word_length):
                        if now_word[i] != check_word[i]:
                            diff_cnt += 1
                    # 확인되면 계속 탐색
                    if diff_cnt == 1:
                        visited[idx] = 1
                        stack.append((check_word,cnt+1))      
    
    return answer
    