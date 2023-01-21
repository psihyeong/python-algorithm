# BOJ번 2800번 괄호 제거
def dfs(depth, BeginWith):
    if len(ssang) == depth:
        return
    else:
        for i in range(BeginWith,len(ssang)):
            left_i = ssang[i][0]
            right_i = ssang[i][1]
            sic[left_i] = ''
            sic[right_i] = ''
            result.append(''.join(sic))
            dfs(depth+1,i+1)
            sic[left_i] = '('
            sic[right_i] = ')'


sic = list(input())

ssang = []
stack = []
for i in range(len(sic)):
    if sic[i] == '(':
        stack.append((sic[i],i))
    elif sic[i] == ')':
        ssang.append((stack[-1][1],i))
        stack.pop()

result = []
dfs(0,0)
result = list(set(result))
result.sort()
for i in result:
    print(i)