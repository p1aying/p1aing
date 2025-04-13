matrix=[list(map(int,input().split())) for _ in range(4)]

total=0
for row in matrix:
    for eli in row:
        total+=eli
    print(total)
    total=0