# BOJ 10158번 개미

w, h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())
p += t
q += t
p_idx = p//w
q_idx = q//h
r_p, r_q = 0, 0

if p_idx % 2:
    r_p = w-(p-(p_idx*w))
else:
    r_p = p-(p_idx*w)

if q_idx % 2:
    r_q = h-(q-(q_idx*h))
else:
    r_q = q-(q_idx*h)

print(r_p,r_q)
