# BOJ번 2800번 괄호 제거

# 백트래킹 조합을 활용해 괄호 쌍을 없에는 함수
def dfs(depth, BeginWith):
    # 괄호 쌍을 모두 없앤 경우, 종료조건
    if len(ssang) == depth:
        return
    else:
        for i in range(BeginWith,len(ssang)):
            # 괄호쌍 인덱스 값
            left_i = ssang[i][0]
            right_i = ssang[i][1]
            # 전처리
            sic[left_i] = ''
            sic[right_i] = ''
            # 괄호를 없앤 값 result에 삽입
            result.append(''.join(sic))
            # 괄호를 없앤 수 == depth에 +1, 백트래킹 조합 구현을 위해 i+1
            dfs(depth+1,i+1)
            # 후처리
            sic[left_i] = '('
            sic[right_i] = ')'


sic = list(input())
# 괄호 쌍 인덱스 번호의 튜플을 가지는 리스트
ssang = []
# 스택을 활용
stack = []
for i in range(len(sic)):
    if sic[i] == '(':
        stack.append((sic[i],i))
    elif sic[i] == ')':
        ssang.append((stack[-1][1],i))
        stack.pop()

result = []
dfs(0,0)
# 중복처리
result = list(set(result))
# 사전순으로 정렬
result.sort()
for i in result:
    print(i)
