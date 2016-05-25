from random import randint


def guess_a_number():
    """Game to guess a number the computer randomly generated."""
    return randint(0,100)

    # TODO:
    # generate a random number (uniformly distributed between 0 and 100)
    # read input from the user and validate that the input is numeric (use the function check_raw)
    # check whether the number was guessed 
    # implement the functions evaluate_my_number, which checks whether the number is too high or too low
    # and print this information to the user
    # let the computer guess, therefore implement the demo_a_number function
    


def check_raw(let_computer_guess,guess, number print_string='Please try again: '):
    """Gets the string, raw_input should print, checks and returns the input."""
    if let_computer_guess==False:
        input_number=input(print_string)
        typetest=False
        while typetest==False:
            try:
                int_number=int(input_number)
                typetest=True
            except ValueError:
                print("Incorrect input: Integer value expected!")
                input_number=input(print_string)
    else:
        if guess>number:
            int_number=randint(number,100)
        else:
            int_number=randint(0,number)
    return int_number


def evaluate_my_number(guess, random_number):
    """Is the guess to high or to low? Guess again!"""
    if guess==random_number:   
        print("Hurra!") 
        return True
    elif guess<random_number:
        print("Guess too high.")
    else:
        print("Guess too low.")
    return False



let_computer_guess=False
    
guess=guess_a_number()
#print guess


mynumber=check_raw(let_computer_guess, guess, mynumber)

while evaluate_my_number(guess,mynumber)!=True:
    mynumber=check_raw(let_computer_guess, guess, mynumber)