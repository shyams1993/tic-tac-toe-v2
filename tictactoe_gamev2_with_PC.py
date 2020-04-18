import time, sys, random
list=['0','1','2','3','4','5','6','7','8']
comp_input=[0,1,2,3,4,5,6,7,8]
counter=0

def boardprint():
    print(list[0],"|",list[1],"|",list[2])
    print("----------")
    print(list[3],"|",list[4],"|",list[5])
    print("----------")
    print(list[6],"|",list[7],"|",list[8])

boardprint()

def checkwin():
    global counter
    if (list[0]=='X' and list[1]=='X' and list[2]=='X') or (list[3]=='X' and list[4]=='X' and list[5]=='X') or (list[6]=='X' and list[7]=='X' and list[8]=='X') or (list[0]=='X' and list[3]=='X' and list[6]=='X') or (list[1]=='X' and list[4]=='X' and list[7]=='X') or (list[2]=='X' and list[5]=='X' and list[8]=='X') or (list[0]=='X' and list[4]=='X' and list[8]=='X') or (list[2]=='X' and list[4]=='X' and list[6]=='X'):
        print("'X' wins.")
        counter+=1
    elif (list[0]=='O' and list[1]=='O' and list[2]=='O') or (list[3]=='O' and list[4]=='O' and list[5]=='O') or (list[6]=='O' and list[7]=='O' and list[8]=='O') or (list[0]=='O' and list[3]=='O' and list[6]=='O') or (list[1]=='O' and list[4]=='O' and list[7]=='O') or (list[2]=='O' and list[5]=='O' and list[8]=='O') or (list[0]=='O' and list[4]=='O' and list[8]=='O') or (list[2]=='O' and list[4]=='O' and list[6]=='O'):
        print("'O' (Computer Brain) wins.")
        counter+=1

def x_entry():
    global x_pos,counter
    print("Player X enters first (HUMAN)")
    x_pos = int(input("Where do you want to enter 'X'?"))
    if (list[x_pos]!= 'O') and (list[x_pos]!= 'X'):
        list[x_pos]='X'
        boardprint()
    else:
        print("This position is already filled : Looping back")
        x_entry()
    checkwin()
    if counter!=0:
        print("GAME OVER. \nExiting in 3 seconds")
        time.sleep(3)
        sys.exit()

def o_entry():
    global o_pos,counter
    print("Player O enters next : Computer Brain (AI)")
    o_pos = random.choice(comp_input)
    if (list[o_pos]!= 'X') and (list[o_pos]!= 'O'):
        list[o_pos]='O'
        boardprint()
    else:
        print("This position is already filled : Looping back")
        o_entry()
    checkwin()
    if counter!=0:
        print("GAME OVER. \nExiting in 3 seconds")
        time.sleep(3)
        sys.exit()

for x_pos in range(len(list)-4):
    for o_pos in range(len(list)-5):
        x_entry()
        o_entry()
        time.sleep(1)
    if counter <=1:
        print("\n GAME OVER  -- It's going to end up as a Tie. \nExiting in 3 seconds")
        time.sleep(3)
        sys.exit()