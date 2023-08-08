# problem4, 07/08/21, Cordelia Jiang
# Write a function that given a list length 1 or more of integers, print the difference
# between the largest and smallest values in the list.

# ask for user input and store user input in intInput variable
intInput = input("Input: ")

# split a string into a list of strings separated by white space, and turn items into integers
intList = [int(x) for x in intInput.split()]


# define a function that takes intList as input, calculates the difference between the largest and smallest integers
def calcDifference(_intList):
    # while length of _intList is not 0, do max and min function on _intList to get the largest and smallest integer
    # in _intList, and store the difference between largest and smallest in difference variable, print the difference.
    # if the list contains 0 items, then print "a list should contain 1 or more integers."
    while len(_intList) != 0:
        largestInt = max(_intList)
        smallestInt = min(_intList)
        difference = largestInt - smallestInt
        print("Output:", difference)

        # read value to check whether the inputted number is sentinel
        intInput = input("Input: ")
        _intList = [int(x) for x in intInput.split()]
    print("a list should contain 1 or more integers.")


# call calcDifference function
calcDifference(intList)
