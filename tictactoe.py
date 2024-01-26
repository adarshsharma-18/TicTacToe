print("\t \t Tic-Tac-Toe Game Designed By Adarsh sharma and shriyash")

print('\n','\n')

import time as t
import os
#import mysql.connector
from functions import *
from datetime import datetime as dt

time= dt.now()

dt=time.replace(microsecond = 0)
print()
print(dt)
print()

'''
#mysql connection
try:
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ad12ad12",database="tic_tac_toe")
myc=mydb.cursor()

 if mydb.is_connected():
        print('successfully connection made with sql')
        print('===================================================================')
except:
    print('connection.........ERROR')

    '''
while True:
    print('===================================================================')
    print("1.single")
    print("2.multiplayer")
    print('3.HISTORY')
    print('4.EXIT')
    choice=int(input('enter your choice:'))
    print('====================================================================')
    if choice==1:
    # the master piece

        name=input("enter player name :")
        player1='computer'
        player2=name
        show_board(al)
        cm = 0
        x_moves = 0

        s=[]
        
        moves = 0
        cdd = 3
        while True:
            if chkfin(check_winner):
                ipx = finwhr(check_winner)
            elif chksav(check_winner):
                ipx = savwhr(check_winner)
            elif x_moves < cdd:
                ipx = computer_moves[cm][x_moves]
            else:
                ipx = av[0]
            print("Computer's turn...... ")
            print()
            print()
            t.sleep(1)
            excuteinpx(ipx, c1mx, c2mx, al)
            
            x_moves += 1

            s.append(ipx)
            
            
            moves += 1
            avmov(av, al)
            show_board(al)
            if check_win(check_winner, winner):
                break
            if moves == 9:
                break


            #User
            while True:
                print(name,"'s turn....")
                t.sleep(1)
                ipo = int(input("Enter the position for O: "))
                if ipo in s:
                    print("please enter valid position.....")
                    print('\n')
                    continue
                else:
                    break
            
                
            excuteinpo(ipo, c1mo, c2mo, al)
            s.append(ipo)
            while x_moves == 1:
                if ipo == 2 or ipo == 3:
                    cm = 0
                    break
                if ipo == 4 or ipo == 7:
                    cm = 1
                    break
                if ipo == 5:
                    cm = 2
                    cdd = 2
                    break
                if ipo == 6 or ipo == 9:
                    cm = 3
                    break
                if ipo == 8:
                    cm = 4
                    break
            moves += 1
            avmov(av, al)
            if check_win(check_winner, winner):
                break
            show_board(al)

        if len(winner) == 1 and winner[0] =="X":
            print( "Computer WON!")
            result= 'P1 WINS'
            break
        elif len(winner) == 1 and winner[0] !="X":
            print( "You WON!")
            result= 'P2 WINS'
            break
        else:
            print( "D" + "R"+  "A" + "W")
            result='DRAW'
        
    # query="insert into history_XO (player1,player2,result,played_time) values ('{}','{}','{}','{}')".format(player1,player2,result,dt)
       # myc.execute(query)
        #mydb.commit()
        
    #multiplayer 

    if choice==2:
        
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
        player = 1    
        
        ########win Flags##########    
        Win = 1    
        Draw = -1    
        Running = 0    
        Stop = 1    
        ###########################    
        Game = Running    
        Mark = 'X'    
        result=''

        
        #This Function Draws Game Board    
        def DrawBoard():    
            print(" %c | %c | %c " % (board[1],board[2],board[3]))    
            print("___|___|___")    
            print(" %c | %c | %c " % (board[4],board[5],board[6]))    
            print("___|___|___")    
            print(" %c | %c | %c " % (board[7],board[8],board[9]))    
            print("   |   |   ")    
        
        #This Function Checks position is empty or not    
        def CheckPosition(x):    
            if(board[x] == ' '):    
                return True    
            else:    
                return False    
        
        #This Function Checks player has won or not    
        def CheckWin():    
            global Game    
            #Horizontal winning condition    
            if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
                Game = Win    
            elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
                Game = Win    
            elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
                Game = Win    
            #Vertical Winning Condition    
            elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
                Game = Win    
            elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
                Game = Win    
            elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
                Game=Win    
            #Diagonal Winning Condition    
            elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
                Game = Win    
            elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
                Game=Win    
            #Match Tie or Draw Condition    
            elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
                Game=Draw    
            else:            
                Game=Running


        

        player1=input("enter player name [X]:")
        player2=input("enter player name [O]:")
        print(player1,"[X]---" ,player2 ,"[O]\n")    
        print()    
        print()    
        print("Please Wait...")    
        t.sleep(1)    
        while(Game == Running):    
            #os.system('cls')   #to open a procesing unit
            
            DrawBoard()    
            if(player % 2 != 0):    
                print(player1,"'s chance")    
                Mark = 'X'    
            else:    
                print(player2,"'s chance")    
                Mark = 'O'    
            choice = int(input("Enter the position between [1-9] where you want to mark : "))    
            
            if choice not in range(1,10):
                print('please enter positions between [1-9]')
                player+=2
                continue
            elif(CheckPosition(choice)):    
                board[choice] = Mark    
                player+=1    
                CheckWin()
            
        #os.system('cls')    
        DrawBoard()    
        if(Game==Draw):    
            print("Game Draw")    
        elif(Game==Win):    
            player-=1    
            if(player%2!=0):    
                print(player1," Won")    
            else:    
                print(player2," Won")


        def winner ():
            global result
            if (Game==Draw):
                result= 'DRAW'
                return('Draw')
            elif(player%2!=0):
                result= 'P1 WINS'
                return (player1)    
            else:
                result= 'P2 WINS'
                return(player2)
        wnn=winner()
    # query="insert into history_XO (player1,player2,result,played_time) values ('{}','{}','{}','{}')".format(player1,player2,result,dt)
       # myc.execute(query)
       # mydb.commit()

    '''  
    if choice==4:
            #break

    if choice==3:
            #HISTORY
            
            try:
                Q2='select * from history_xo'
                myc.execute(Q2)
                records=myc.fetchall()
                for i in records:
                    print('player 1 [P1]=',i[0],end='      ')
                    print('player 2 [P2]=',i[1],end='      ')
                    print('result=', i[2],end='      ')
                    print('time=',i[3])
                mydb.commit()
            except:
        print()
        

'''
            
print("done.....")
