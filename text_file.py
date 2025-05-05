def game_record(player_move,player_black_hole,computer_move,computer_black_hole,player_result,computer_result):
    "A record of the game written in a text file"
    from datetime import datetime

    #Creating and initializing variables
    file = 0

    #current date and time
    now = datetime.now()
    #Creating the text file name
    file_name = now.strftime("%Y_%m_%d_%H_%M")+ ".txt"
    #Open a text file with write only mode
    file = open(file_name,"w")
    with file:
        #Player's record
        file.write("Player")
        file.write("\nTotal moves" + " " + str(player_move))
        file.write("\nBlack hole hits" + " " + str(player_black_hole))
        file.write("\n" + str(player_result))
    
        #Computer's record
        file.write("\n\nComputer")
        file.write("\nTotal moves" + " " + str(computer_move))
        file.write("\nBlack hole hits" + " " + str(computer_black_hole))
        file.write("\n" + str(computer_result))
