# problem2, 27/04/21, Cordelia Jiang
# sum the first and the last integers in two lists, print the larger sum. In the event of
# tie, print Same, When only one integer in the list, the sum is the integer itself.
listInput1 = input("List 1: ")
listInput2 = input("List 2: ")

list1 = listInput1.split()      # split string into a list where each word is a list item
list2 = listInput2.split()


# sum is the integer itself if there is only one integer in list, else the sum
# is the first item plus last item in a string, convert list items into integers
if len(list1) == 1:
    sum1 = int(list1[0])
else:
    sum1 = int(list1[0]) + int(list1[-1])
if len(list2) == 1:
    sum2 = int(list2[0])
else:
    sum2 = int(list2[0]) + int(list2[-1])


if int(sum1) > int(sum2):
    print("Output:", int(sum1))
elif sum1 == sum2:
    print("Output: Same")
else:
    print("Output:", int(sum2))

