#the queen challenge
matrix = []
for i in range(8):
    matrix.append([])
    for c in range(8):
        matrix[i].append(0)
def up(matrix,row,column):
    for c in range(8):
        if matrix[c][column] == 1:
            return False
    for c in range(8):
        if matrix[row][c] ==1:
            return False
    return True

def ur(matrix,row,column):
    r = row
    c = column
    while r>0 and c >0: #left up
        r += -1
        c += -1
        if matrix[r][c] == 1:
            return False
    r = row
    c = column
    while r > 0 and c < 7: #up right
        r += -1
        c += 1
        if matrix[r][c] == 1:
            return False
    c = column
    r = column
    while c < 7 and r < 7:#right down
        c += 1
        r += 1
        if matrix[r][c] == 1:
            return False
    c = column
    r = row
    while c > 0 and r < 7:#down left 
        r += 1
        c += -1
        if matrix[r][c] == 1:
            return False
    return True

def find(matrix):
    for row in range(8):
        if 1 not  in matrix[row]:
            for column in range(8):
                if ur(matrix,row,column) and up(matrix,row,column):
                    temp = [x[:] for x in matrix]
                    temp[row][column] = 1
                    find(temp)
                    
            return False
        else:
            pass
    for i in matrix:
        print (i)
    print()
find(matrix)
