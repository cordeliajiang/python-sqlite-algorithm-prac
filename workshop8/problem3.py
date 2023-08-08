# problem3, 11/05/21, Cordelia Jiang

# function that given a list of numbers, returns True if and only if all of the
# numbers in the list form an arithmetic progression: difference between any
# two adjacent numbers in the list is the same
def arithmetic_progression(_intList):
    difference = _intList[1] - _intList[0]
    # as known number of index 1 and 0, loop check for third number and forward
    for i in range(2, len(_intList)):
        if _intList[i+1] - _intList[i] != difference:
            return False
        else:
            return True


# read a file containing space-separated numbers as test lists
fileHandle = open(input("File name:  "))
for line in fileHandle:
    intList = [int(x) for x in line.split()]  # split string into list, turn list items to integers.
    arithmeticOutcome = arithmetic_progression(intList)

    # print each list and the outcome after calling the function.
    # turn int items in intList into strings and join each item with space.
    print(" ".join(str(x) for x in intList), arithmeticOutcome)

