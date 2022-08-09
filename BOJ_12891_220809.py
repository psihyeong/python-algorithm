# BOJ 12891번 DNA 비밀번호

total_len, part_len = map(int,input().split())
munza = list(map(str,input()))
ACGT = list(map(int,input().split()))
# check[i] 는 i번째 문자열까지 문자들의 개수 리스트
check = [[0,0,0,0]]
tmp = [0 for _ in range(4)]

for i in range(total_len):
    if munza[i] == 'A':
        tmp[0] += 1
    elif munza[i] == 'C':
        tmp[1] += 1
    elif munza[i] == 'G':
        tmp[2] += 1
    elif munza[i] == 'T':
        tmp[3] += 1

    check.append(tmp[::])

result = 0

for i in range(part_len,total_len+1):
    # 모든 부분문자열
    tmp_lst = [x-y for x, y in zip(check[i], check[i-part_len])]
    result_check = 1

    for j in range(4):
        # A, C, G, T 조건에서
        if tmp_lst[j] < ACGT[j] :
            # 한 문자라도 조건을 틀리면 바로 다음 문자열로
            result_check = 0
            break
    # 조건을 모두 통과했다면 +1
    if result_check:
        result += 1

print(result)
