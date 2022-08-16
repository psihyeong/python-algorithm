# SWEA 1216번 회문2

TC = 10
for _ in range(1, TC + 1):
    tc = int(input())
    moon = [list(map(str, input())) for _ in range(100)]
    max_val = 0

    for long in range(100, 0, -1):
        for row_n in range(100):
            for start in range(100 - long + 1):
                check = moon[row_n][start:start + long]
                if check == check[::-1]:
                    if long > max_val:
                        max_val = long
                        break

    for i in range(100):
        for j in range(100):
            if i > j:
                moon[i][j], moon[j][i] = moon[j][i], moon[i][j]

    for long in range(100, 0, -1):
        for row_n in range(100):
            for start in range(100 - long + 1):
                check = moon[row_n][start:start + long]
                if check == check[::-1]:
                    if long > max_val:
                        max_val = long
                        break

    print(f"#{tc} {max_val}")
