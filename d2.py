import os

# learning from Apreche how to parse an input file Hopefully... (from their d1 AoC solution)
# i'm assuming this part is what the cool kids call some sort of scaffolding
# since the particulars get put together later down in the function in def main()
# cause boy and also howdy, i am going to learn how to input a file without copying and pasting
# i ran it and it creates a list where each item in the list is the two letters per line
# which honestly seems ideal for me!
def parse_input_file(filename: str):  # the filename has to be run as a string
    current_dir = os.path.dirname(__file__) # gets the directory that the file you're putting in is in (would be relevant if i was using organized directories)
    full_file_path = os.path.join(current_dir, filename) # creates the full file path so the open function will work
    with open(full_file_path) as input_file: # "with" must let you set a variable to be used in a function - seems so useful, learned this just now
        parsed_input = [] # we're running this as a list which honestly seems like the best way to do it here, i dunno a different way
        for line in input_file.read().splitlines(): # reading and splitting lines by line is this easy ;-; 
            parsed_input.append(line) # so to append to a list we can literally just follow this. this appends each line by line but remember this for later
    return parsed_input


# okay so there's a lot going on in this puzzle. first off, the 3rd position in each string (right? first char, whitespace second char, third char?)
# statically determines a simple addition to your score. x = 1, y = 2, z = 3. so the simplest first part to code seems to be to get that static score
# but then we're gonna have to go item by item and determine based on the first character whether or not you win lose or draw.
# my first idea is to go item by item, replace the X Y Z with 1 2 3, and then since we know that 1 = rock 2 = paper 3 = scissors, we can do like,
# some wacky if/else statements to determine the win/loss scenario for the A B C in that situation, and then replace the A B C with 6 win 3 draw 0 loss.
# then sum all the items in the list. will there be issues in '0 3', '6 1' being summed to 64? or will it be 10? gotta test w little test cases.

# alright let's also just make it perfectly clear here what the win conditions are
# if i choose X (rock), opponent's A = 3 (rock draw), opponent's B = 0 (i lose to paper), opponent's C = 6 (i win versus scissors)
# if i choose Y (paper), opponent's A = 6 (win over rock), opponent's B = 3 (paper tie), opponent's C = 0 (lost to scissors)
# if i choose Z (scissors), opponent's A = 0 (lost to rock), opponent's B = 6 (cut paper), opponent's C = 3 (scissors tie)

# this returns a boolean based on if the letter is in the string or not
# == True has to be capitalized, == true is nothing (same for False)
def containsLetter(string, letter):
    return letter in string

def optionSelected(bigList: list):
    scoredStaticList = []
    for i in range(len(bigList)):
        currentItem = bigList[i]
        if containsLetter(currentItem, "X") == True:
            scoreStatic = currentItem.replace("X", "1")
        if containsLetter(currentItem, "Y") == True:
            scoreStatic = currentItem.replace("Y", "2")
        if containsLetter(currentItem, "Z") == True:
            scoreStatic = currentItem.replace("Z", "3")
        scoredStaticList.append(scoreStatic) 
        i += 1
    return scoredStaticList

# i would like it if i didn't have to have all the if statements checking for presence for each A, B, C,
# but my first idea was to reassign scoreWin with .replace("A", "3"), reassign scoreWin with .replace("B", "0")
# but that might end up only reassigning the C values if it gets overwritten each time
# and if there's no C then the first changes wouldn't stick and it would just be letters
# so. the if statements are fine i guess
def winState(scoredList: list):
    scoredWinList = []
    for i in range(len(scoredList)):
        currentScoredItem = scoredList[i]
        # checks all situations where I played rock, where 1 is in the item
        if containsLetter(currentScoredItem, "1") == True:
            if containsLetter(currentScoredItem, "A") == True: 
                scoreWin = currentScoredItem.replace("A", "3") 
            if containsLetter(currentScoredItem, "B") == True:
                scoreWin = currentScoredItem.replace("B", "0")
            if containsLetter(currentScoredItem, "C") == True:
                scoreWin = currentScoredItem.replace("C", "6")
        # checks all situations where I played paper, where 2 is in the item
        if containsLetter(currentScoredItem, "2") == True:
            if containsLetter(currentScoredItem, "A") == True:
                scoreWin = currentScoredItem.replace("A", "6")
            if containsLetter(currentScoredItem, "B") == True:
                scoreWin = currentScoredItem.replace("B", "3")
            if containsLetter(currentScoredItem, "C") == True:
                scoreWin = currentScoredItem.replace("C", "0")
        # checks all situations where I played scissors, where 3 is the item 
        if containsLetter(currentScoredItem, "3") == True:
            if containsLetter(currentScoredItem, "A") == True:
                scoreWin = currentScoredItem.replace("A", "0")
            if containsLetter(currentScoredItem, "B") == True:
                scoreWin = currentScoredItem.replace("B", "6")
            if containsLetter(currentScoredItem, "C") == True:
                scoreWin = currentScoredItem.replace("C", "3")
        scoredWinList.append(scoreWin)
        i += 1
    return scoredWinList

def sumScores(winList: list):
    summedScoreList = [] 
    sumDigit = 0
    for i in range(len(winList)):
        currentUnsummed = winList[i]
        for x in currentUnsummed:
            if x.isdigit():
                sumDigit += int(x)
        summedScoreList.append(sumDigit)
        i += 1
    return summedScoreList[-1] # take the last item in this list and you'll get the total sum, not entirely sure why, but it works with the test case
    # guessing that it's because sumDigit doesn't get reset to 0 for each item in the list
    # but hey that's what we wanted anyway and we stumbled into it! only 2 hours of coding this time vs yesterday's 3! woah!

def main():
    parsed_input = parse_input_file("input2.txt")
    
    print(sumScores(winState(optionSelected(parsed_input)))) # i wonder if there's a way to build the nest into the functions themselves easier than this
    # we put print(parsed_input) here at first and by god it printed a list looking like ['C X', 'B Z'] ad infinitum (ad 2500 lines actually)

# whatever's in main() is what will be run when this script is called. do other shit before main() and put it into main()
if __name__ == "__main__": # so whenever a function is run directly (not referenced in other stuff) this variable is set to main.
    main()
