# Exercise 3: Kon banega Crorepati
# Create a program capable of displaying questions to the user
# Use list data type to store questions and their correct answers
# Display the final amount the user is taking home after playing the game

# I created this first instance of the game using only if statements and no loops, and I dont like it
# print("*Welcome to Kon Banega Crorepati \nI'm your host, **Amitabh BACHAN** *")
# print("*Today, we have upon ourselves a guest, who will test their knowledge and win rewards*")
# print("*Please, would you like to introduce yourself?*\n")

# plrName = input("What is your name: ")
# print(plrName)

# print("*Alright, then lets get started with the game*\n")
# questionsList = ["What does SRK stand for?", "Who played the role of the father in \'Kabhi Khushi Kabhi Gham\'", "How tall is Amitabh Bachan?", "What is the name of Amitabh Bachan's son?"]

# print("Here's your first question: ", questionsList[0])

# choice1 = ["a: Shah Rukh Khan", "b: Samosa Roti Kabab", "c: Salman Rukh Khan"]
# print("Answers: ", choice1)
# answer1 = input("What is your answer: \n")

# if (answer1 == "a"):
#     print("Correct Answer")
#     print("You have cleared the first question, your prize is $500.\n")

#     print("Now lets move onto our next question.\n")
#     print("Here's your second question: ", questionsList[1])

#     choice2 = ["a: Salman Khan", "b: Abhishek Bachan", "c: Amitabh Bachan"]
#     print("Answers: ", choice2)
#     answer2 = input("What is your answer: ")

#     if (answer2 == "c"):
#         print("Correct Answer")
#         print("You have cleared the second question, your prize is $1500.")

#         print("Now lets move onto the last question. \n")
#         print("Here's your third and last question: ", questionsList[2])

#         choice3 = ["a: 5 Ft 8 inches", "b: 6 Ft 2 inches", "c: 6 Ft 5 inches"]
#         print("Answers: ", choice3)
#         answer3 = input("What is your answer: ")

#         if (answer3 == "b"):
#             print("Correct answer.")
#             print("You have cleared the final question, your prize is $3000\n")

#             print("You have competed excellently, and have won a total prize of $5000.")
#             print("First Round: $500\n" \
#             "Second Round: $1500\n" \
#             "Third Round: $3000\n" \
#             "Total: $5000\n" \
#             "" \
#             "We want to give you our heartfelt congratulations.\n")
#         else:
#             print("Too bad, you answered that wrong. See you next time.")
#     else: 
#         print("Wrong Answer. Better luck next time.")

# else:
#     print("Wrong answer")
#     print("You have lost the game, see you next time.")

# print("Alright folks, that was the game Kon Banega Crorepati, with our guest", plrName,".We will see you next time.")


print("Welcome to KON BANEGA CROREPATI with your lovely host AMITABH BACHCHAN 🙏🙏🙏🙏")
print("Today we are welcoming a new guest on the show. We'll see if they win a fortune or return home empty handed.")
print("So lets get started.\n")

guestName = input("What is your name: \n")

questionsList = ["What does SRK stand for?", "Who played the role of the father in \'Kabhi Khushi Kabhi Gham\'", "How tall is Amitabh Bachan?", "What is the name of Amitabh Bachan's son?"]
choice1 = ["a: Shah Rukh Khan", "b: Samosa Roti Kabab", "c: Salman Rukh Khan"]
choice2 = ["a: Abishek Bachchan", "b: Amitabh Bachchan", "c: Ajay Devgan"]
choice3 = ["a: 5 ft 2 inches", "b: 6 ft 5 inches", "c: 6 ft 2 inches"]
totalRewards = 0
reward1 = 500
reward2 = 1500
reward3 = 3000
def balance():
    print("Your balance: ", totalRewards)

answerOneDone = False
answerTwoDone = False
answerThreeDone = False

while (answerOneDone == False):
    print("\nFirst Question: ", questionsList[0])
    print("Answers: ", choice1)
    answer1 = input("What is your answer: ")

    if (answer1 == "a"):
        print("Correct answer. \n")
        print("Your reward balance is: ", totalRewards)
        print("As you have answered correctly, your balance is now: ")
        totalRewards = totalRewards + reward1
        balance()

        answerOneDone = True
    else:
        print("Wrong answer, you will be rewarded nothing.")
        answerOneDone = True
        balance()

print("\nMoving onto the next question.")

while (answerTwoDone == False):
    print("\nSecond Question: ", questionsList[1])
    print("Answers: ", choice2)
    answer2 = input("What is your answer: ")

    if (answer2 == "b"):
        print("Correct answer. \n")
        print("You got rewarded $1500 for correctly answering. Your balance is now: ")
        totalRewards = totalRewards + reward2
        balance()

        answerTwoDone = True
    else:
        print("Your answer was incorrect. You got no reward for that.")
        answerTwoDone = True
        balance()

print("\nAlright, moving to the third and last question.\n")

while (answerThreeDone == False):
    print("Third Question: ", questionsList[2])
    print("Answers: ", choice3)
    answer3 = input("What is your answer: ")

    if (answer3 == "c"):
        print("Correct answer. \n")
        print("You got rewarded $3000 for correctly answering. Your balance is now: ")
        totalRewards = totalRewards + reward3
        balance()

        answerThreeDone = True
    else: 
        print("Too bad, your answer was wrong. No reward given.")
        answerThreeDone = True
        balance()

print("Alright folks, that was the game. Hope you enjoyed.")

