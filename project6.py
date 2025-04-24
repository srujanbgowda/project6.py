import random

def play():
    choices = ["rock", "paper", "scissors"]
    print("🪨 📄 ✂️  Welcome to Rock, Paper, Scissors!")

    while True:
        player = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if player == "exit":
            print("👋 Thanks for playing!")
            break
        if player not in choices:
            print("❌ Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print(f"🧠 Computer chose: {computer}")

        if player == computer:
            print("🤝 It's a tie!\n")
        elif (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ):
            print("🎉 You win!\n")
        else:
            print("💻 Computer wins!\n")

if __name__ == "__main__":
    play()
