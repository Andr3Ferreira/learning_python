# import random

# '''
#     Function to print the welcome screen, prompt the user to start the game and call the playGame() function
# '''
# def startGame():
#   print("=============================")
#   print("  Python Game of War")
#   print("=============================")
#   start = str(input("\nTo start the game press ENTER: "))
#   if start == "":
#     playGame()
#   else:
#     print("Exiting. Thanks for playing!")
#     return -1

# '''
#     Function that actually runs the rounds through a loop until all the 20 rounds are finished. 
#     By the end of the 20 rounds, the function replayGame() is called.
# '''
# def playGame():
#   list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
#   score1 = 0
#   score2 = 0
#   round = 0

#   # Loop that will run the game for the user
#   while round < 2:
#     number1 = random.choice(list)
#     number2 = random.choice(list)
#     print("\nYour card: ", str(number1)+". Opponent's card: ", str(number2))
    
#     # If statement to count the score and the rounds
#     if(number1 > number2):
#         print("==> You WON this round! :)")
#         score1 += 2
#         round += 1
#     elif(number1 == number2):
#         print("==> It's a DRAW! :|")
#         score1 += 1
#         score2 += 1
#         round += 1
#     elif(number1 < number2):
#         print("==> You LOST this round! :(")
#         score2 += 2
#         round += 1
#     else:
#         print("Oh oh! Something went wrong. Exiting the game...")
#         return -1
    
#     #Prompts the user to continue playing after each round
#     run = str(input("\nPress ENTER to continue: "))
#     if run != "":
#       print("Exiting. Thanks for playing!")
#       return -1
    
#   # Compares the score of both players and call replayGame() function
#   if score1 < score2:
#     print("You lost!")
#     replayGame()
#   else:
#     print("You win!")
#     replayGame()


# '''
#     Function to ask if the user wants to play again or not.  
# '''
# def replayGame():
#     replay = str(input("Play again? Yes(y) No(n) ").lower())

#     # If positive, it calls the playGame() function.
#     if replay == "yes" or replay == "y" or replay == "":
#         playGame()
#     # If negative, it exits the game.
#     elif replay == "no" or replay == "n" or replay != "":
#         print("Exiting. Thanks for playing!")
#         return -1
#     # If some funny business happens, it exits the game anyway.
#     else:
#         print("Oh oh! Something went wrong. Exiting the game...")
#         return -1
