# problem3, 05/05/21, Cordelia Jiang
# prompts for the name of a file containing numbers in each line, prints the average
# of each line. Assume each line contains numbers only and they are separated by spaces.

lineCounter = 0

fileHandle = open(input("File name: "))  # if doesn't work, include .txt


# convert each line to list items, and convert list items to float
# prints average of each line in the file
for line in fileHandle:
    floatList = [float(x) for x in line.split()]
    avgForLine = sum(floatList) / len(floatList)

    lineCounter += 1
    print("The average of line", lineCounter, "is", avgForLine)


fileHandle.close()
