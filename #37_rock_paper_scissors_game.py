import random

play_again = True

while play_again:
    #rock or paper or scissors
    choises = ["r", "p", "s"]
    computer = random.choice(choises)
    human = None
    while human not in choises:
        human = input("Choose Rock, Paper or Scissors (r/p/s): ").lower()

    if computer == human:
        print("Tie")
    elif computer == "r" and human == "s":
        print("You lost\nThe computers choise was rock")
    elif computer == "p" and human == "r":
        print("You lost\nThe computers choise was paper")
    elif computer == "s" and human == "p":
        print("You lost\nThe computers choise was scissors")
    else:
        print("You won")

    play_again = None
    if input("Want to play again (y/n): ").lower() == "y":
        play_again = True
    else:
        print("Bye")
