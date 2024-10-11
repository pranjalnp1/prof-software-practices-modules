import random

n_min = 1
n_max = 100
n_rand = random.randint(n_min, n_max)

i =1
Continue = 1

while Continue == 1:
    guess = input("please enter a guess number")

    if (guess > 100 or guess < 1) or guess.isdigit == False:
        print("your guess is out of bounds or the input is not an integer")
    else:
        if guess == n_rand:
            print("you guessed the number in " + str(i) + " attempts")
            Continue +=1
        else: 
            if guess > n_rand:
                print("too high")
            else: 
                print("too low")
            i +=1

