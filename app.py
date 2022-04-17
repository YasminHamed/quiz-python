#title
print("Welcome to Python Language quiz!")

#A question to increase enthusiasm
playing = input("Let's Start ????   yes/no ")
if playing != "yes" :
    quit()
print("Okay! Let's Start :)")
score = 0

#Question 1 if else
answer = input("What is a correct syntax to output 'Hello World' in Python? ")
if answer == "print('Hello World')":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question 2 if else
answer = input("How do you insert COMMENTS in one line in Python code? ")
if answer == "#":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question 3 if else
answer = input("Which one is NOT a legal variable name?(_myvar , myvar , my-var , MYVAR) ")
if answer == "my-var":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question 4 if else
answer = input("What is the correct file extension for Python files? ")
if answer == ".py":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#final result + your score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")