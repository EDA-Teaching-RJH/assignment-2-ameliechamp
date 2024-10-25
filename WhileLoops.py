### Part Two -- your code goes here. 
import random
num = random.randint(0,100)
guess = int(input("I am thinking of a number. Enter in your guess: "))
while guess != num:
    print("That is incorrect.")
    if guess > num:
        print("That guess is too high.")
    elif guess < num:
        print("That guess is too low.")
    guess = int(input("Enter another guess: "))
print("Correct! Well done, the number is", num)