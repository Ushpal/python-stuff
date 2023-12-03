print("Welcome to my computer quize!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("okey! Let's Play:)")
score=0


answer= input("what does CPU means?\n")
if answer=="Central Processing Unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer= input("what does GPU means?\n")
if answer=="graphics Processing Unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer= input("what does RAM means?\n")
if answer=="Random Access Memory":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer= input("what does ROM means?\n")
if answer=="Read Only Memory":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer= input("what does DOM means?\n")
if answer=="Data Object Module":
    print("correct")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score)+ " questions correct!")
print("You got " + str((score/4)*100) + "%.")










