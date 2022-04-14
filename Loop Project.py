def count100(userchoice2):
    even = int(0)
    if userchoice2 == "even":
        while even <= 100:
            print(even)
            even += 2
    elif userchoice2 == "odd":
        for x in range(1, 100, 2):
            print(x)
    else:
        print("Incorrect")


def choiceCount(userchoice2, userchoice3, userchoice4):
    for i in range(userchoice2, userchoice3 + 1, userchoice4):
        print (i)



def choices(userchoice1):
    if userchoice1 == "choose":
        choice3 = int(input("What would you like the starting value of your loop to be? "))
        choice4 = int(input("What would you like the ending value of your loop to be? "))
        choice5 = int(input("What would you like the interval for your loop to be? "))
        choiceCount(choice3, choice4, choice5)
    elif userchoice1 == "loop":
        choice2 = str(input("Would you like an even or odd loop? ")).lower()
        count100(choice2)


choice1 = str(input("Would you like to (choose) your loop values, or do a (loop) from 0-100? ")).lower()
choices(choice1)