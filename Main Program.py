#Import packages
import dice_roll

#Calling the game function
dice_roll.game()
print()
#Asking the player wants to play again or not          
play_again = input("Do you want to play again? y/n : ")

if play_again=="y":
    dice_roll.game()
else:
    exit()
