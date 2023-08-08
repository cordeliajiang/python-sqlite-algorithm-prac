# problem3, 07/08/21, Cordelia Jiang
# write a program that reads the file phillip.txt,
# counts the number of words in the file, and prints out the count.

# read all lines in file phillips.txt, and split string into a list of strings (words)
readPhillipTxt = open("phillip.txt").read()
words = readPhillipTxt.split()


# define a function to count number of words in phillip.txt
def countNumOfWords():
    # initially set word counter to 0
    wordCnt = 0
    alphabetList = []

    # go through each item in words list, check if all the characters in strings are alphabet letters,
    # increase word counter by 1 if all characters in one string are alphabet letters, otherwise do a pass
    for i in range(len(words)):
        if words[i].isalpha():
            wordCnt += 1
            alphabetList.append(words[i])
        else:
            pass

    # return the word count for printing
    return wordCnt


# call countNumOfWords function and put its returned value in a variable numOfWords, and print its stored value
numOfWords = countNumOfWords()
print("Number of words: ", numOfWords)

