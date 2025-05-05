def game():
    "Roll the dice and find the winner of the 20x2 Game"
    import text_file
    import time
    import random

    #Creating and initializing variables
    player_position = -1
    computer_position = -1
    player_black_hole = 0
    computer_black_hole = 0
    player_move = 0
    computer_move = 0
    player_result = ""
    computer_result = ""

    #Creating the list
    board = []
    for i in range(2):
        row = [" "]*20
        board.append(row)
    board[0][6] = "O"
    board[0][13] = "O"
    board[1][6] = "O"
    board[1][13] = "O"

    #Starting the game
    print("\t\t\t\t\t\tWelcome to the 20x2 Game")
    time.sleep(1)
    print()
    print()
    print("Initial game board")

    #Continue the game until a player wins
    while player_position <=20 and computer_position <=20:
        print()
        time.sleep(1)

        #Moving player's pawn on the game board
        if player_position > 0: 
            board[0][player_position-1] = "X"
        if computer_position > 0: 
            board[1][computer_position-1] = "X"

        #Printing the initial game board
        print("     1     2     3     4     5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20")
        for row in board:
            print(" ","|    ", end="")
            for block in row:
                print(block, end="|    ")
            print()
        print()
    
        time.sleep(1)
        
        input("Press enter key to roll the dice")
        
        #Player's turn
        dice_value = random.randrange(1,7)
        
        #Whether the player’s pawn is permitted to enter to the board or not
        if dice_value == 6 and player_position == -1:
            print("Your dice roll is",dice_value,"and you can start the game now")
            player_position = 0
        elif dice_value != 6 and player_position == -1: 
            print("Your dice roll is",dice_value,"and you can't start the game until you get 6")
        #Calculating the total moves of the player
        else:
            player_move = player_move + 1
            board[0][player_position-1] = " "
            steps = dice_value // 2
            #If the dice value is 1
            if steps == 0: 
                print("Your roll is",dice_value,"and no moves")
            else:
                new_position = player_position + steps
                #If the player crossed the 20th block first and win the game
                if new_position>=20:
                    player_result = "Won the game"
                    computer_result = "Lost the game"
                    print("Your dice roll is",dice_value)
                    print()
                    print()
                    print("Congratulations!!! You won the game")
                    break
                #If the player hits a black hole
                elif new_position == 7 or new_position == 14: 
                    print("Your dice roll is",dice_value,"Oops! You hit a black hole")
                    player_black_hole = player_black_hole + 1
                    player_position = 1
                else: 
                    player_position = new_position
                    print("Your dice roll is",dice_value,"and you moved to block", player_position )

        time.sleep(1)

        #Computer's turn
        computer_dice_value = random.randrange(1,7)
        
        #Whether the computer’s pawn is permitted to enter the board or not
        if computer_dice_value == 6 and computer_position == -1:
            print("The computer dice roll is",computer_dice_value,"and the computer can start the game now")
            computer_position = 0 
        elif computer_dice_value != 6 and computer_position == -1:
            print("The computer dice roll is",computer_dice_value,"and the computer can't start the game until it gets 6")
        #Calculating the total moves of the computer
        else:
            computer_move = computer_move + 1
            board[1][computer_position-1] = " "
            moves = computer_dice_value // 2 
            #If the dice value is 1
            if moves == 0:
                print("The computer dice roll is",computer_dice_value,"and no moves")
            else:
                new_position = computer_position + moves
                #If the computer crossed the 20th block first and win the game
                if new_position>=20:
                    player_result = "Lost the game"
                    computer_result = "Won the game"
                    print("The computer dice roll is",computer_dice_value)
                    print()
                    print()
                    print("The Computer won!!!\n\nSorry, You lost the game")
                    break
                #If the computer hits a black hole
                elif new_position == 7 or new_position == 14: 
                    print("The computer dice roll is",computer_dice_value,"Oops! The computer hits a black hole")
                    computer_black_hole = computer_black_hole + 1
                    computer_position = 1
                else: 
                    computer_position = new_position
                    print("The computer dice roll is",computer_dice_value,"and the computer moved to block", computer_position)



    #Calling the game_record function
    text_file.game_record(player_move,player_black_hole,computer_move,computer_black_hole,player_result,computer_result)



    

    
