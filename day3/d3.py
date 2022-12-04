import os
import string

# i prefer using camel case for variables so gonna keep this consistent now
def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__)
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = []
        for line in inputFile.read().splitlines():
            parsedInput.append(line)
    return parsedInput

def containsLetter(string, letter): # ole reliable
    return letter in string

def createDictionary():
    priorityLower = dict(zip(string.ascii_lowercase, range(1,27)))
    priorityHigher = dict(zip(string.ascii_uppercase, range(27,53)))
    priorityDict = {**priorityLower, **priorityHigher} # apparently double asterisks indicate dictionaries. dunno the relevance though
    return priorityDict

def sortPacks(rawList: list):
    priorityDict = createDictionary()
    sumPriorities = 0 
    # HEY there herbe 15 lines of code from now! the issue was that I initialized the oldVal newVal variables before the for loop
    # which meant if one guy had duplicate K's and the next guy had duplicate K's the code would ignore the next guy, thinking it was duplicates from last time
    # so we have to reinitialize for every new guy's bookbag (every new item in the list)
    for i in range(len(rawList)):
        oldVal = 1 
        newVal = 0  # newVal should be 0 instead of oldVal cause oldVal will always get turned into a real index number whereas newVal needs
                    # to be definitely different at the first pass. if swapped oldVal 0 and newVal 1, if "a" was the duplicate in the first bookbag, errors.
        currentItem = rawList[i]
        splitPoint = (len(currentItem)//2)
        firstHalfPack  = currentItem[0:splitPoint]
        secondHalfPack = currentItem[splitPoint:len(currentItem)]
        for letter in secondHalfPack:
            char = letter
            if containsLetter(firstHalfPack, char) == True: # we need something that avoids repeats
               oldVal = priorityDict.get(char)
               if newVal != oldVal:
                    newVal = priorityDict.get(char) 
                    sumPriorities += newVal # I did not expect the oldVal newVal stuff to work lmao
               else:
                   sumPriorities += 0
                    # Addendum: It worked with the test cases, but not with the real input case! too low. HOW.
                    # What I did was oldVal = priorityDict.get(char), then if oldVal != newVal, make them the same and add the val to the sumPriorities
                    # It made the test cases work but not the real deal.
                    # Then I just did val = priorityDict.get(char) and add to sum, but then it made it too high, cause repeats.
        i += 1
    return sumPriorities 

def badgeFind(rawList: list):
    priorityDict = createDictionary()
    # i've seen this oneliner stuff referenced twice now on stackOverflow so i really gotta figure out why it works
    badgeGrouped = [rawList[x:x+3] for x in range(0, len(rawList), 3)]
    sumBadges = 0
    for row in badgeGrouped: # this goes row by row, doesn't require iteration at the end. can go into lists. can't do badgeGrouped[row][0]. cause row is list
        elfGroup = row
        oldVal = 1
        newVal = 0
        firstElf = elfGroup[0]
        secondElf = elfGroup[1]
        thirdElf = elfGroup[2]
        for letter in firstElf:
            char = letter
            if containsLetter(secondElf, char) and containsLetter(thirdElf, char):
                oldVal = priorityDict.get(char)
                if newVal != oldVal:
                    newVal = priorityDict.get(char)
                    sumBadges += newVal
    return sumBadges 


def main():
    parsedInput = parseInputFile("input3.txt")
    # first answer
    print("first answer:", sortPacks(parsedInput))

    #second answer
    print("second answer:", badgeFind(parsedInput))
    

if __name__ == "__main__":
    main()
