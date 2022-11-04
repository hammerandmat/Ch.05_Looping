'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
print("\033[1:0m")
print("Welcome to the Camel Game!")
print()
print("In this game your goal is to get 200 miles across the desert to escape the natives.")
print("You will have you watch your thirst, camel tiredness, and how close the natives are")
print("to get across the desert. If your thirst gets above 6 you will die. If your camel's")
print("tiredness gets above 8 your camel will die, and you can't escape natives without a")
print("camel. You can check your status anytime by pressing E. Ahead a moderate speed will")
print("move you ahead 5-12 miles and add 1 to camel tiredness. Meanwhile ahead full speed will")
print("move you ahead 10-20 miles but, add 1-3 to camel tiredness. Stopping for the night will")
print("completely rest your camel, but remember the natives never rest. The drinks in your")
print("canteen are limited, so unless you get lucky and happen upon an oasis that is all the")
print("drinks you will have for your entire journey, so don't waste them.")
print("Good Luck, and have fun!")
print()

done = False

milesTraveled = 0
thirst = 0
camelTired = 0
nativeTraveled = -20
drinkInCanteen = 5
lucky = 0
unlucky = 0

while not done:
    if lucky == 1:
        print("\033[1:32m")
        print("You found a oasis!")
        print("Your canteen was refilled.")
        print("You are no longer thirsty.")
        print("Your camel is well rested.")
        drinkInCanteen = 5
        thirst = 0
        camelTired = 0
        lucky = 0

    if unlucky == 1:
        print("\033[1:33m")
        print("You got stuck in a sandstorm.")
        print("The natives were able to advance while you were stuck.")
        print("You became more thirsty.")
        print("Your camel got more tired.")
        nativeTraveled += random.randint(7, 14)
        thirst += 1
        camelTired += random.randint(1, 3)
        unlucky = 0
        if thirst >= 4 and thirst < 6:
            print("You are thirsty.")
        if camelTired >= 5 and camelTired < 8:
            print("Your camel in getting tired.")
    print("\033[1:0m")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print("\033[1:0m")
    userinput = str(input("What would you like to do? "))
    if userinput.lower() == "a" and drinkInCanteen == 0:
        print("\033[1:33m")
        print("You have no drinks in your canteen.")
    elif userinput.lower() == "a" and drinkInCanteen > 0:
        thirst = 0
        drinkInCanteen -= 1
    elif userinput.lower() == "b":
        num = random.randint(5, 12)
        milesTraveled += num
        print("\033[1:32m")
        print("You moved", num, "miles.")
        camelTired += 1
        thirst += 1
        nativeTraveled += random.randint(7, 14)
        lucky = random.randint(1, 20)
        unlucky = random.randint(1, 20)
    elif userinput.lower() == "c":
        num = random.randint(10, 20)
        milesTraveled += num
        print("\033[1:32m")
        print("You moved", num, "miles.")
        camelTired += random.randint(1, 3)
        thirst += 1
        nativeTraveled += random.randint(7, 14)
        lucky = random.randint(1, 20)
        unlucky = random.randint(1, 10)
    elif userinput.lower() == "d":
        camelTired = 0
        print("\033[1:32m")
        print("Your camel in happy.")
        nativeTraveled += random.randint(7, 14)
    elif userinput.lower() == "q":
        print("\033[1:32m")
        print("Thanks for playing!")
        done = True
        break
    else:
        print("\033[1:0m")
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", drinkInCanteen)
        print("Thirst:", thirst)
        print("Camel tiredness", camelTired)
        print("The natives are", milesTraveled - nativeTraveled, "miles behind you.")

    if milesTraveled >=200:
        print("\033[1:32m")
        print("You Win!")
        done = True
        break

    if not done and thirst >= 4 and thirst < 6:
        print("\033[1:33m")
        print("You are thirsty.")
    elif not done and thirst >= 6:
        print("\033[1:31m")
        print("You died of thirst.")
        print("Game Over!")
        done = True
        break

    if not done and camelTired >= 5 and camelTired < 8:
        print("\033[1:33m")
        print("Your camel in getting tired.")
    elif not done and camelTired >= 8:
        print("\033[1:31m")
        print("Your camel is dead.")
        print("Game Over!")
        done = True
        break

    if not done and nativeTraveled == milesTraveled:
        print("\033[1:31m")
        print("You have been caught by the natives.")
        print("Game Over!")
        done = True
        break
    elif not done and milesTraveled - nativeTraveled <= 15:
        print("\033[1:33m")
        print("The natives are getting close!")
