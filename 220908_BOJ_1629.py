# BOJ 1629번 곱셈
def recursive(a, b):
    if b == 1:
        return a % C
    temp = recursive(a, b//2)

    if b % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * a % C


A, B, C = map(int, input().split())
print(recursive(A, B))
