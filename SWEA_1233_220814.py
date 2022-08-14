# SWEA 1233번 사칙연산 유효성 검사

TC = 10
for tc in range(1,TC+1):
    N = int(input())

    tree = [list(input().split()) for _ in range(N)]
    giho = ['*','/','-','+']
    # 유효성 검사 True
    is_cal = 1

    for node in tree:
        # 자식노드 2개를 가지고 있는 노드 값이 기호가 아닐경우, False
        if len(node) == 4:
            if node[1] not in giho:
                is_cal = 0
                break
        # 자식노드를 1개만 가지고 있는 경우, False
        if len(node) == 3:
            is_cal = 0
        # 단말노드의 값이 기호일 경우, False
        if len(node) == 2:
            if node[1] in giho:
                is_cal = 0
                break

    print(f'#{tc} {is_cal}')
