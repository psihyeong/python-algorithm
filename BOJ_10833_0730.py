# BOJ 10844번 쉬운 계단 수
N = int(input())
# 계단수의 길이는 1보다 크고 100보다 작거나 같음
d = [0] * 101
d[1] = [i for i in range(1,10)]

for stair_num in range(1,N):
    temp = []

for num in d[stair_num]:
        # 맨 뒷자리가 0이나 9일땐, 갱신값이 하나. 아닐땐 둘씩 다음 계단수 값에 추가
        if str(num)[-1] == '0':
            new = str(num)+str(int(str(num)[-1])+1)

        elif str(num)[-1] == '9':
            new = str(num)+str(int(str(num)[-1])-1)
 
        else:
            new = str(num)+str(int(str(num)[-1])+1)
            plus = str(num)+str(int(str(num)[-1])-1)
            temp.append(plus)

        temp.append(new)

    d[stair_num+1] = temp

print(len(d[N]) % 1000000000)

# 바텀업 DP 풀이

N = int(input())
# 일의 자리가 인덱스 번호인 수의 개수
dp = [[0 for _ in range(10)] for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 점화식
for i in range(2, 101):
    
    for last_n in range(10):
        
        # 0이 될 수 있는 건 마지막 자리가 1인 수
        if last_n == 0:
            dp[i][last_n] = dp[i-1][1]
        # 9가 될 수 있는 건 마지막 자리가 8인 수
        elif last_n == 9:
            dp[i][last_n] = dp[i-1][8]
        else:
            dp[i][last_n] = dp[i-1][last_n-1] + dp[i-1][last_n+1]

print(sum(dp[N]) % 1000000000)
