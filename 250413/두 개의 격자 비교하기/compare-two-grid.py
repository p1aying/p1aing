row,curm=map(int,input().split())

matrix1=[list(map(int,input().split()))for _ in range(row)]
matrix2=[list(map(int,input().split()))for _ in range(row)]
#print(matrix1)
#print(matrix2)
new_matrix=[[0,0,0,0] for _ in range(row)]
for i in range(row):
    for ii in range(curm):
        if matrix1[i][ii]==matrix2[i][ii]:
            new_matrix[i][ii]=0
        else:
            new_matrix[i][ii]=1

for iii in range(row):
    for j in range(curm):
        print(new_matrix[iii][j], end=" ")
    print()