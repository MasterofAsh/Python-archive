# Exercise 4: Secret Code Language
"""Rules for converting english words into secret code words
Coding:
1. If the word contains 3 or less than 3 characters, simply reverse it.
Example: Sky -> ykS
2. If the word contains more than 3 characters, then take the first letter of the word and place it
at the end. Then add 3 random words at the end and start of the same word.
Example: abdullah -> bdullaha -> tfgbdullahaplq

Decoding:
1. If the word contains 3 or less than 3 characters, reverse it to get the english word.
Example: ykS -> Sky
2. If the word contains more than 3 characters, then remove the 3 characters at the end and start
of the secret word. Finally, take the last letter of the word and place it at the start.
Example: tfgbdullahaplq -> bdullaha -> abdullah
"""
import random
import string

# Functions: 
def secrWord():
    charPool = string.ascii_letters
    randLetters = "".join(random.choices(charPool, k = 3)) # Using string and random modules to randomly create 3 string characters and store them

    while True:
        userInput = input("\nWhat do you want to do: \n" \
        "Code\n" \
        "Decode\n" \
        "Quit\n" \
        "Please choose an option: ")

        if (userInput == "Code"):
            engWord = input("Enter the word/phrase/sentence you want to CODE: ")

            if (len(engWord) <= 3):
                myList = list(engWord)

                myList.reverse() # Reversing the word back to make it secret
                engWord = "".join(myList)

                print("Secret Word: ", engWord)
            else:
                myList = list(engWord)
                firstLetter = myList[0]

                myList.append(firstLetter) # Appends the first letter of the chosen word to the end of it
                print("\nAdding the first letter to the end.")

                myList.pop(0)
                print("Removing the first letter\n", myList)

                myList.append(randLetters) # Joins the random letters at the end of the word
                print("Adding 3 random words to the end of the word.")
                myList.insert(0, randLetters) # Joins the random letters at the end of the word
                print("Adding 3 random words to the start of the word.\n", myList)

                secretWord = "".join(myList) # Finally converts the list back into a readable string.
                print("\nPresenting the secret word: ", secretWord)
                
        elif (userInput == "Decode"):
            secretWord = input("What is the word/phrase/sentence you want to DECODE: ")
            if (len(secretWord) <= 3):
                myList = list(secretWord)

                myList.reverse()
                print(myList)

                engWord = "".join(myList)
                print("Decoded word: ", engWord)

            else:
                myList = list(secretWord) # Converts the string back into a list

                for x in range(1, 4): # Using a loop to delete the end and beginning 3 random letters 
                    myList.pop()
                    myList.pop(0)

                print("\n\nRemoving the first 3 random letters and the last 3 random letters.")
                print(myList)

                firstLetter = myList[-1]
                print(myList[-1])
                myList.insert(0, firstLetter) # Joining back the first letter stored in a variable
                myList.pop()

                engWord = "".join(myList)
                print("Adding back the first letter of the original word.\n")
                print("Decoding the word back to original: ", engWord)
        else:
            print("All right, quitting the program. See you.")
            break

secrWord()