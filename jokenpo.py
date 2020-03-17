import random

jokenpo = (["rock", "paper", "scissor"])

user_input = "Empty"
while user_input == "Empty":
    user_input = input("Choose between rock, paper or scissor \n")
    if user_input.lower() not in ["rock", "paper", "scissor"]:
        print("You need to choose a valid entry.")
        user_input = "Empty"
    else:
        print("You choose: " + user_input.lower())

player = user_input.lower()
compvalue = random.choice(jokenpo)

print("I choose: " + compvalue)

if player == compvalue:
    print("It's a draw!")
elif player == "scissor":
    if compvalue == "paper":
        print("You lost!")
    if compvalue == "rock":
        print("You win!")
elif player == "paper":
    if compvalue == "scissor":
        print("You lost!")
    if compvalue == "rock":
        print("You win!")
elif player == "rock":
    if compvalue == "paper":
        print("You lost!")
    if compvalue == "scissor":
        print("You win!")