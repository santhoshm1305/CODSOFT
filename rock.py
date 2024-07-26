import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def play():
    game_images = [rock, paper, scissors]
    print("\t\t\t\t\t\tWelcome to the game of Rock, Paper, Scissors!")
    user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print("\nYou chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

play()
while True:
    play_again = int(input("\nChoose 0 to Quit, 1 to play again!\n"))
    if play_again == 1:
        play()
    elif play_again == 0:
        print("Good Game!")
        break
    elif play_again != 0 or 1:
        print("Enter a valid choice.")