# BOJ 20923번 숫자 할리갈리 게임
import sys
from collections import deque
N, game = map(int,sys.stdin.readline().split())
d_dec = deque()
s_dec = deque()

for i in range(N):
    d,s = map(int,input().split())
    d_dec.append(d)
    s_dec.append(s)


d_num, s_num = 0, 0

d_ground = deque()
s_ground = deque()
for i in range(game):
    # 게임진행, 처음엔 도수턴이니 i가 짝수면 도수가 카드를 냄
    if i % 2 == 0:
        d_num = d_dec.pop()
        d_ground.append(d_num)
    else:
        s_num = s_dec.pop()
        s_ground.append(s_num)
    # 게임진행 도중 카드 수가 0개면 끝
    if len(d_dec) == 0:
        print("su")
        break
    elif len(s_dec) == 0:
        print("do")
        break
    # 수연이가 냈을 때 그라운드가 최초로 다 채워지므로 수연이부터 검사
    if d_num + s_num == 5 and d_num >= 1 and s_num >= 1:
        # 상대방거부터
        if len(d_ground) > 0:
            s_dec.extendleft(d_ground)
            d_num = 0
            d_ground = deque()
        if len(s_ground) > 0:
            s_dec.extendleft(s_ground)
            s_num = 0
            s_ground = deque()
    # 도수 검사
    elif d_num == 5 or s_num == 5:
        # 상대방거부터
        if len(s_ground) > 0:
            d_dec.extendleft(s_ground)
            s_num = 0
            s_ground = deque()
        if len(d_ground) > 0:
            d_dec.extendleft(d_ground)
            d_num = 0
            d_ground = deque()

if len(d_dec) != 0 and len(s_dec) != 0:
    if len(d_dec) > len(s_dec):
        print("do")
    elif len(d_dec) < len(s_dec):
        print("su")
    else:
        print("dosu")
