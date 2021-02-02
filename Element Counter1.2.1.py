import os 

# Function that counts the total amount of words in a text
def countWords():
    text = input("Insert text here: ")
    count = 1
    for i in text.strip(): # stripping the string of its blank spaces in the beginning and end to avoid counting mistakes
        if i == " ":
            count += 1
    print("Total amount of words: ", count)

# Functions that counts user-inputted elements in a text
def countElement():
    text = input("Insert text here: ")
    element = input("What element do you want to count? ")
    elementCount = text.count(element)
    print("There were a total of ",elementCount, " times it appeared in the text")

quitCondition = False # boolean that decides whether the program should return to the main menu or terminate
# Function that checks whether the quitCondition boolean should stay false or become true terminating the program
def quitChecker():
    global quitCondition
    while not quitCondition:
        resetInp = int(input("\nDo you wish to:\n1. Quit       2. Return to the start\n"))
        if resetInp == 1:
            quitCondition = True
        elif resetInp == 2:
            clear()
            break
        else:
            clear()
            print("Invalid input, please try again\n")
            quitCondition = False
            pass
        break

def clear(): 
    os.system('cls')

menuCondition = True
clear()
while menuCondition and not quitCondition:
    inp = int(input("What do you want to do?\n1. Count word amount       2. Count specific elements       3. Quit\n"))
    clear()
    if int(inp) == 1:
        countWords()
        quitChecker()
    elif int(inp) == 2:
        countElement()
        quitChecker()
    elif int(inp) == 3:
        break
    else:
        menuCondition = True
        print("Invalid input, try again ")
        pass
