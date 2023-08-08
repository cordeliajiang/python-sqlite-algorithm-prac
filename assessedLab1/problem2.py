# problem2, 06/08/21, Cordelia Jiang
# Say that a "clump" in a list is a series of 2 or more adjacent elements of the same value.
# Print the number of clumps in the given list.

# ask for user input and store user input in intInput variable
intInput = input("Input: ")

# replace any " " received from input to "", turn every character in intInput to integer, and put them in a list
intList = [int(x) for x in intInput.replace(" ", "")]


# define a function that takes intList as input
def clumpFunc(_intList):
    # a variable that is used to store a 'clumped' value to stop already clumped value getting clumped again
    # e.g. inputting 1 1 1 1 1 will only get 1 for the numOfClump,
    # clumpVar will be reset once current index and next index are not the same (allowing already appeared value to be
    # clumped again as long as there is different value sit in between same values e.g. 1 1 2 1 1)
    clumpVar = None

    # a variable used for counting number of clump
    numOfClump = 0

    # go through each item in the intList
    for i in range(len(_intList)-1):
        # if the integer in current index and next index are the same
        if _intList[i] == _intList[i + 1]:
            # if current index is not clumpVar, then set value of current index to clumpVar, and add 1 to numOfClump
            if _intList[i] != clumpVar:
                clumpVar = _intList[i]
                numOfClump += 1
            else:
                pass
        # if the integer in current index and next index aren't the same, then set clumpVar to None
        else:
            clumpVar = None
    return numOfClump


# define a function that takes intList as input, to print clumpFunc's return value
def printClumpFunc(_intList):
    # while length of _intList is not 0, call clumpFunc and put its returned value in a clumpFuncOutput variable
    # and print its stored value, otherwise print The list should be length 1 or more.
    while len(_intList) != 0:
        clumpFuncOutput = clumpFunc(_intList)
        print("Output:", clumpFuncOutput)

        # read value to check whether the inputted number is sentinel
        intInput = input("Input: ")
        _intList = [int(x) for x in intInput.replace(" ", "")]
    print("The list should be length 1 or more.")


# call printClumpFunc
printClumpFunc(intList)
