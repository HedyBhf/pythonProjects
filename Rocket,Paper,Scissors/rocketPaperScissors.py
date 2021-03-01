import random

game_list = ['Rock','Paper','Scissors']
computer = 0
player = 0

print('score : computer = ', str(computer), ' player = ', str(player))
run = True
while run:

    computer_choice = random.choice(game_list)
    player_choice = input("choose : 'Rock , Paper , Scissors' or Quit :")
    print('computer choice is :', computer_choice)
    print('player choice is :', player_choice)
    if player_choice == 'Rock':
        if computer_choice == 'Paper':
            print('Computer won!')
            computer+=1
        elif computer_choice == 'Rock':
            print('Tie !')
        else:
            print('player won!')
            player+=1

    elif player_choice == 'Paper':
        if computer_choice == 'Scissors':
            print('Computer won!')
            computer+=1
        elif computer_choice == 'Paper':
            print('Tie !')
        else:
            print('player won!')
            player+=1
    elif player_choice == 'Scissors':
        if computer_choice == 'Rock':
            print('Computer won!')
            computer+=1
        elif computer_choice == 'Scissors':
            print('Tie !')
        else:
            print('player won!')
            player+=1
    elif player_choice == 'Quit':
        print("")
        print("--------------")
        print('score : computer = ', str(computer), ' player = ', str(player))
        if computer > player:
            print('The Computer is the WINNER !')
        elif computer < player:
            print('The Player is the WINNER !')
        else:
            print("It's Tie Guys try again !")
        print("--------------")
        print("")
        break
    else:
        print('Wrong command!')
    print("")
    print("--------------")
    print('score : computer = ', str(computer), ' player = ', str(player))
    print("--------------")
    print("")


