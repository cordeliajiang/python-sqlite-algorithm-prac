# problem1, 05/08/21, Cordelia Jiang
# input a list of integers, print True if 6 appears as either first or last element in list.
# The list will be length of 1 or more

# ask for user input
intInput = input("Input: ")

# replace any " " received from input to "", turn every character in intInput to integer, and put them in a list
intList = [int(x) for x in intInput.replace(" ", "")]


# define a function that takes variable intList as input
def checkIntSix(_intList):
    # print True if 6 appears as either first or last element in list
    if _intList[0] == 6 or _intList[-1] == 6:
        return True
    # print False if otherwise.
    else:
        return False


# define a function that takes intList as input, to print checkIntSix function's return value
def printOutput(_intList):
    # while length of _intList is not 0, call the checkIntSix function and put its returned value in a
    # intListOutput variable and print its stored value, otherwise print The list should be length 1 or more.
    while len(_intList) != 0:
        intListOutput = checkIntSix(_intList)
        print("Output:", intListOutput)

        # read value to check whether the inputted number is sentinel
        intInput = input("Input: ")
        _intList = [int(x) for x in intInput.replace(" ", "")]
    print("The list should be length 1 or more.")


# call the printIntList function
printOutput(intList)
