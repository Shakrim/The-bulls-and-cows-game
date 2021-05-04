from random import randint



SEPARATOR = "-" * 100


def main():
    # Intro & Rulles
    Invitation()

    # Generation of secret code
    generated_code = Generation_of_number(4)
    print(generated_code)

    # Game parameters
    game_on = True
    attempts = 0

    while game_on and attempts < 10:
        # User input
        my_guess = input(f"Enter your 4-digit code or 'q' for exit: ")

        # Verifying input code
        if Code_check(my_guess):
            continue

        # Transformation my_guess into the list with int
        my_guess_list = [character for character in my_guess]
        for i in range(0, len(my_guess_list)):
            my_guess_list[i] = int(my_guess_list[i])

        #measuring parameters of game
        attempts += 1
        print(f"Attempt(s): {attempts}")

        #scoring
        score = count_score(my_guess_list, generated_code)
        print(score)
        print(SEPARATOR)



        if check_game_over(score, attempts):
            break



def Invitation()-> None:
    print(SEPARATOR,f"GAME BULLS AND COWS".center(len(SEPARATOR)), SEPARATOR, sep = '\n')
    print("""Rules:
    # I've generated a random 4-digit code for you. 
    # Your task is to guess the correct code.
    # Digits will not repeat and the number cannot begin with 0.
    # If your digit guess matches with that randomly generated you received bull.
    # If your digit guess is in other position of that randomly generated you received cow.
    
Are you ready? Let's play!""")
    print(SEPARATOR)


def Generation_of_number(number:int) ->list:
    """ The function generates unique 4-digit code as a list, where first digit must be from 1-9.
    The another must very from others to create unique code. As an example (1234)"""

    randomlist = []
    for i in range(0, 10):
        if len(randomlist) == number:
            break
        else:
            if i == 0:
                n = randint(1, 9)
                randomlist.append(n)
            else:
                n = randint(0, 9)
                if n in randomlist:
                    continue
                else:
                    randomlist.append(n)
    return randomlist


def Code_check(user_code:str) -> bool:
    """ This function verifies the correct format of user's code.
    If wrong input is detected, the function returns True."""

    result = True
    if user_code == "q" or user_code == "Q":
        exit()
    elif user_code.isdigit():
        if len(user_code) < 4 or len(user_code) > 4:
            print("The code must contain 4 digits.")
            return result
        elif user_code[0] == "0":
            print("The first digit needs to be different than 0.")
            return result
        elif len(user_code) == 4:
            for i in range(len(user_code)):
                for j in range(i + 1, len(user_code)):
                    if (user_code[i] == user_code[j]):
                        print("Be careful you have duplicate digit.")
                        return result
                    else:
                        continue
    else:
        print("You entered non-digit character.")
        return result


def count_score(my_guess, code) -> dict:
    """ This function creates dictionary for calculation of bull(s) and cow(s)"""
    score = {"bull(s)":0, "cow(s)":0}
    for index, cislo in enumerate(my_guess):
        if cislo == code[index]:
            score["bull(s)"] = score["bull(s)"] +1
        elif cislo in code:
            score["cow(s)"] = score["cow(s)"] + 1

    return score

def check_game_over(score:dict, attemps:int) ->bool:
    """ Check user's win."""
    game_over = True
    if score["bull(s)"] == 4:
        print(f"Correct, you've guessed the right number.")
        evaluation(attemps)

    else:
        game_over = False


    return game_over

def evaluation(attemps:int):
    """ This function should evaluate the performance of user.
     Simply, it compares the number of attempts required for guessed right number. """
    if attemps < 4:
        print(f"Amazing! You needeed only {attemps} attemps.")

    elif attemps > 4 and attemps < 8:
        print(f'Very well! You just needed {attemps} attemps.')

    else:
        print(f'You need better luck next time. You needed {attemps} attemps.')



main()