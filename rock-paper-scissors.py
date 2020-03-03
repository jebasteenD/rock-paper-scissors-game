import random

playagain="y"

def full(x):
    if x=="r":
        return "Rock"
    elif x=="p":
        return "Paper"
    else:
        return "Scissors"

while playagain=="y":
    me = None
    computer = random.choice(['r','p','s'])
    while me == None:
        me = input('Rock(r), Paper(p), Scissors(s)?')
        print("")
        me=me.lower()
        if me not in ['r','p','s']:
            print('Please type r,s or p')
            me = None
    if me == computer:
        print('***DRAW***')
    if me == 'r':
        if computer == 'p':
            print('THE COMPUTER WINS')
        elif computer == 's':
            print('***YOU WIN!***')
    if me == 'p':
        if computer == 's':
            print('THE COMPUTER WINS')
        elif computer == 'r':
            print('***YOU WIN!***')
    if me == 's':
        if computer == 'r':
            print('THE COMPUTER WINS')
        elif computer == 'p':
            print('***YOU WIN!***')
    print("")
    print('The computer was',full(computer))
    print('You were',full(me))
    print('******************************')
    print('Do you want to play again?')
    print('Press y for Yes or any other key to leave the game.')
    playagain=input('')
    playagain=playagain.lower()
    print("")
    print("")
else:
    print('Bye!')
