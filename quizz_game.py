print("Welcome to my Computer Quizz!")
playing = input(" Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("okay! Let's Play:)")
Score = 0
answer = input("What does CPU stand for? ")
if answer.lower() != "central processing unit":
    print("correct!")
    Score +=1
else:
    print('INCorrect!')
answer = input("What does GPU stands For? ")
if answer.lower() == "graphics processing unit ":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit ":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")
answer = input("how many input devices? ")
if answer.lower() == "five ":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")

print("you got " + str(Score) + " questions correct!")
print("you got " + str((Score / 5) * 100) + "%.")


