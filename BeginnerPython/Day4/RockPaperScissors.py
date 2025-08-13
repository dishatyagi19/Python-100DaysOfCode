import random

print("Game : Rock, Paper, Scissors")

human_choice = int(input("Choose your option: Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if human_choice >=3 or human_choice < 0:
    print("You choose an invalid input. Result : Computer Won!")
else:    
    if human_choice == 0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif human_choice == 1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


    computer_choice = random.randint(0,2)

    if computer_choice == 0:
        print("Computer chose: Rock")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif computer_choice == 1:
        print("Computer chose: Paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    else:
        print("Computer chose: Scissors")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    #for results:-
    if human_choice == computer_choice: #rock, rock | paper, paper | scissors, scissors
        print("Draw")
    elif human_choice < computer_choice: #rock, paper | paper, scissors
        if human_choice == 0 and computer_choice == 2: #rock, scissors
            print("You Win!")
        else:
            print("Computer Won!")
    elif human_choice > computer_choice: #paper, rock | scissors, paper
        if human_choice == 2 and computer_choice == 0: #scissors, rock
            print("Computer Won!")
        else:    
            print("You Win!")
