import random



def diceRoller(diceRolled):
    numOnes = 0
    totalHit = 0
    print("Rolling " + str(diceRolled) + " dice")
    for roll in range(diceRolled):
        value = random.randint(1, 6)
        print(value)
        if value >= 5:
            totalHit += 1
        if value == 1:
            numOnes+=1
    if numOnes > diceRolled/2:
        if totalHit == 0:
            print("CRITICAL GLITCH!")
        else:
            print("Glitch!")

    return totalHit

numDice = int(input("Enter the number of d6 you want to roll: \n"))

totalHitVal = diceRoller(numDice)

printVal = "You hit " + str(totalHitVal) + "!"

print(printVal)


while True:
    newHits = totalHitVal
    edgeCheck = input("Want to roll consume edge to re-roll? Y/N \n")
    if edgeCheck == "Y" or edgeCheck =="y":
        newHits = diceRoller(numDice-newHits)
        totalHitVal += newHits
        print("New total hits = " + str(totalHitVal))
    else:
        print("No re-roll requested! Total hits = " + str(totalHitVal))
        break


