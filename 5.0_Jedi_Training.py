  #Sign your name:Matthew
import random
'''
 1. Make the following program work.
   '''

# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total = total + x
# print("The total is:", total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

# for i in range(1,51):
#     i*=2
#     print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

# countdown = False
# num=11
# while not countdown:
#     num-=1
#     print(num)
#     if num == 0:
#         countdown = True
# print("Blast off!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

# print(random.randint(1,10))

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

total = 0
positive = 0
negative = 0
zero = 0
for i in range(7):
    num=(int(input("Input a number: ")))
    total= total+num
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        zero+=1
print("The sum of your numbers is",total)
if positive == 1:
    print("There was",positive,"positive number.")
else:
    print("There were",positive,"positive numbers.")
if negative == 1:
    print("There was",negative,"negative number.")
else:
    print("There were",negative,"negative numbers.")
if zero == 1:
    print("There was",zero, "zero.")
else:
    print("There were",zero,"zeros.")
#test


