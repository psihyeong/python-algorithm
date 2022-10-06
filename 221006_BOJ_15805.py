# BOJ 15805번 트리 나라 관광 가이드

N = int(input())
v = list(map(int,input().split()))
root = v[0]         # 루트 도시 번호
max_node = max(v)   # 도시 중 최댓값
# 최댓값까지 도시가 있기 때문에 최댓값 인덱스만큼 부모 리스트를 생성
parent = [-1 for _ in range(max_node+1)]

for i in range(0,len(v)-1):
    # 뒤에 있는 도시의 부모가 정해지지 않았으면,
    if parent[v[i+1]] == -1:
        # 앞에 있는 도시를 뒤에 있는 도시의 부모로 저장
        parent[v[i+1]] = v[i]

nocity = 0
for i in range(len(parent)):
    # 루트 도시가 아니면서
    if i != root:
        # 부모가 정해지지 않은 도시는
        if parent[i] == -1:
            # 트리 나라의 도시가 아니므로, 개수를 세서
            nocity += 1
            
# 결과값에서 빼준다
result = max_node + 1 - nocity
# 루트 도시는 부모가 없으므로 -1로 변경
parent[root] = -1
# 출력
print(result)
print(*parent)
