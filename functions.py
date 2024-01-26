al = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def show_board(al):
    loop=0
    
    for i in al:
        print(*i, sep = "  | ")
        loop+=1
        if loop<=2:
            print("___|____|___")
        else:
            print("   |    |  ")
    print()

computer_moves = [
    [1, 7, 9],
    [1, 3, 9],
    [1, 3],
    [1, 3, 7],
    [1, 7, 3]
]
winner = []
check_winner ='''[
    [al[0][0], al[0][1], al[0][2]],
    [al[1][0], al[1][1], al[1][2]],
    [al[2][0], al[2][1], al[2][2]],
    [al[0][0], al[1][0], al[2][0]],
    [al[0][1], al[1][1], al[2][1]],
    [al[0][2], al[1][2], al[2][2]],
    [al[0][0], al[1][1], al[2][2]],
    [al[0][2], al[1][1], al[2][0]]
]'''

def check_win(check_winner, winner):
    for i in eval(check_winner):
        if i[0] == i[1] and i[1] == i[2]:
            winner.append(i[0])
    if len(winner) == 1 :
        return True
    else:
        return False

c1mx = 0
c2mx = 0
def excuteinpx(ipx,c1mx, c2mx, al):
    if ipx == 1 or ipx == 2 or ipx == 3:
        c1mx = 0
    if ipx == 4 or ipx == 5 or ipx == 6:
        c1mx = 1
    if ipx == 7 or ipx == 8 or ipx == 9:
        c1mx = 2
    if ipx == 1 or ipx == 4 or ipx == 7:
        c2mx = 0
    if ipx == 2 or ipx == 5 or ipx == 8:
        c2mx = 1
    if ipx == 3 or ipx == 6 or ipx == 9:
        c2mx = 2
    al[c1mx][c2mx] =  "X"
c1mo = 0
c2mo = 0
def excuteinpo(ipo,c1mo, c2mo, al):
    if ipo == 1 or ipo == 2 or ipo == 3:
        c1mo = 0
    if ipo == 4 or ipo == 5 or ipo == 6:
        c1mo = 1
    if ipo == 7 or ipo == 8 or ipo == 9:
        c1mo = 2
    if ipo == 1 or ipo == 4 or ipo == 7:
        c2mo = 0
    if ipo == 2 or ipo == 5 or ipo == 8:
        c2mo = 1
    if ipo == 3 or ipo == 6 or ipo == 9:
        c2mo = 2
    al[c1mo][c2mo] ="O"

def savwhr(check_winner):
    for i in eval(check_winner):
        if i[0] == i[1] and i[0] == "O" and i[2] !=  "X" and i[2] !=  "O":
            return i[2]
        if i[0] == i[2] and i[0] == "O" and i[1] !=  "X" and i[1] !=  "O":
            return i[1]
        if i[2] == i[1] and i[2] == "O" and i[0] != "X" and i[0] != "O":
            return i[0]
def chksav(check_winner):
    for i in eval(check_winner):
        if i[0] == i[1] and i[0] == "O" and i[2] !=  "X" and i[2] != "O":
            return True
        if i[0] == i[2] and i[0] == "O" and i[1] != "X" and i[1] != "O":
            return True
        if i[2] == i[1] and i[2] == "O" and i[0] !=  "X" and i[0] != "O":
            return True
def finwhr(check_winner):
    for i in eval(check_winner):
        if i[0] == i[1] and i[0] == "X" and i[2] != "X" and i[2] !="O":
            return i[2]
        if i[0] == i[2] and i[0] ==  "X" and i[1] !="X" and i[1] != "O":
            return i[1]
        if i[2] == i[1] and i[2] ==  "X" and i[0] !=  "X" and i[0] != "O":
            return i[0]
def chkfin(check_winner):
    for i in eval(check_winner):
        if i[0] == i[1] and i[0] =="X" and i[2] != "X" and i[2] != "O":
            return True
        if i[0] == i[2] and i[0] == "X" and i[1] != "X" and i[1] != "O":
            return True
        if i[2] == i[1] and i[2] == "X" and i[0] !=  "X" and i[0] !=  "O":
            return True
av = []
def avmov(av, al):
    av.clear()
    for i in al:
        for j in i:
            if j !=  "X" and j !='O':
                av.append(j)
