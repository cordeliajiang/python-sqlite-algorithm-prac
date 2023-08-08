# problem1, 17/05/21, Cordelia Jiang
# write a version of Adder REPL

# input sons and daughters: prompt for and allow the user to enter two values.
def varInput(_varDict, sons, daughters):
    if sons.isalpha():
        sonsInput = input("Enter a value for sons: ")
        # store sonsInput as int in varDict if sonsInput is number.
        if sonsInput.isdigit():
            _varDict[sons] = int(sonsInput)
        else:
            return
    else:
        print("Syntax error.")

    if daughters.isalpha():
        daughtersInput = input("Enter a value for daughters: ")
        # store daughtersInput as int in varDict if daughtersInput is number.
        if daughtersInput.isdigit():
            _varDict[daughters] = int(daughtersInput)
        else:
            return
    else:
        print("Syntax error.")


# print children: print the value of children.
def valPrint(_varDict, children):
    if children.isdigit():
        print("children equals" + str(_varDict[children]))
    elif children.isalpha():
        # checking whether children in dictionary
        # the last part: convert children stored in _varDict to a string and print it
        if children in _varDict:
            print("children equals " + str(_varDict[children]))
        else:
            print(children + " is undefined.")
    else:
        print("Syntax error.")


# children gets sons: variable children is assigned the value sons.
def varGetsVal(_varDict, children, sons):
    if not children.isalpha():
        print("Syntax error.")
    else:
        # checking whether children is number and in dictionary
        if children not in _varDict and sons.isdigit():
            _varDict[children] = int(sons)
        # checking whether children is alphabet and in dictionary
        elif children not in _varDict and sons.isalpha():
            if sons in _varDict:
                _varDict[children] = _varDict[sons]
            else:
                print(sons, "is undefined.")
        else:
            print("Syntax error.")


# children adds daughters: variable children has the value daughters added to it.
def varAddsVal(_varDict, children, daughters):
    if not children.isalpha():
        print("Syntax error.")
    else:
        if children not in _varDict:
            print(children + " is undefined.")
        else:
            # checking whether daughters is number
            if daughters.isdigit():
                _varDict[children] += int(daughters)
            # checking whether daughters is alphabet
            elif daughters.isalpha():
                if daughters in _varDict:
                    _varDict[children] += _varDict[daughters]
                else:
                    print(daughters, "is undefined.")
            else:
                print("Syntax error.")


print("Welcome to the Adder REPL.")
varDict = dict()

# read file and turn it into list
fileHandle = open(input("Script name: "))
lineLists = fileHandle.readlines()

# get rid of \n in list
lineLists = [x.replace("\n", "") for x in lineLists]

# newLineLists is defined for handling a lists in list. Within the for loop a single
# string item in each lists of list are separated into multiple strings, so that
# list element's position can be determined in the while loop.
newLineLists = []
for line in lineLists:
    line = line.split()
    newLineLists.append(line)


# while loop handles parsing elements into functions.
while newLineLists != "quit":
    # acting like switch statement, do specific function if condition satisfies
    if len(newLineLists[0]) == 2 and newLineLists[0][0] == "input" or \
            len(newLineLists[1]) == 2 and newLineLists[1][0] == "input":
        varInput(varDict, newLineLists[0][1], newLineLists[1][1])
    if len(newLineLists[2]) == 3 and newLineLists[2][1] == "gets":
        varGetsVal(varDict, newLineLists[2][0], newLineLists[2][2])
    if len(newLineLists[3]) == 3 and newLineLists[3][1] == "adds":
        varAddsVal(varDict, newLineLists[3][0], newLineLists[3][2])
    if len(newLineLists[4]) == 2 and newLineLists[4][0] == "print":
        valPrint(varDict, newLineLists[4][1])
    if len(newLineLists[5]) == 1 and newLineLists[5][0] == "quit":
        exit(0)  # terminate program
