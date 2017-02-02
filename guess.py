#!/bin/python

# To refresh your memory of Python, write a 'guess the number' game. The
# computer should 'think' of a random number within a certain range, and
# challenge the user to guess the number. Provide feedback and hints for the
# user; such as "too high" or "too low".

import random

# initialize the pseudorandom generator
random.seed()

LOW_END = 0
HIGH_END = 9


def generate_random_number(low, high):
    return random.randint(low, high)


def display_intro():
    print("I am thinking of an integer from " + str(LOW_END) + " to " + str(
        HIGH_END) + ".")


def input_guess():
    """
    Prompts for user input. Keeps prompting until we get an integer.
    :return:
    """
    while True:
        guessed_number_string = input("What number am I thinking of? ")
        # Make sure it's actually an integer
        try:
            guessed_number = int(guessed_number_string)
            break
        except ValueError:
            print("That's not an integer!")
            continue

    return guessed_number


def test_if_in_range(guess_int):
    if (guess_int >= LOW_END) or (guess_int <=HIGH_END):
        return True
    else:
        return False


def respond_low_high(target_int, guess_int):
    """
    Tests if the guess is equal to the target.
    If not, tell whether it is high or low and return false.
    :param target_int:
    :param guess_int:
    :return:
    """
    if guess_int > target_int:
        print("Sorry, your number is too high.")
        return False
    elif guess_int < target_int:
        print("Sorry, your number is too low.")
        return False
    elif guess_int == target_int:
        return True


def main():

    random_number = generate_random_number(LOW_END, HIGH_END)
    display_intro()

    while True:

        guessed_number = input_guess()
        if not test_if_in_range(guessed_number):
            print("That is not between " + str(LOW_END) +
                  " and " + str(HIGH_END) + "!")
            continue  # loop to another guess
        if not respond_low_high(random_number, guessed_number):
            continue  # keep guessing
        else:
            print("You got it! I picked " + str(random_number) + ".")
            break  # End


if __name__ == "__main__":
    main()
