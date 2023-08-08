# problem1, 26/04/21, Cordelia Jiang

# string library function is imported to use ascii_letters
import string

stringInput = input("Enter a string: ")

# while string is not empty, convert string to lower case and split to words
# print words in descending order lexicographically
while len(stringInput) != 0:
    # replace digits and symbols with space character
    # ascii_letters has alphabetical lowercase and uppercase string constants
    for character in stringInput:
        if character.isdigit() or character not in string.ascii_letters:
            stringInput = stringInput.replace(character, " ")

    words = stringInput.lower().split()
    words.sort(reverse=True)

    # join all items in a list into a string, using a space character as separator
    print(" ".join(words))
    stringInput = input("Enter a string: ")
