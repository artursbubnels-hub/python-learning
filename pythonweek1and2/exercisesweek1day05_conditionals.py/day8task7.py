computer_move = input('Choose rock paper or scissors ')
my_move = input('Choose rock paper or scissors ')
if my_move == computer_move:
    print("draw")
elif my_move == "rock" and computer_move == "scissors":
    print('user wins')
elif my_move == "paper" and computer_move == "rock":
    print('user wins')
elif my_move == "scissors" and computer_move == "paper":
    print("user win")
else:
    print('user loses')
