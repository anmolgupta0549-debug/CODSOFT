import random

print("Rock - Paper - Scissors Game")
print("Type rock, paper, or scissors to play.")

user_score = 0
computer_score = 0

while True:
    user = input("\nYour choice: ").lower()
    choices = ["rock", "paper", "scissors"]

    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {user_score}  Computer: {computer_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
