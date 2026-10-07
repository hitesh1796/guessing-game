import random
def guess_game():
    local_num = random.randint(1,50)
    return local_num

print("welcome to the guessing game!!\n\n")
print("*****rules*****")
print("     - I have a number in my mind between 1 and 50.")
print("     - You have to guess the number.")
print("     - If your guess is too high, I will tell you to guess lower.")
print("     - If your guess is too low, I will tell you to guess higher.")
print("     - You win if you guess the number correctly.")
print("     - You have 10 attempts to guess the number correctly.\n\n")
print("let's start the game!!")

guess_num = guess_game()    #to generate a random number for the user to guess
count = 10

while count > 0:
    user_num = int(input("enter your guess:"))

    if user_num < 1 or user_num > 50:
        print("invalid input, please enter a number between 1 and 50.")
    elif user_num == guess_num:
        print("congratulations!! you guessed the number correctly.")
        break
    elif user_num < guess_num:
        print("your guess is too low, please guess higher.")
        count -= 1
        print("you have",count,"attempts left.")
    else:
        print("your guess is too high, please guess lower.")
        count -= 1
        print("you have",count,"attempts left.")

if count == 0:
    print("you lost ,better luck next time!!")
else:
    print("thanks for playing!!")
