#1181 단어 정렬
N = int(input())
word_list = []
for _ in range(N):
    w = input()
    if w not in word_list: # 중복단어 리스트 추가x = 중복제거
        word_list.append(w)

words = sorted(word_list, key = lambda x : len(x), reverse = False) # 길이가 짧은 것 부터 정렬
longest = len(words[-1])
len_list = []
for i in range(1, 1+longest): #길이별 단어 리스트 생성
    temp = []
    for word in words:
        if len(word) == i:
            temp.append(word)
    if len(temp) >= 1 :
        len_list.append(temp)        
for i in len_list: # 길이별 정렬
    i.sort()

for i in len_list: # 하나씩 출력
    for j in i:
        print(j)
               
-------------------------------------------------------------              
               
#1085 직사각형에서 탈출
x, y, w, h = map(int,input().split())
case = []
case.append(w-x)
case.append(h-y)
case.append(x)
case.append(y)
# 현재위치(x,y)에서 각 변으로 수직으로 이동하는게 최솟값의 경우의 수들
print(min(case))
