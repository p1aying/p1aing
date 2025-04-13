flag=0
for i in range(2):
    if flag==0:
        matrix1=[list(map(int,input().split()))for _ in range(3)]
        flag+=1
    else:
        matrix2=[list(map(int,input().split()))for _ in range(3)]
print(matrix1)
print(matrix2)
for ii in range(3):
    for iii in range(3):
        keke=matrix1[ii][iii]*matrix2[ii][iii]
        print(keke,end=" ")
    print()