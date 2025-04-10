n = int(input())
b = []

for i in range(1, n):  # 1부터 n-1까지
    if (i % 2 == 0) or (i % 5 == 0) or (i % 3 == 0):
        b.append(i)
    else:
        continue

print((n - 1) - len(b))  # 실제 검사한 수의 총 개수 - b의 길이