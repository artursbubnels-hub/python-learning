secret= 42
guess_count= 1
guess = int(input('guess the number '))
while guess != secret:
    guess_count += 1
    if guess > secret:
        guess = int(input('too high, guess the number '))
    elif guess < secret:
        guess = int(input('too low, guess the number '))        
else:
    print('you win')
    print(guess_count)
