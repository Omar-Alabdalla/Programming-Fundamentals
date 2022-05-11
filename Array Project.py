# Arrays in python are Lists
# There are 4 types of lists
# The first is of course a list
# The syntax for a list is List_Name = [variables]
# Lists are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# The second is a Tuple
# The syntax for a tuple is Tuple_Name = (Variables)
# Tuples are a collection which is ordered and unchangeable.
# The third is a Set
# The syntax for a set is Set_Name = {Variables}
# A set is a collection which is unordered, unchangeable, and unindexed
# The last type are Dictionaries
# A dictionary is a collection which is ordered, changeable, and do not allow duplicates.
# The syntax for a dictionary is Dictionary_Name = {
# "Variable name": Variable_Value
# }

choice = True
PersonList = []


def createDictionary(FirstName, LastName, Age, Height, PhoneNumber):
    DictName = {
        "FirstName": FirstName,
        "LastName": LastName,
        "Age": Age,
        "height": Height,
        "PhoneNumber": PhoneNumber
    }
    return DictName


PersonList.append(createDictionary("Omar", "Alabdalla", "17", "510", "1351241243"))
PersonList.append(createDictionary("Eli", "Maffry", "18", '''6'9"''', "9133336858"))
PersonList.append(createDictionary("Monish", "Chittampalli", "18", "510", "9132307340"))

while choice is True:

    userInput = str(input(
        "Please input (1) if you would like to create a new list or (2) if you would like to view the created ones "
        "\nYou can also input (3) if you want to search for a specific list "))

    if userInput == str(1):
        firstName = str(input("Please input your first name "))
        lastName = str(input("Please input your last Name "))
        age = str(input("Please input your age "))
        height = str(input("Please input your height "))
        phoneNumber = str(input("Please input your phone number "))
        PersonList.append(createDictionary(firstName, lastName, age, height, phoneNumber))

        for i in PersonList:
            print(i)
    elif userInput == str(2):
        for i in PersonList:
            print(f"\n`{i} \n")
    elif userInput == str(3):
        aInput = str(input("Please input some variable from the list to see the whole thing "))
        print("\n")
        for i in PersonList:
            if aInput in i.values():
                print(i)
