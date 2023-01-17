import random
#Rock, Paper, Scissors
#explain game instructions
print("User enters rock, paper, or scissors, program returns rock, paper, or scissors, and if the user wins, loses, or ties")
#user enters their first move
user = input('Enter your move:')
#while user wants to keep playing
while(user != "stop"):
#computer gives a random move
    i = random.randint(0,2)

    if i == 0:
        move = "rock"
        print("computer chose rock!")
    elif i == 1:
        move = "paper"
        print("computer chose paper!")
    elif i == 2:
        move = "scissors"
        print("computer chose scissors!")

#check if user wins, loses, or ties with the computer
    if (user == "rock" and move == "paper") or (user == "paper" and move == "scissors") or (user == "scissors" and move == "rock"):
        print("you lose!")
    elif user == move:
        print("tie!")
    else:
        print("you win!")
#user enters their second move or stop
    user = input('Enter your move:')
    
