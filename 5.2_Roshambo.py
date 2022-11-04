'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''

import random

done = False

win = 0
lose = 0
tie = 0

while not done:
    comnum = random.randint(1,3)
    if comnum == 1:
        comchoc = "Rock"
    elif comnum == 2:
        comchoc = "Paper"
    else:
        comchoc = "Scissors"

    print("1 for rock, 2 for paper, 3 for scissors and 4 for quit")
    userinput = int(input(""))
    if userinput == 1:
        userchoc = "Rock"
    elif userinput == 2:
        userchoc = "Paper"
    elif userinput == 3:
        userchoc = "Scissors"
    else:
        done = True
        break

    print("Your choice:", userchoc)
    print("Computer choice:", comchoc)
    if userinput == comnum:
        print("Tie")
        tie += 1
    elif userinput > comnum or userinput == 1 and comnum == 3:
        print("Win")
        win += 1
    else:
        print("Lose")
        lose += 1

print("Won",win,"time(s)")
print("Lost",lose,"time(s)")
print("Tied",tie,"time(s)")









