# problem2, 10/05/21, Cordelia Jiang

# function that takes these two lists as the input arguments and returns the
# list of all the elements in the first list that occur in the second list.
def first_occur_in_second(_list1, _list2):
    outputList = []

    for x in _list1:
        if x in _list2 and x not in outputList:  # if not duplicate, append to outputList
            outputList.append(x)

    return outputList


# allow user enter two lists of number
# end input with a blank line for list1, while loop will terminate when there
# is 0 items in list1.
listInput1 = input("List 1: ")
list1 = [int(x) for x in listInput1.split()]  # split string into list, and convert list items to integers.

while len(list1) > 0:
    listInput2 = input("List 2: ")
    list2 = [int(x) for x in listInput2.split()]

    outputList = first_occur_in_second(list1, list2)
    print(outputList)

    listInput1 = input("List 1: ")  # read value to check whether the inputted number is sentinel
    list1 = [int(x) for x in listInput1.split()]
