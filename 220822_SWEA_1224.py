# SWEA 1224번 계산기 3

TC = 10
for tc in range(1,TC+1):
    N=int(input())
    tmp = list(input())

    stack = []
    sick = []
    priority = {'(':0, '+':1, '-':1,'*':2, '/':2}
    for i in tmp:
        # 숫자면 식에 push
        if i.isdigit():
            sick.append(int(i))
        # 왼쪽 괄호는 무조건 push
        elif i == '(':
            stack.append(i)
        # 오른쪽 괄호면
        elif i == ')':
            while True:
                tmp = stack.pop()
                # 왼쪽 괄호를 만날때 까지 스택에서 pop, 식에 push
                if tmp != '(':
                    sick.append(tmp)
                else:
                    break
        else:
            # 스택이 비었으면 push
            if len(stack)==0:
                stack.append(i)
            # 스택의 Top보다
            # 우선순위가 높으면, 스택에 push
            elif priority[stack[-1]] < priority[i]:
                stack.append(i)
            # 우선순위가 높지 않으면,
            else:
                # 스택이 빌 때까지
                while len(stack)>0:
                    # 우선순위가 낮지 않으면 스택에서 pop하고 식에 push
                    if priority[stack[-1]] >= priority[i]:
                        sick.append(stack.pop())
                    # 낮은 걸 만나면 break
                    else:
                        break
                # 스택이 비었거나, 우선순위가 낮은 걸 만났을 때, 스택에 push
                stack.append(i)
    # 남은 기호 마지막에 전부 push
    while len(stack)>0:
        sick.append(stack.pop())
    # 계산
    cal = []
    for i in sick:
        if i == '*':
            a = cal.pop()
            b = cal.pop()
            cal.append(b*a)
        elif i == '/':
            a = cal.pop()
            b = cal.pop()
            cal.append(b / a)
        elif i == '-':
            a = cal.pop()
            b = cal.pop()
            cal.append(b - a)
        elif i == '+':
            a = cal.pop()
            b = cal.pop()
            cal.append(b + a)
        else:
            cal.append(i)
    print(f'#{tc} {cal[0]}')
