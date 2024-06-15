import random

# write 'hello world' to the console
print('hello world')
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# develop a rock-paper-scissors game
# 0. make the game in a menu
# make a code to check if the user must enter the valid choice
user_score = 0
round = 0
win = 0
# make all these instructions in a loop
while True:
    print("Welcome to Rock-Paper-Scissors Game!")
    print("1. Play the game")
    print("2. Quit")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        user_choice = input('Enter your choice: rock, paper, or scissors: ').lower()
        valid_choices = ['rock', 'scissors', 'paper']
        if user_choice in valid_choices:
            # 2. Get the computer's choice
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
            # 3. Determine the winner
            round += 1
            # claculate the user score
            
            if user_choice == computer_choice:
                print('It is a tie!')
            elif user_choice == 'rock' and computer_choice == 'scissors':
                print('You win!')
                win += 1
                user_score += 1
            elif user_choice == 'scissors' and computer_choice == 'paper':
                print('You win!')
                win += 1
                user_score += 1
            elif user_choice == 'paper' and computer_choice == 'rock':
                print('You win!')
                win += 1
                user_score += 1
            else:
                print('You lose!')
                user_score -= 1
            # 4. Display the winner
            print(f'You chose {user_choice}, and the computer chose {computer_choice}.')
        else :
            print("Invalid choice. Please try again.")
        
    elif choice == "2":
        print("Thank you for playing. Goodbye!")
        # display the user score
        print(f'Your score is: {user_score}')
        # display the number of rounds played
        print(f'You played {round} rounds and you wins {win}.') 
        break
    else:
        print("Invalid choice. Please try again.")

