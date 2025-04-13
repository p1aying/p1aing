flag=0

matrix1=[list(map(int,input().split()))for _ in range(3)]
matrix2=[list(map(int,input().split()))for _ in range(4)]
matrix2.pop(0)
#print(matrix1)
#print(matrix2)

for ii in range(3):
    for iii in range(3):
        keke=matrix1[ii][iii]*matrix2[ii][iii]
        print(keke,end=" ")
    print()