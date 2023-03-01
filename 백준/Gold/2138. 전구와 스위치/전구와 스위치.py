# BOJ 2138번 전구와 스위치

def push(n,lst):
    for i in range(n-1,n+2):
        if 0 <= i < N:
            if lst[i]:
                lst[i] = 0
            else:
                lst[i] = 1

N = int(input())
not_push_first = list(map(int,input()))
goal = list(map(int,input()))
push_first = not_push_first[::]
push(0,push_first)

not_res = 0
res = 1

for i in range(1,N):
    if not_push_first[i-1] != goal[i-1]:
        not_res += 1
        push(i,not_push_first)

    if push_first[i-1] != goal[i-1]:
        res += 1
        push(i,push_first)

if not_push_first[-1] == goal[-1] and not_push_first[-2] == goal[-2]:
    print(not_res)
elif push_first[-1] == goal[-1] and push_first[-2] == goal[-2]:
    print(res)
else:
    print(-1)
