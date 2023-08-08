# problem1, 15/05/21, Cordelia Jiang
# write a version of Adder REPL

# input var: prompt for and allow the user to enter a value for the variable named var.
# var is always a variable name containing only letters (no symbols)
def varInput(_varDict, var):
    if var.isalpha():
        varInput = input("Enter a value for " + var + ": ")
        # store varInput as int in varDict if varInput is number.
        if varInput.isdigit():
            _varDict[var] = int(varInput)
        else:
            print("Syntax error.")
    else:
        print("Syntax error.")


# print val: print the value val.
# val can be either a variable name containing only letters or a int number containing
# only digits.
def valPrint(_varDict, val):
    if val.isdigit():
        print(val)
    elif val.isalpha():
        # checking whether val in dictionary
        # the last part: convert value stored in _varDict to a string and print it
        if val in _varDict:
            print(val + " equals " + str(_varDict[val]))
        else:
            print(val + " is undefined.")
    else:
        print("Syntax error.")


# var gets val: variable var is assigned the value val.
def varGetsVal(_varDict, var, val):
    if not var.isalpha():
        print("Syntax error.")
    else:
        # checking whether var is number and in dictionary
        if var not in _varDict and val.isdigit():
            _varDict[var] = int(val)
        # checking whether var is alphabet and in dictionary
        elif var not in _varDict and val.isalpha():
            if val in _varDict:
                _varDict[var] = _varDict[val]
            else:
                print(val, "is undefined.")
        else:
            print("Syntax error.")


# var adds val: variable var has the value val added to it.
def varAddsVal(_varDict, var, val):
    if not var.isalpha():
        print("Syntax error.")
    else:
        if var not in _varDict:
            print(var + " is undefined.")
        else:
            # checking whether val is number
            if val.isdigit():
                _varDict[var] += int(val)
            # checking whether val is alphabet
            elif val.isalpha():
                if val in _varDict:
                    _varDict[var] += _varDict[val]
                else:
                    print(val, "is undefined.")
            else:
                print("Syntax error.")


print("Welcome to the Adder REPL.")
varDict = dict()


# use sentinel pattern continue to prompt the user to give one of the four commands
# below, until user give quit command.
# quit: exit the REPL or terminate a program.
commandInput = input("??? ")
while commandInput != "quit":
    commandSplit = commandInput.split()
    # acting like switch statement, do specific function if condition satisfies
    if len(commandSplit) == 2 and commandSplit[0] == "input":
        varInput(varDict, commandSplit[1])
    elif len(commandSplit) == 2 and commandSplit[0] == "print":
        valPrint(varDict, commandSplit[1])
    elif len(commandSplit) == 3 and commandSplit[1] == "gets":
        varGetsVal(varDict, commandSplit[0], commandSplit[2])
    elif len(commandSplit) == 3 and commandSplit[1] == "adds":
        varAddsVal(varDict, commandSplit[0], commandSplit[2])
    else:
        print("Syntax error.")
    commandInput = input("??? ")  # refresh of sentinel pattern
print("Goodbye.")
