import random

MAX_NUM = 10
MIN_NUM = 1


def generate_random_number():
    return random.randint(MIN_NUM,MAX_NUM)


def get_user_input():
    print(f"your number should be between {MIN_NUM} - {MAX_NUM}")
    while True:
        try:
            user_input = int(input("enter your guess : "))
        except ValueError:
            print("Error ! enter a valid number :")
        else:
            return user_input
        
def check_guessed_number(user_input,random_num):
    return user_input == random_num


def main():
    max_guess_count = 3
    random_num = generate_random_number()
    print(f"random number is : {random_num}")
    while max_guess_count > 0 :
        user_input = get_user_input()
        if(check_guessed_number(user_input,random_num)):
            print("you've guess right")
            break
        max_guess_count -= 1
        print(f"guesses left {max_guess_count}")
    else:
        print("you couldn't guess the number ")



if __name__ == "__main__":
    main()
