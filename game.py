import random

def fun():
    choices = ["rock", "paper", "scissors"]
    while True:
        print("\nWelcome to the Rock-Paper-Scissors Showdown!")
        print_menu()
        user_selection = get_user_choice()
        if user_selection == 4:
            print("Thanks for playing!")
            break
        computer_selection = oppChoice()

        print("You picked:", choices[user_selection])
        print("Computer chose:", choices[computer_selection])

        chooseAWinner(user_selection, computer_selection)

def print_menu():
    
    print("Choose your move: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit the game")

def get_user_choice():
    
    while True:
        user_input = input("Enter your choice (1-4): ")
        if user_input == "4":
            return 4
        elif user_input not in ["1", "2", "3"]:
            print("Invalid choice. Enter a number between 1 and 4.")
        else:
            return int(user_input) - 1

def oppChoice():
    
    return random.randint(0, 2)

def chooseAWinner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
            user_choice == 2 and computer_choice == 1):
        print("You won! 🏆🏅")
    else:
        print("Computer won! :/ \nBetter luck next time! :)")

if __name__ == "__main__":
    fun()
