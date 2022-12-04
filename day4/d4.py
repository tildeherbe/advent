import os

def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__) #note to self find out why __file__ works
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = []
        for line in inputFile.read().splitlines():
            parsedInput.append(line)
    return parsedInput

def rangeSubset(range1, range2):
    return range1.start in range2 and range1[-1] in range2 # will have to check both ways for each pair. also this is a boolean check

def formatData(rawList: list):
    formattedList = []
    totalSubset = 0
    for item in rawList: # we need to go line by line of [2-45,31-88] and turn that into something workable to compare ranges of numbers
        fullPair = item # this looks like [2-45,31-88]
        ranges = fullPair.split(",") # ranges looks like ['2-45', '31-88']
        firstRangePair = ranges[0] # this looks like 2-45
        # for some inscrutible reason secondRangePair  worked during the test case but broke on full input. ranges[1] out of range.
        # addendum: this was because there was a sneaky new line in the full input that was empty as hell
        secondRangePair = ranges[1] # this looks like 31-88. also these are strings obviously rn. 
        firstBookends = firstRangePair.split('-')
        secondBookends = secondRangePair.split('-')
        firstS = int(firstBookends[0]) # firstS stands for first Start (firstF is first Finish et cetera) also they gotta be int not str
        firstF = int(firstBookends[1]) # these four variables (firstS - secondF) all return integers
        secondS = int(secondBookends[0])
        secondF = int(secondBookends[1])
        firstRange = range(firstS, firstF + 1) # working as intended! grabs the range, remember this variable works as a range, not a set
        secondRange = range(secondS, secondF + 1)
        # i should seperate these functions out, have it return [firstRange, secondRange], and do different things with this
        # at first i just added to the totalSubset in-house in one function
        formattedList.append([firstRange,secondRange]) # can't append two at a time
    return formattedList 

        
def totalSubset(rangeList: list):
    totalSubset = 0
    for item in rangeList:
        rangePair = item
        firstRange = rangePair[0]
        secondRange = rangePair[1]
        if rangeSubset(firstRange, secondRange) == True or rangeSubset(secondRange, firstRange) == True:
            totalSubset += 1
    return totalSubset

def anyOverlap(rangeList: list):
    total = 0 # this counts by one for each pair of elves that has any shared value at all in both of their ranges
    for item in rangeList:
        rangePair = item
        firstRange = rangePair[0] # we can find the beginnings and ends of ranges by indexing into them like a list
        secondRange = rangePair[1]
        # i wonder if there's a better way to check if there's any overlap between ranges, but this worked great for me
        if firstRange[0] in secondRange or firstRange[-1] in secondRange or secondRange[0] in firstRange or secondRange[-1] in firstRange:
            total += 1
    return total

def main():
    parsedInput = parseInputFile("input4.txt")
    rangeList = formatData(parsedInput)
    print("first answer is:", totalSubset(rangeList))
    print("second answer is:", anyOverlap(rangeList))

if __name__ == "__main__":
    main()

