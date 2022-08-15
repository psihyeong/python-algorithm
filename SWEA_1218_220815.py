# SWEA 1218번 괄호 짝짓기

TC = 10
for tc in range(1,TC+1):
    N = int(input())
    arr = list(map(str,input()))
    is_giho = ['<>', '{}', '[]', '()']
    is_right = ['>', '}', ']', ')']
    is_left = ['<', '{', '[', '(']

    stack = []
    result = 1
    for giho in arr:
        # 왼쪽 괄호면 stack에 넣어줌
        if giho in is_left:
            stack.append(giho)
        # 오른쪽 괄호가 등장 했을 때
        if giho in is_right:
            # stack의 마지막 왼쪽 괄호를 꺼내서
            left = stack.pop()
            # 짝이 아니면 유효하지 않은 문자열
            if left+giho not in is_giho:
                result = 0
                break

    print(f'#{tc} {result}')
