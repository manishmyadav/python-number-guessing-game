from random import randint
from os import system
from art import logo

def main():
    should_continue = True
    while should_continue:
        print("Welcome!")
        print(logo)
        difficulty_level = input("Difficulty level: \'Easy\' or \'Hard\'? ").lower()
        guess_the_number(difficulty_level)
        choice = input("Do you wanna play again? \'y\' or \'n\' ")
        if choice == 'y':
            should_continue = True
            system('cls') # Clear the console on windows
            #system('clear') Clear the console on linux
        else:
            should_continue = False
    return            
        
def guess_the_number(difficulty_level):
    secret_number = randint(1, 100)
    if difficulty_level =='easy':
        total_attempts = 10
    else:
        total_attempts = 5   
    print("Heyy! I have guessed a number from 1 to 100")
    print(f"You have {total_attempts} attempts to guess the number")    
    left_attempts = total_attempts
    for _ in range(total_attempts):
        user_guess = int(input("Guess the no.: "))
        if user_guess == secret_number:
            print(f"You guessed it correctly! The number is {secret_number}")
            break
        elif user_guess < secret_number:
            print("Too Low!")
            left_attempts -= 1
            print(f"You have only {left_attempts} attempts left!")
        else:
            print("Too High!")
            left_attempts -= 1
            print(f"You have only {left_attempts} attempts left!")
    else:
        print("You have exceeded the maximum no of attempts!")
        print(f"The number I guessed was {secret_number}!")
    return

# Calling main() at last to follow python program flow
main()
