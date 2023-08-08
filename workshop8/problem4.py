# problem4, 11/05/21, Cordelia Jiang

# given two lists, write a function that merges two lists in descending order
# merge by concatenating two lists into a new list and manually sort
def merge_list_descending(_list1, _list2):
    outputList = _list1 + _list2

    # go through all list items
    for i in range(len(outputList)):
        # as last item already in place after first pass, so no need to re-check
        for j in range(len(outputList)-i-1):
            # swap place if item in current position is greater than next
            if outputList[j] < outputList[j+1]:
                outputList[j], outputList[j+1] = outputList[j+1], outputList[j]
    print(outputList)


# main program allow user enter two lists of numbers, and end input with blank
# line for list 1
listInput1 = input("List 1: ")
list1 = [int(x) for x in listInput1.split()]  # split string into list, and convert list items to integers.


while len(list1) > 0:
    listInput2 = input("List 2: ")
    list2 = [int(x) for x in listInput2.split()]

    merge_list_descending(list1, list2)

    listInput1 = input("List 1: ")  # read value to check whether the inputted number is sentinel
    list1 = [int(x) for x in listInput1.split()]
