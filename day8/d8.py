import os

def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__) 
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = []
        for line in inputFile.read().splitlines():
            parsedInput.append(line)
    return parsedInput

# at first i had a function here to count all the trees on the outline and then treat them different than the inner trees
# turned it into figuring out how many trees altogether there are so we can subtract the invisible trees from the total
def treeAll(rawGrid: list):
    rowsCount = len(rawGrid) # how many rows there are in the trees. 
    columnsCount = len(rawGrid[0]) # how many trees per row -- maybe this is useful somewhere
    # columnsCount takes the trees all along the top edge and counts them for top and bottom edges
    # rowsCount, minus the already counted top and bottom rows, times the two trees on each edge of the row, at the beginning and end of each row item
    treeTotal = rowsCount*columnsCount
    return treeTotal

def innerTree(rawGrid: list):
    treeTotal = int(treeAll(rawGrid)) # it SHOULD be an integer already but just in case.
    invisibleCount = 0

    for i in range(1, (len(rawGrid)-1)): # the range of all the rows between topmost and bottommost
        innerRow = rawGrid[i] # this is takin this babey row by row

            
        # from the documentation I've seen, the "stop" in the range should be non-inclusive.
        # but this range is successful in the test, the length is 5, and eachTree prints the middle 3 numbers... the second, third, fourth
        # if len(innerRow)-1 was noninclusive here, we would only see the leftmost middle two numbers, yeah? not the fourth one.
        # maybe it's different in for loops somehow.
        # OH I think i got it! We're using t to find the index, the length of a test string would be 5 but the index would be 0,1,2,3,4.
        # So len-1 would be 4, and not including 4 means that the last reported value is indexed at 3. It's a quirk of the length vs index thing.
        for t in range(1, (len(innerRow)-1)): # t for each tree at a time that we are checking

            # reset all these to False for each tree. if they get set to True then they're blocking the viewpoint from that specific angle
            # if all of these are True, then the tree is invisible.
            # ... hm. could we perchance just take the entire grid's treecount and then subtract the invisible ones?
            leftTall = False
            rightTall = False
            upTall = False
            downTall = False 
            
            eachTree = int(innerRow[t]) # we wanna do Integer Things with these trees aight? also yes! this works as intended.

            # so i think we wanna check horizontally first and then vertically
            # ending out with an or statement so as to avoid duplicates
            # horizontally, we just have to check if it's the highest number to the left or right, yeah?
            # ... are we going to do more for loops. for the left side and right side.
            # there's gotta be a better way but let's do it this way for now.
            # i wonder if there's like, a 0<t<len(innerRow) solution that explicitly doesn't include t. for all not including t. something like that
            for l in range(0, t): # l for left side. is t inclusive or not? should it be t-1?... it's not a slice.... based on the eachTree thing i think it is inclusive
                # ok son of a bitch it isn't inclusive this time! what the hell! how is it inclusive up in eachtree but not down here.
                # when it was t-1, it would stop after grabbing the tree two spaces to the left.
                # now that it's t, it stops properly at t and grabs the one exactly to the left at finish.
                leftTree = int(innerRow[l])
                if leftTree >= eachTree:
                    leftTall = True
            for r in range(t+1, len(innerRow)): # well shit if this isn't inclusive then am i gonna have to do len+1???
                rightTree = int(innerRow[r])
                if rightTree >= eachTree:
                    rightTall = True
            # okay i think leftTall and rightTall are working as intended with the test cases. up and down will be a bit trickier.
            # keep in mind that nuance we learned about using the length function when dealing with indexing. and the discrepency there.
            for u in range(0, i): #taking all the rows up to not including i, the current row of the tree we're checking
                upperRows = rawGrid[u]
                upperTree = int(upperRows[t])
                if upperTree >= eachTree:
                    upTall = True
            for d in range(i+1, len(rawGrid)):
                downRows = rawGrid[d]
                downTree = int(downRows[t])
                if downTree >= eachTree:
                    downTall = True


            if leftTall == True and rightTall == True and upTall == True and downTall == True:
                invisibleCount += 1
    visibleTrees = treeTotal - invisibleCount
    return visibleTrees


def main():
    parsedInput = parseInputFile("input8.txt")
    print("visible trees total:", innerTree(parsedInput)) 

if __name__ == "__main__":
    main()

