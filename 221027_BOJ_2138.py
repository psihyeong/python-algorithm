# BOJ 2138번 전구와 스위치
# 그리디

# n번 인덱스 스위치를 눌렀을 때 전구를 상태를 변화시키는 함수
def push(n,lst):
    for i in range(n-1,n+2):
        if 0 <= i < N:
            if lst[i]:
                lst[i] = 0
            else:
                lst[i] = 1

N = int(input())
# 0번 스위치는 누를지 말지 여부를 알 수 없으므로
# 두 경우를 모두 탐색을 해줘야함

# 0번 스위치를 누르지 않은 현재 전구 상태
not_push_first = list(map(int,input()))
# 0번 스위치를 누른 현재 전구 상태
push_first = not_push_first[::]
push(0,push_first)

# 목표 전구 상태
goal = list(map(int,input()))

# 스위치를 누른 횟수
not_cnt = 0
cnt = 1

# 1번 전구부터 확인
# i-1의 전구를 목표 전구 상태와 맞출 수 있는 건
# i번 전구 스위치에 달려있음
for i in range(1,N):
    # i-1의 전구 상태를 확인
    if not_push_first[i-1] != goal[i-1]:
        # 목표 상태와 다르면 스위치 누르기
        push(i,not_push_first)
        # 누른 횟수 갱신
        not_cnt += 1

    # 0번 스위치를 누른 전구도 똑같이 진행
    if push_first[i-1] != goal[i-1]:
        push(i, push_first)
        cnt += 1

# 마지막에 스위치에 따라 변하는 전구는 -1, -2번 전구이므로,
# 두 전구만 목표 전구와 확인해주면 목표 상태를 만들었는지 확인할 수 있음
if not_push_first[-1] == goal[-1] and not_push_first[-2] == goal[-2]:
    print(not_cnt)
elif push_first[-1] == goal[-1] and push_first[-2] == goal[-2]:
    print(cnt)
else:
    print(-1)
