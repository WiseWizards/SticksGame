import random
#Welcome the player to the game
print("Welcome to the Sticks Game! How to play: The game starts with some number of sticks on the table (between 10 and 100, chosen by the user. Three players take turns choosing how many sticks to take. On each player’s turn they must take either 1, 2, or 3 sticks. The player to take the last stick loses. However, there is a catch, the third player is the computer. Good luck! \n")

#Set variables equal to zero to use later
exit_count = 0
player_one_loses = 0
player_two_loses = 0
computer_loses = 0

#Create a while loop that continues the game as long as the player does not want to exit
while exit_count != 1:
  #Set the number of sticks equal to the number of sticks chosen by the user
  sticks_on_table = int(input("Enter the amount of sticks you want on the table (between 10-100): "))
  #Error Checking for sticks on table
  while sticks_on_table < 10 or sticks_on_table > 100:
    print("ERROR: Invalid number of sticks. Please try again.")
    sticks_on_table = int(input("Enter the amount of sticks you want on the table (between 10-100): "))
  #As long as everything below is true, the program will keep running
  while True:
    #PLayer one is asked to choose how many sticks they want to take
    one_stick =int(input("Player One: Enter the number of sticks to take (1, 2, 3): "))

    #Error Checking for Player One sticks
    while one_stick != 1 and one_stick != 2 and one_stick != 3:
      print("ERROR: Invalid number of sticks. Please try again.")
      one_stick =int(input("Player One: Enter the number of sticks to take (1, 2, 3): "))
      
    sticks_on_table -= one_stick
    print("There are " + str(sticks_on_table) + " sticks left.")
    #If the sticks left on the table is less than zero, player one loses
    if sticks_on_table <=0:
      print("Player one loses.")
      player_one_loses += 1
      #The player is asked if they want to play again
      exit = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
      #Error Checking for player one exit
      while exit != "y" and exit != "n":
        print("ERROR: Invalid input. Please try again.")
        exit = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
      #If the player wants to play again, the program will restart
      if exit.lower() == "y":
        break
      #If the player does not want to play again, the program will end and the loses are printed
      else:
        exit_count += 1
        print("Player One Losses: " + str(player_one_loses))
        print("Player Two Losses: " + str(player_two_loses))
        print("Computer Losses: " + str(computer_loses))
        break
    #Player two is asked to choose how many sticks they want to take
    two_stick = int(input("Player Two: Enter the number of sticks to take (1, 2, 3): "))
    #Error Checking for Player Two sticks
    while two_stick != 1 and two_stick != 2 and two_stick != 3:
      print("ERROR: Invalid number of sticks. Please try again.")
      two_stick =int(input("Player Two: Enter the number of sticks to take (1, 2, 3): "))
  
    sticks_on_table -= two_stick
    print("There are " + str(sticks_on_table) + " sticks left.")
    #If the sticks left on the table is less than zero, player two loses
    if sticks_on_table <=0:
      print("Player two loses.")
      player_two_loses += 1
      exit = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
      #Error checking for player two exit
      while exit != "y" and exit != "n":
        print("ERROR: Invalid input. Please try again.")
        exit = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
      #If the player wants to play again, the program will restart
      if exit.lower() == "y":
        break
      #If the player does not want to play again, the program will end and the loses are printed
      else:
        exit_count += 1
        print("Player One Losses: " + str(player_one_loses))
        print("Player Two Losses: " + str(player_two_loses))
        print("Computer Losses: " + str(computer_loses))
        break
    #The computer chooses 1-3 sticks
    computer_stick = random.randint(1, 3)
    sticks_on_table -= computer_stick
    #The computer's sticks are printed 
    print("The computer chooses " + str(computer_stick) + " sticks. There are " + str(sticks_on_table) + " sticks left.")
    #If the sticks left on the table is less than zero, the computer loses
    if sticks_on_table <=0:
      print("The computer loses")
      computer_loses += 1
      #The player is asked if they want to play again
      exit = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
      #Error checking for computer exit
      while exit != "y" and exit != "n":
        print("ERROR: Invalid input. Please try again.")
        exit = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
      #If the player wants to play again, the program will restart
      if exit.lower() == "y":
        break
      #If the player does not want to play again, the program will end and the loses are printed
      else:
        exit_count += 1
        print("Player One Losses: " + str(player_one_loses))
        print("Player Two Losses: " + str(player_two_loses))
        print("Computer Losses: " + str(computer_loses))
        break


