import random
smallest_num = 1
biggest_num = 100
secret = random.randint(smallest_num, biggest_num)
guess_count = 0

while True:
    x = input("Guess the number ")
    if x.isdigit():
        x=int(x)
        guess_count+=1
        if x==secret:
            print("correct")
            if guess_count > 10: print(f"You can do better, your guess count is {guess_count}")
            else: print(f"Your guess count is {guess_count}")
        
            break
        
        elif x > secret:
            print ("Incorrect! Too high!")
        else: 
            print ("Incorrect! Too low!") 
    else: print ("Incorrect! Not a number!") 
    

    
    