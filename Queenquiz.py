brd = []

for a in range(8):
    minibrd  = []
    for b in range(8):
        minibrd.append(False)
    brd.append(minibrd)
for i in brd:
    print i
def find(brd):
    for row in range(8):
        for column in range(8):
            if fits(brd,row,column):
                
                temp_brd = [x[:]for x in brd]
                temp_brd[row][column] = True
                res = find(temp_brd)
                if res:
                    return res
        if empty_row(brd,row):
            
            return False
        else:
            
            pass
    print "\n"
    Print(brd)
    return False
def fits(brd,row,column):
    if empty_row(brd,row) and empty_column(brd,column) and empty_side(brd,row,column):
        return True
    else:
        return False
def empty_row(brd,row):
    for i in brd[row]:
        if i:
            return False
    return True
def empty_column(brd,column):
    for unit in brd:
        if unit[column]:
            return False
    return True
def empty_side(brd,row,column):
    trow = row
    tcolumn = column
    while trow<8 and tcolumn<8:
        if brd[trow][tcolumn]:
            return False
        trow += 1
        tcolumn += 1
    trow = row
    tcolumn = column
    while trow >= 0 and tcolumn< 8:
        if brd[trow][tcolumn]:
            return False
        trow += -1
        tcolumn += 1
    trow = row 
    tcolumn = column 
    while trow <8 and tcolumn >=0:
        if brd[trow][tcolumn]:
            return False
        trow += 1
        tcolumn += -1
    trow = row 
    tcolumn = column 
    while trow >=0 and tcolumn >=0:
        if brd[trow][tcolumn]:
            return False
        trow += -1
        tcolumn += -1
    return True
def Print(brd):
    text = "\n"
    for row in brd:
        line = "\n"
        for space in row:
            line += " "
            if space:
                line += "X"
            else: 
                line += "+"
        text += line
    print text
find(brd)