import random
secret=random.randint(1,10)
attempt=1
while attempt<=3:
    guess_number=int(input(" guess the number: "))
    if guess_number<secret:
        print(" it is a small")
    elif guess_number>secret:
        print("it is a large number")
    else:
        print('you guess correct number')
        break
    attempt+=1
else:
    print(f'the guess_number was {secret}')
