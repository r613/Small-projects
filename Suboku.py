import time
start = time.time()
def find(matrix):
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0:
                for i in range(1,10):
                    if fits(matrix,row,column,i):
                        temp = [x[:]for x in matrix]
                        temp[row][column] = i
                        res = find(temp)
                        if res:
                            return res
                return False
    for i in matrix:
        print i
def fits(matrix,row,column,a):
    if fits_r(matrix,row,a) and fits_c(matrix,column,a) and fits_b(matrix,row,column,a):
        return True
    return False
def fits_r(matrix,row,a):
    for i in matrix[row]:
        if i == a:
            return False
    return True
def fits_c(matrix,column,a):
    for arow in matrix:
        if arow[column] == a:
            return False
    return True
def fits_b(matrix,row,column,a):
    row_b = (row/3)*3
    col_b = (column/3)*3
    for row_n in range(row_b,row_b+3):
        for col_n in range(col_b,col_b+3):
            if matrix[row_n][col_n] == a:
                return False
    return True
#sample
matrix = [[6,0,0,0,0,0,0,4,0],[0,1,7,4,0,0,0,0,3],[0,4,0,0,0,0,1,0,0],[2,5,6,0,0,9,0,0,0],[0,0,0,1,0,5,0,0,0],[0,0,0,3,0,0,8,5,6],[0,0,4,0,0,0,0,8,0],[3,0,0,0,0,2,5,9,0],[0,6,0,0,0,0,0,0,7,]]
find(matrix)
print time.time()-start