print ("miccru0585")

correctNumber = 5
guessCount = 0

studentName = input("What is your name? ")
studentId = input("What is your studentID? ")

print("Welcome,", studentName + "!")
print("Student ID:", studentId)

userGuess = int(input("Please guess a number between 1 and 10... "))
guessCount += 1

while userGuess != correctNumber:
    if userGuess < correctNumber:
        print("You guessed too low")
    else:
        print("You guessed too high")

    userGuess = int(input("Please guess a number between 1 and 10... "))
    guessCount += 1

print("Congratulations,", studentName + "!", "You guessed the number in", guessCount, "tries!")
print("Student ID:", studentId)
print()

print("Output from the 'While' loop:")
counter = 0
while counter < 5:
    print(correctNumber, "incremented by", counter + 1, "is", correctNumber + counter + 1)
    counter += 1

print()
print("Output from the 'for' loop:")
for counter in range(5):
    print(correctNumber, "incremented by", counter + 1, "is", correctNumber + counter + 1)
