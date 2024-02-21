import random

select_bot = ["rock", "paper", "scizzor"]
select_bot = random.choice(select_bot)

def game(select_user,select_bot):
    if select_user == select_bot:
        print("Draw!")
        print("Oponent select:", select_bot)
    elif select_user == "rock" and select_bot == "paper":
        print("You lose!")
        print("Oponent select:", select_bot)
    elif select_user == "rock" and select_bot == "scizzor":
        print("You win!")
        print("Oponent select:", select_bot)
    elif select_user == "paper" and select_bot == "scizzor":
        print("You lose!")
        print("Oponent select:", select_bot)
    elif select_user == "paper" and select_bot == "rock":
        print("You win!")
        print("Oponent select:", select_bot)
    elif select_user == "scizzor" and select_bot == "rock":
        print("You lose!")
        print("Oponent select:", select_bot)
    elif select_user == "scizzor" and select_bot == "paper":
        print("You win!")
        print("Oponent select:", select_bot)

select_user = input("Rock, paper or scizzor? ")
game(select_user, select_bot)