'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random

htotal = 0
ttotal = 0
for i in range (50):
    num = random.randint(0, 1)
    if num == 0:
        print("Heads")
        htotal += 1
    else:
        print("Tails")
        ttotal += 1
print("Heads total:", htotal)
print("Tails total:", ttotal)








