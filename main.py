import random
row1=None
column1=None
row2 = None
column2 = None
print("TIC-TAC-TOE")
tic=input("choose 'O' or 'X'")
if tic=='O':
    tac='X'
else:
    tac='O'
block=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
i=0
print("Enter the row and column ")
row1=int(input("Row"))
column1=int(input("Column"))
block[row1-1][column1-1]=tic
print(block[0][0],"|",block[0][1],"|",block[0][2])
print(block[1][0],"|",block[1][1],"|",block[1][2])
print(block[2][0],"|",block[2][1],"|",block[2][2])
index1=0
index2=0
while True:
    i+=1
    if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
        if block[0][0]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
        if block[1][0]==tic:
            print("You Win!!")
        else:
            print('you Lose!!')
        break
    elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
        if block[2][0]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
        if block[0][0]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
        if block[0][1]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
        if block[0][2]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
        if block[0][0]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
        if block[0][2]==tic:
            print("You Win!!")
        else:
            print("You Lose!!")
        break
    elif i%2!=0:
        print("computer")
        if row2!=None and column2!=None:
            row2=random.randint(1,3)
            while block[row2-1][0]!=' ' and block[row2-1][1]!=' ' and block[row2-1][2]!=' ':
                row2=random.randint(1,3)
            column2=random.randint(1,3)
            while block[row2-1][column2-1]!=' ':
                column2=random.randint(1,3)
        else:
            row2=random.randint(1,3)
            column2=random.randint(1,3)
            while block[row2-1][column2-1]!=' ':
                column2=random.randint(1,3)
        block[row2-1][column2-1]=tac
        print(block[0][0],"|",block[0][1],"|",block[0][2])
        print(block[1][0],"|",block[1][1],"|",block[1][2])
        print(block[2][0],"|",block[2][1],"|",block[2][2])
    elif i%2==0:
        print('Your Turn')
        row1=int(input("Row"))
        column1=int(input("Column"))
        block[row1-1][column1-1]=tic
        print(block[0][0],"|",block[0][1],"|",block[0][2])
        print(block[1][0],"|",block[1][1],"|",block[1][2])
        print(block[2][0],"|",block[2][1],"|",block[2][2])
    if block[0][0]!=' ' and block[0][1]!=' ' and block[0][2]!=' ' and block[1][0]!=' ' and block[1][1]!=' ' and block[1][2]!=' 'and block[2][0]!=' ' and block[2][1]!=' 'and block[2][2]!=' ':
        print("Draw!!")
        break
print("play again")