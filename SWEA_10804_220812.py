# SWEA 10804번 문자열의 거울상

TC = int(input())
for tc in range(1,TC+1):
    string = str(input())
    string = string[::-1]
    result = ''
    for i in string:
        if i == 'q':
            result += 'p'
        elif i == 'p':
            result += 'q'
        elif i == 'b':
            result += 'd'
        elif i == 'd':
            result += 'b'

    print(f'#{tc} {result}')
