import random

def guess(num):
    random_num=random.randint(1,num)
    guess=0
    while guess!=random_num:
        guess=int(input(f'Guess a number between 1 and {num}: '))
        if guess<random_num:
            print('The number is low. Try again.')
        elif guess>random_num:
            print('The number is high. Try again.')

    print(f'You have guessed the correct number {random_num}')


guess(20)