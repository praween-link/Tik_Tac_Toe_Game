
print("_____________________-- TIC-TAC-TOE GAME --__________________________")

print("                                 START GAME                          ")
print("                      ______________________________                 ")
print()

box = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#--------------------------Display tic tac toebox---------------------------
def display():
    print(' ' + box[0] + '|' + ' ' + box[1] + ' ' + '|' + ' ' + box[2] + ' ')
    print("__|___|__")
    print("  |   |  ")
    print(' ' + box[3] + '|' + ' ' + box[4] + ' ' + '|' + box[5] + ' ')
    print("__|___|__")
    print("  |   |  ")
    print(' ' + box[6] + '|' + ' ' + box[7] + ' ' + '|' + box[8] + ' ')

#------------------------------Vinner Cheacking Function------------------------------------
def vineer_cheacking():
    global row
    global column
    global mid
    r1 = box[0] == box[1] == box[2] != " "
    r2 = box[3] == box[4] == box[5] != " "
    r3 = box[6] == box[7] == box[8] != " "
    row = False
    if r1 or r2 or r3:
        row = True

    c1 = box[0] == box[3] == box[6] != " "
    c2 = box[1] == box[4] == box[7] != " "
    c3 = box[2] == box[5] == box[8] != " "
    column = " "
    if c1 or c2 or c3:
        column = True

    m1 = box[0] == box[4] ==box[8] != " "
    m2 = box[2] == box[4] ==box[6] != " "
    mid = " "
    if m1 or m2:
        mid = True


#-------------------------------------------------------------------------

#----------------------------Start Turn Game-----------------------------
def turn():
    pos = []  #List For Storing Selected Positions

    #------------------------------------ Start Turn Of Geast-X ----------------------------------
    def turn_X():
        print("X's turn:-")
        position = int(input("choose your position from 1-9: "))
        ch = position in pos
        print(ch)
        if position <= 9 and position > 0 and ch == False:
            position = position-1
            box[position] = 'X'
            pos.append(position+1)
        else:
            turn_X()

    #-------------------------------- Start Turn Of Geast-0 -------------------------------------

    def turn_0():
        global position
        print("0's turn:-")
        position = int(input("choose your position from 1-9: "))
        ch = position in pos
        if position <= 9 and position > 0 and ch == False:
            position = position-1
            box[position] = '0'
            pos.append(position+1)
        else:
            turn_0()

    #---------------------- Repitation Of Turns ---------------------------
    def repit_turn():
        count = 0
        NoVinner = 0

        if first_turn == 0:
            display()
            while count<9:

                turn_0()
                display()
                count +=1

                vineer_cheacking()
                if row == True or column == True or mid == True:
                    print("Game Over...")
                    print()
                    print(">>> Vinner Gest 0!")
                    NoVinner = 1
                    break

                else:
                    if count<9:
                        turn_X()
                        display()
                        count +=1
                    vineer_cheacking()
                    if row == True or column == True or mid == True:
                        print("Game Over...")
                        print()
                        print(">>> Vinner Gest X!")
                        NoVinner = 1
                        break

        elif first_turn == 1:
            display()
            while count<9:
                turn_X()
                display()
                count +=1

                vineer_cheacking()
                if row == True or column == True or mid == True:
                    print("Game Over...")
                    print()
                    print(">>> Vinner Gest X!")
                    NoVinner = 1
                    break
                else:
                    if count<9:
                        turn_0()
                        display()
                        count +=1
                    vineer_cheacking()
                    if row == True or column == True or mid == True:
                        print("Game Over...")
                        print()
                        print(">>> Vinner Gest 0!")
                        NoVinner = 1
                        break

        else:
            print()

        if NoVinner != 1:
            print(" No Vinner...\n Game Over...")

    #------------------------------- Choice Whose First Turn --------------------------------
    def chose_turn():
        global first_turn
        first_turn = int(input("Whose first turn gest 0(0) or 1(X): "))
        if first_turn==0 or first_turn==1:
            repit_turn()
        else:
            chose_turn()

    #---------------------------------
    chose_turn()

#-----------------------------

def play_game():
    turn()
#------------------------------

play_game()
