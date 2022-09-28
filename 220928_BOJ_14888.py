# BOJ 14888번 연산자 끼워넣기

def DFS(depth,val):
    # 다 끼워넣었으면
    if depth == N-1:
        result.append(val)
        return
    else:
        for i in range(4):
            # 사용할 기호가 남아있다면,
            if giho[i] > 0:
                # 전처리
                giho[i] -= 1
                next = depth+1
                # 연산
                if i == 0:
                    new_val = val+nums[next]
                elif i == 1:
                    new_val = val-nums[next]
                elif i == 2:
                    new_val = val * nums[next]
                else:
                    # C++14 나눗셈 기준
                    if val < 0:
                        new_val = -((-val) // nums[next])
                    else:
                        new_val = val // nums[next]
                # 재귀호출
                DFS(next,new_val)
                # 후처리
                giho[i] += 1

N = int(input())
nums = list(map(int,input().split()))
giho = list(map(int,input().split()))
result = []
DFS(0,nums[0])
print(max(result))
print(min(result))
