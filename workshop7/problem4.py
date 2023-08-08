# problem4, 05/05/21, Cordelia Jiang
# the Unix tool wc counts the numbers of characters, words and lines in a file.
# write own version of wc that prompts for the name of the file to read,
# then prints the counts.

fileHandle = open(input("File name: "))  # if doesn't work, include .txt

characterCounter = 0
wordCounter = 0
lineCounter = 0


for line in fileHandle:
    lineList = line.split()  # split string into lists
    lineCounter += 1
    wordCounter += len(lineList)  # counting list items in lists
    characterCounter += len(line) - line.count(" ")  # count char and subtract spaces

print("Character:", characterCounter)
print("Words:", wordCounter)
print("Lines:", lineCounter)


fileHandle.close()
