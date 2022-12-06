import os
import re

def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__) #note to self find out why __file__ works
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = []
        for line in inputFile.read().splitlines():
            parsedInput.append(line)
    return parsedInput

# for initializing the crate list I trust writing it out by hand the most.
# it's not that long or difficult, and the vertical way it's written out would be a frustrating stopping block before the meat of the problem
# i look forward to seeing how others automate the task though!

# the bottom of any given stack will be indexed at 0, highest number in stack will have len(list)

# also keep in mind that the list is indexed 0, not 1, so each stack's number will have to be adjusted accordingly
# maybe put in an empty 0 stack at start if we run into trouble?

# switch between test and normal cases here. really hard to work with test cases but we can try later.

# test = True

# if test:
 #    crateKey = []
  #   crateKey.append(['Z', 'N']) # these HAVE to be strings. if not written as strings they're read as undefined variables
 #    crateKey.append(['M','C', 'D'])
  #   crateKey.append(['P'])


# okay i am willing to do a lot of things the dumb way when that's the way that works but i am not manually writing out each string marker 
# i formatted the first line in input5.txt to be a list of lists
# just gonna parse that somehow once it's in here. worrying about the test cases first though

def moveCrates(moveList: list): # taking in the move lists
    instructionList = []
    # okay i want a way to just identify which three numbers are in the string cause i know each number in each place does a specific thing.
    # don't wanna fiddle with the english in it.
    # there's gotta be some sort of regular expression or shortcut sort of way to do this
    # i saw someone do like, \d+ which seems to mean one or more digits?
    # gotta find that three times per string and have them in order. and accomodate for double digit orders
    # although double digits only happen in the "move" command, not the stack name digit (from: to:)
    for item in moveList:
        moves = item
        nums = re.findall(r'\d+', moves)
        instructionList.append(nums) # for the line that had no nums, key line, there was an empty item. broke craneaction till we fixed it. need specified range next time, like, /if/ nums are there append them, or specify which line to start. just took the offending line out for now
    return instructionList

def craneAction(moveList: list):
    # we can use the already-declared crateKey here
    # or maybe we should declare it in here at some point instead
    
    # YES this was one single array at some point but i was debugging some absolute hell caused by .append when i should have used .extend
    # so in the process of debugging i unarrayed it cause i didn't understand that .extend was missing until the very end of the problem, and fixing it got me the solve
    # the AoC rewrite will be a project in like a month or two ahaha. for now it's just What I Actually Used
    pile1 = ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C']
    pile2 = ['N', 'V', 'G', 'P', 'H', 'W', 'B']
    pile3 = ['F', 'W', 'B', 'J', 'G']
    pile4 = ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S']
    pile5 = ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H']
    pile6 = ['B', 'C', 'W', 'G', 'F', 'S']
    pile7 = ['H', 'T', 'P', 'M', 'Q', 'B', 'W']
    pile8 = ['F', 'S', 'W', 'T']
    pile9 = ['N', 'C', 'R']
    instructionList = moveCrates(moveList) 
    for row in instructionList: 
        pileNumFr = []
        pileNumTo = []
        move = int(row[0]) # these numbers are strings until otherwise proven. so int them
        fr = int(row[1]) # would be from but from is a reserved keyword. this is the initial pile to take from though
        to = int(row[2])
        # get ready for some new if statement bullshit!
        if fr == 1:
            pileNumFr = pile1
        if fr == 2:
            pileNumFr = pile2
        if fr == 3:
            pileNumFr = pile3
        if fr == 4:
            pileNumFr = pile4
        if fr == 5:
            pileNumFr = pile5
        if fr == 6:
            pileNumFr = pile6
        if fr == 7:
            pileNumFr = pile7
        if fr == 8:
            pileNumFr = pile8
        if fr == 9: 
            pileNumFr = pile9
        if to == 1:
            pileNumTo = pile1
        if to == 2:
            pileNumTo = pile2
        if to == 3:
            pileNumTo = pile3
        if to == 4:
            pileNumTo = pile4
        if to == 5:
            pileNumTo = pile5
        if to == 6:
            pileNumTo = pile6
        if to == 7:
            pileNumTo = pile7
        if to == 8:
            pileNumTo = pile8
        if to == 9: 
            pileNumTo = pile9
        # so we gotta work with the pileNumFr and pileNumTo and then assign the other way at the end of the function. like, pile9 = pileNumTo, but generalized. more ifs...
        # i would love to be able to identify variables based on which digit they have in them.

        # pileSlice = pileNumFr[-1:-move-1:-1]
        
        # the stopping point has to be past the part where the moves happen, cause the stop is non-inclusive
        # HEY. For Part 1 this pileSlice line was pileSlice = pileNumFr[-1:-move-1:-1] and i am NOT redoing this whole damn program lmao.
        # We no longer need to reverse the slices so we're just gonna fix this one line.

        pileSlice = pileNumFr[-move::]

        pileNumTo.extend(pileSlice) # MVP LINE OF CODE RIGHT HERE!!!! i had a MESS of [[]][][[][[[[[[[[]][][][[[[[[[ when i used append cause that creates a new row. EXTEND...
        del pileNumFr[-1:-move-1:-1]
        
        if fr == 1:
            pile1 = pileNumFr
        if fr == 2:
            pile2 = pileNumFr
        if fr == 3:
            pile3 = pileNumFr
        if fr == 4:
            pile4 = pileNumFr
        if fr == 5:
            pile5 = pileNumFr
        if fr == 6:
            pile6 = pileNumFr
        if fr == 7:
            pile7 = pileNumFr
        if fr == 8:
            pile8 = pileNumFr
        if fr == 9: 
            pile9 = pileNumFr
        if to == 1:
            pile1 = pileNumTo
        if to == 2:
            pile2 = pileNumTo
        if to == 3:
            pile3 = pileNumTo
        if to == 4:
            pile4 = pileNumTo
        if to == 5:
            pile5 = pileNumTo
        if to == 6:
            pile6 = pileNumTo
        if to == 7:
            pile7 = pileNumTo
        if to == 8:
            pile8 = pileNumTo
        if to == 9: 
            pile9 = pileNumTo
        
    print(pile1)
    print(pile2)
    print(pile3)
    print(pile4)
    print(pile5)
    print(pile6)
    print(pile7)
    print(pile8)
    print(pile9)



def main():
    parsedInput = parseInputFile("input5.txt")
    craneAction(parsedInput)

if __name__ == "__main__":
    main()

