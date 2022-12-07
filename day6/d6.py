import os

def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__) # __file__ is whatever pathway the file's currently in. guess thats why currentDir/.dirname works
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = ""
        for line in inputFile.read().splitlines():
            parsedInput = line
    return parsedInput

# ok so we are dealing with one huge fucking string. we can index into a string no problem. :P 

def findStart(data: str):
    firstMarker = 0
    firstMessage = 0
    found = False
    foundMessage = False
    for i in range(0, len(data)-4): # since we gotta slice four at a time, i represents beginning of each slice) 
        check = data[i:i+4]
        checkMessage = data[i:i+14]
        if len(set(check)) == len(check) and found == False: # the set thing is clever cause turning a string into a set will not repeat any character
            found = True
            firstMarker = i + 4 
            print("first marker at:", firstMarker)
            # so when the conditions are met, i will be the first character in the start-packet
            # need to add 1 because it starts indexed at 0, and then add 4 to satisfy that the full packet has come in, so i + 5
            # ok this did not work :^) maybe it's just to add 4 to get to the end of the packet. said it was too high.
            # yup! only needed to add 4 to get to the end of the packet. 
        if len(set(checkMessage)) == len(checkMessage) and foundMessage == False:
            foundMessage = True
            firstMessage = i + 14
            print("first message at:", firstMessage)
        i += 1

def main():
    parsedInput = parseInputFile("input6.txt")
    findStart(parsedInput)

if __name__ == "__main__":
    main()

