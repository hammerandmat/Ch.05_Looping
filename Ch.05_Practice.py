#LOOPING!
import random

# for i in range(100,-1,-2):
#     print(i)

# for i in [2,6,1,7,0,9]:
#     print(i)

# for i in ("Hello World"):
#     print(i)

# total = 0
# for i in range(1,101):
#     total+=i
# print("The total is:",total)

# a = 0
# for i in range(10):
#     a+=1
#     for j in range(10):
#         a+=1
# print(a)

# for i in range(10):
#     print(i)
#
# i=0
# while i<=2**32:
#     print(i)
#     i*=1

# quit ="n"
# while quit =="n":
#     quit = input("Do you want to quit? (type y) ")
# print("Goodbye!")

# done = False
# perseverance = 0
# while not done:
#     quit = input("Do you want to quit? (type y) ")
#     if quit.lower()=="y":
#         done = True
#     else:
#         perseverance+=1
# print("Goodbye! Your perseverance level is ",perseverance)


# num = random.randint(1,100)
# done = False
# tries = 0
# while not done:
#     guess = int(input("Guess my number (1-100): "))
#     if guess == num:
#         print("You're right my number was", num)
#         tries+=1
#         done = True
#     elif guess>num:
#         print("That number is too big.")
#         tries+=1
#     else:
#         print("That number is too small.")
#         tries+=1
# print("It took you",tries,"tries to guess my number.")

# for letter in "Death Star":
#     if letter == " ":
#         break
#     print('Current letter: ',letter)

# for letter in "Death Star":
#     if letter == " ":
#         continue
#     print('Current letter: ',letter)

# var = 10
# while var > 0:
#     print("Current variable value: ", var)
#     var -= 1
#     if var == 5:
#         break

var = 0
while var <= 10:
    var += 1
    if var%2 != 0:
        
    print("Current variable value: ", var)
print("Goodbye")
