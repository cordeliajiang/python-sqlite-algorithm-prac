# problem 4, 23/04/21, Cordelia Jiang
# compute total length required lengthways and widthways

from math import ceil

room_dimension1 = float(input("Enter room dimension 1 (m): "))
room_dimension2 = float(input("Enter room dimension 2 (m): "))
room_length = 0
room_width = 0
carpet_width = 3.66
printResult = False     # to make sure we only printing once in the while loop for every new inputs


# if either room_dimension1 or room_dimension2 is equal to 0 then we terminate
# out of two numbers entered, bigger number is length, and the other width
while room_dimension1 > 0 and room_dimension2 > 0:
    if room_dimension1 >= room_dimension2:
        room_length = room_dimension1
    else:
        room_length = room_dimension2

    if room_dimension1 <= room_dimension2:
        room_width = room_dimension1
    else:
        room_width = room_dimension2
    carpet_length = room_length     # carpet length is assumed to be infinite
    printResult = True

    if printResult:
        # argument of format method interpolated into output string
        # .3f means that there is 3 figures after decimal, fixed point notation
        print("Length = {:.3f}".format(room_length), "m")
        print("Width = {:.3f}".format(room_width), "m")

        # round carpet length and carpet width to next full integer
        print("Total length required lengthways = {:.0f}".format(ceil(carpet_length)), "m")
        print("Total length required widthways = {:.0f}".format(ceil(carpet_width)), "m")

        printResult = False

        room_dimension1 = float(input("Enter room dimension 1 (m): "))
        room_dimension2 = float(input("Enter room dimension 2 (m): "))
