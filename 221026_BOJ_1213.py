# BOJ 1213번 팰린드롬 만들기

arr = list(input())
# 사전순 출력을 위해 내림차순 정렬
arr.sort()
# 알파벳을 key, 개수를 value로 갖는 딕셔너리
dp = {}
for i in arr:
    if i in dp:
        dp[i] += 1
    else:
        dp[i] = 1

front = ''
mid = ''
odd = 0
for key, value in dp.items():
    # key의 절반의 개수를 front에 더하기
    front += key * (value // 2)
    # 만약 알파벳의 개수가 홀수이면,
    if value % 2:
        # 홀수 개수 카운트
        odd += 1
        # 중앙값 저장
        mid = key

# 개수가 홀수인 알파벳이 두 개 이상이면 팰린드롬이 될 수 없는 경우
if odd >= 2:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 만들기
    result = front + mid + front[::-1]
    print(result)