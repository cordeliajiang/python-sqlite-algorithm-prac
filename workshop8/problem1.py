# problem1, 09/05/21, Cordelia Jiang
# write a function that gives a list of numbers, rotate numbers so the first number becomes
# the last, and rest numbers move one position forward until returns to the initial form.

numberInput = input("Input a list:  ")
numberList = [int(x) for x in numberInput.split()]  # split string into list, and convert list items to integers.


# rotate the numbers until returns to the initial form
def rotate_numbers(_numberInput, _numberList):
    for i in range(len(_numberList) + 1):
        firstNumber = _numberList[0]  # storing the first number before removing the first number
        print(_numberList)
        _numberList.pop(0)
        _numberList.append(firstNumber)


rotate_numbers(numberInput, numberList)
