# SWEA 1952번 수영장

def dfs(tmp):
    if sum(tmp) >= 12:
        one_three.append(tmp[::])
        return
    else:
        for i in [1,3]:
            tmp.append(i)
            dfs(tmp)
            tmp.pop()

def cal(lst):
    month = 0
    result = 0
    for i in lst:
        month += i
        if i == 1:
            result += monthly_or_daily(month)
        else:
            result += ticket_p[2]
        
        if result > res:
            break
    return result

def monthly_or_daily(n):
    if planner[n - 1] * ticket_p[0] > ticket_p[1]:
        return ticket_p[1]
    else:
        return planner[n - 1] * ticket_p[0]

for tc in range(1,int(input())+1):
    ticket_p = list(map(int,input().split()))
    planner = list(map(int,input().split()))
    one_three = []
    tmp = []
    dfs(tmp)
    res = ticket_p[3]

    for case in one_three:
        if cal(case) < res:
            res = cal(case)

    print(f'#{tc} {res}')
