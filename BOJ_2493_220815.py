# BOJ 2493번 탑
import sys
input  = sys.stdin.readline

N = int(input())
tops = list(map(int,input().split()))
stack = []
result = []
# 모든 탑에 대해서
for i in range(N):
    # 현재 탑이
    while stack:
        # 스택의 맨 위 탑으로부터 수신 가능할 경우
        if stack[-1][1] >= tops[i]:
            # 수신 가능한 탑의 번호를 result에 삽입
            result.append(stack[-1][0] + 1)
            # 현재 탑의 정보 stack에 삽입
            stack.append([i,tops[i]])
            break
        # 수신 못할 경우 pop
        else:
            stack.pop()

    # 수신 가능한 탑이 아예 없을 경우
    else:
        stack.append([i,tops[i]])
        result.append(0)

print(' '.join(map(str,result)))
