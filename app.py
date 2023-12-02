import subPrograms


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
            subPrograms.displayMacros()
            break
        elif userInput == "2":
            subPrograms.predefined()
            break
        elif userInput == "3":
            subPrograms.manualEntry()
            break
        elif userInput == "4":
            subPrograms.deleteRecords()
            break
        elif userInput == "5":
            subPrograms.exitProgram()
            break
        else:
            print("Incorrect Input. Try again")


main()