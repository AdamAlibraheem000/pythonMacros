import subPrograms, sys

def displayMacros():
    readData()

def predefined():
    with open("food.csv", "r") as file:
        for item in file:
            print(item)

def manualEntry():
    print("Manual")

def readData():
    with open("data.csv", "r") as file:
        for item in file:
            print(item)
    

def exitProgram():
    while True:
        userInput = input("Exit Program? (y/n): ")
        userInput = userInput.lower()
        if userInput == 'y':
            print("buh-bye")
            sys.exit()
        elif userInput == 'n':
            main()
            break
        else:
            print("Wrong input. Try again")



def deleteRecords():
    print("Delete")

def main():

    print("*****MACROS PROGRAM********")

    while True:
        print("1)Display Macros")
        print("2)Pre-defined list")
        print("3)Manual Entry")
        print("4)Delete Records")
        print("5)Exit Program")

        userInput = input("> ")

        if userInput == "1":
            displayMacros()
            break
        elif userInput == "2":
            predefined()
            break
        elif userInput == "3":
            manualEntry()
            break
        elif userInput == "4":
            deleteRecords()
            break
        elif userInput == "5":
            exitProgram()
            break
        else:
            print("Incorrect Input. Try again")


main()