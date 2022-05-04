gameSwitch = True
total = 0

while gameSwitch is True:
    letter_dict = {}
    userInput = str(
        input("Please input a string to receive the number of each letter inside of it(To quit input 5): "))
    if userInput == str(5):
        gameSwitch = False
    for letter in userInput:
        total += 1
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] = letter_dict[letter] + 1
    print(letter_dict)
    print(f'String reversed: {userInput[::-1]}')
    print(f"Total is: {total}")
    total = 0
# reverse and count total characters
