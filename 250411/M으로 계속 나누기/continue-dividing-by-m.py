N, M = map(int, input().split())

print(N)
# Please write your code here.
while N != 0:
    N//=M
    if N!=0:
        print(N)
    else:
        break