import random

USER_CHOICES = ["rock","scissor","paper"]


def get_user_input():
    choice = input('pick your choice: [\"rock\",\"scissor\",\"paper\"] :  ')
    while choice not in USER_CHOICES:
        print("Please enter valid value")
        choice = input('pick your choice: [\"rock\",\"scissor\",\"paper\"] :  ')
    return choice


def get_pc_input():
    return random.choice(USER_CHOICES)

def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        return "DRAW!"
    elif (user_input == "rock" and pc_input == "scissor") or (user_input == "scissor" and pc_input == "paper") or (user_input == "paper" and pc_input == "rock"):
        print("user won")
    else:
        print("pc won")


def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input,pc_input)
    print("pc choice :",pc_input)
    print("end of program")

answer = 'y'
while answer == 'y':
    main()
    answer = input('do you want to continue? [y/n]')