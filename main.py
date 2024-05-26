#Just a fun little game I made durning lunch one day. Try to guess the number!

import random

print("Hello, welcome to this little game I made! Try to guess the number!")
plays = 0



def ttime(xe):
    try:
        y = int(xe)

        return y
    except:
        xep = input("Input integers only. ")
        return ttime(xep)


def higher(xe, lower):
    try:
        y = int(xe)

    except:
        xep = input("Input integers only. ")
        return higher(xep, lower)

    if not (y > lower):
        xep = input("Upper bounds must be greater than lower bounds. ")
        return higher(xep, lower)

    return y

def guezz(lower,upper):
    question = 'Guess a number from from '+ str(lower)+ '-'+ str(upper)+ ': '
    guess = ttime(input(question))
    return guess


def game():
    number_list = []
    gnum = 1
    lower = ttime(input("Input a lower bounds for your number range: "))
    upper = higher(input("Input an upper bounds for your number range: "), lower)
    first_numb = random.randint(lower, upper)

    gin = guezz(lower,upper)

    while gin != first_numb:
        number_list.append(gin)
        gnum = gnum + 1
        if gin > first_numb:
            print("Your guess was too high.")
        else:
            print("Your guess was too low.")
        print("Your past guesses are", number_list)
        gin = guezz(lower,upper)
    number_list.append(gin)
    print("You got the correct answer in", gnum, "guesses! "
                                                 "\n You guessed", number_list, "!")


while __name__ == "__main__":

    run = game()
    plays = plays + 1
    print("You have guessed correctly a total of ", (plays), " times!")
    er = input("Input 0 to exit, or other to play again")
    if er == "0":
        exit()
