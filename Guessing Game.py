# this is a guessing game
import random


def main():
    end = False
    lower_bound = 1
    upper_bound = 50

    while not end:
        answer = random.randint(lower_bound, upper_bound)
        # print("Answer: " + str(answer))
        print()
        guessNumber(answer, lower_bound, upper_bound)
        print()
        finished = input("Would you like to exit (Y/N)? ")
        print()
        if finished == "Yes" or finished == "YES" or finished == "y" or finished == "Y" or finished == "yes":
            end = True

    print()
    print("-------Program Terminated-------")


def guessNumber(answer, lower_bound, upper_bound):
    did_guess = False
    number_of_guesses = 0
    guess = int(input("Guess the number from " + str(lower_bound) + " and " + str(upper_bound) + ": "))

    while not did_guess:
        if guess > upper_bound or guess < lower_bound:
            print()
            guess = int(input("Your guess must be between " + str(lower_bound) + " and " + str(upper_bound) + ": "))
        elif guess > answer:
            print("Too high.")
            print()
            number_of_guesses += 1
            guess = int(input("Guess the number from " + str(lower_bound) + " and " + str(upper_bound) + ": "))
        elif guess < answer:
            print("Too low.")
            print()
            number_of_guesses += 1
            guess = int(input("Guess the number from " + str(lower_bound) + " and " + str(upper_bound) + ": "))
        elif guess == answer:
            number_of_guesses += 1
            print("You guessed it! It took you " + str(number_of_guesses) + " guesses.")

            did_guess = True



main()
