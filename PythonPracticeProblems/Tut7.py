# Guess The number
# Generate a random integer(random dekhte hi humme random ko import karna hai) from a to b. You and your friend have to guess a number between two numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum number of trials wins!
# Randomly generate a number after taking a and b as input and don’t show that to the user (say 6)
# Input:
#
# Enter the value of a
#
# 4
#
# Enter the value of b
#
# 13
#
# Output:
#
# Player1 :
#
# Please guess the number between 4 and 13
#
# 5
#
# Wrong guess a greater number again
#
# 8
#
# Wrong guess a smaller number again
#
# 6
#
# Correct you took 3 trials to guess the number
#
# Player 2:
#
# .
#
# .
#
# .
#
# Correct you took 7 trials to guess the number
#
# Player 1 wins!

import random
def guessGame(x,a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number\n"))
            nguess += 1


    print(f"{x} guessed the number in {nguess} guesses\n")
    return nguess

if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)  # randint ek function hota hai random class ka jo ki do arguments leta hai(random.randint(start, stop) start-> An integer specifying at which position to start. stop-> An integer specifying at which position to end.)
    x1 = input("To play this game enter your name\n")
    print(f"{x1}'s turn\n")
    g1 = guessGame(x1,a, b, actual1)
    x2 = input("To play this game enter your name\n")
    if x1 == x2:
        print(f"{x1} already played the match\n")
        exit()
    print(f"{x2}'s turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(x2,a, b, actual2)

    if g1 < g2:
        print(f"{x1} won the match!\n")

    elif g1 > g2:
        print(f"{x2} won the match!\n")

    else:
        print("Its a Tie!\n")

    print(f"The number for {x1} was {actual1} and for {x2} was {actual2}")

