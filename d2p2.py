import os


# Welcome To Part Two, part one worked with this! 
# but i wanted to keep the part one solution seperate so there it is.


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


# alright let's also just make it perfectly clear here what the win conditions are
# X Y Z are static, they determine if you need to Lose, Draw, Win
# so X Y Z corresponds 0 3 6 ... let's go fix that
# we'll have to reverse the if/else statements to check for opponent ABC before checking for XYZ replaced by 036
# reminder choosing rock = 1pt, paper = 2pt, scissors = 3pt
# if opponent A Rock, need to lose means Scissors(3), need to draw means Rock(1), need to win means Paper(2)
# if opponent B Paper, need lose (0) means choose Rock(1), need draw means Paper(2), need win means Scissors(3)
# if opponent C Scissors, need lose means paper(2), need draw means scissors(3), need win means rock(1)


# this returns a boolean based on if the letter is in the string or not
# == True has to be capitalized, == true is nothing (same for False)
def containsLetter(string, letter):
    return letter in string

def optionSelected(bigList: list):
    scoredStaticList = []
    for i in range(len(bigList)):
        currentItem = bigList[i]
        if containsLetter(currentItem, "X") == True:
            scoreStatic = currentItem.replace("X", "0")
        if containsLetter(currentItem, "Y") == True:
            scoreStatic = currentItem.replace("Y", "3")
        if containsLetter(currentItem, "Z") == True:
            scoreStatic = currentItem.replace("Z", "6")
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
        # checks all situations where opponent played rock, where A is in there
        if containsLetter(currentScoredItem, "A") == True:
            if containsLetter(currentScoredItem, "0") == True: 
                scoreWin = currentScoredItem.replace("A", "3") 
            if containsLetter(currentScoredItem, "3") == True:
                scoreWin = currentScoredItem.replace("A", "1")
            if containsLetter(currentScoredItem, "6") == True:
                scoreWin = currentScoredItem.replace("A", "2")
        # checks all situations where opponent played paper, where B is there
        if containsLetter(currentScoredItem, "B") == True:
            if containsLetter(currentScoredItem, "0") == True: 
                scoreWin = currentScoredItem.replace("B", "1") 
            if containsLetter(currentScoredItem, "3") == True:
                scoreWin = currentScoredItem.replace("B", "2")
            if containsLetter(currentScoredItem, "6") == True:
                scoreWin = currentScoredItem.replace("B", "3") 
        # checks all situations where I played scissors, where 3 is the item 
        if containsLetter(currentScoredItem, "C") == True:
            if containsLetter(currentScoredItem, "0") == True: 
                scoreWin = currentScoredItem.replace("C", "2") 
            if containsLetter(currentScoredItem, "3") == True:
                scoreWin = currentScoredItem.replace("C", "3")
            if containsLetter(currentScoredItem, "6") == True:
                scoreWin = currentScoredItem.replace("C", "1") 
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
