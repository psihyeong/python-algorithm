# SWEA 3143번 가장 빠른 문자열 타이핑

TC = int(input())
for tc in range(1,TC+1):
    full, part = map(str,input().split())

    result = len(full)
    idx = 0
    result = 0

    while idx < len(full):
        if full[idx] == part[0]:

            if full[idx:idx+len(part)] == part:
                idx += len(part)
                result += 1
            else:
                idx += 1
                result += 1
        else:
            idx += 1
            result += 1

    print(f'#{tc} {result}')
