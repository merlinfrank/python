import random
count = 0
win = False
number = random.randint(1,30)
while win == False:
    guess = int(input('Enter your number: '))
    if guess != number:
        if guess >= number:
            print('try a lower number')
            count += 1
            print(count)
            if count == 5:
                print('you used so much guesess')
                break
        elif guess <= number:
            print('try a higher number')
            count += 1
            print(count)
            if count == 5:
                print('you used so much guesess')
                break
    elif guess == number:
        print('WOW, you won!')
        break