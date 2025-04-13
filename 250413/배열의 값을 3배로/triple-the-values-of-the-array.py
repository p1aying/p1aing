matrix=[list(map(int,input().split())) for i in range(3)]

for row in range(3):
    for i in range(3):
        matrix[row][i]*=3
        print(matrix[row][i], end=" ")
    print()