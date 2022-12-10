import os

def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__) 
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = []
        for line in inputFile.read().splitlines():
            parsedInput.append(line)
    return parsedInput

# to do day 7 i need a good way to implement a general tree in python
# then i need to use the input to implement the tree, accounting for all the nuance in the command-line stuff

def main():
    parsedInput = parseInputFile("")

if __name__ == "__main__":
    main()

