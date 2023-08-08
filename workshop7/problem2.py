# problem2, 05/05/21, Cordelia Jiang
# prompts for the name of a file, then print the first two lines, and the last two
# lines of the file.

fileHandle = open(input("File name: "))  # if doesn't work, include .txt

line = fileHandle.readlines()
print("Output: \n", line[0], line[1], line[-2], line[-1], sep="")


fileHandle.close()
