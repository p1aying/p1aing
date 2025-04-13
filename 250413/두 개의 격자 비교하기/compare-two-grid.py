row, curm = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(row)]
matrix2 = [list(map(int, input().split())) for _ in range(row)]

# 디버깅용: 입력 확인
assert len(matrix1) == row
assert all(len(r) == curm for r in matrix1)
assert len(matrix2) == row
assert all(len(r) == curm for r in matrix2)

new_matrix = [[0 for _ in range(curm)] for _ in range(row)]

for i in range(row):
    for j in range(curm):
        if matrix1[i][j] == matrix2[i][j]:
            new_matrix[i][j] = 0
        else:
            new_matrix[i][j] = 1

# 출력
for row in new_matrix:
    print(*row)