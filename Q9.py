import random
random_number=random.randint(1,50)
guess=1
while guess!=random_number:
    guess=int(input("Guess number between 1 to 50: "))
    if guess==random_number:
        print("your guess is correct")
    elif guess < random_number:
        print("guess is smaller")
    else:
        print("your guess is larger")