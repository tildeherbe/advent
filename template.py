import os

def parseInputFile(filename: str):
    currentDir = os.path.dirname(__file__) 
    fullFilePath = os.path.join(currentDir, filename)
    with open(fullFilePath) as inputFile:
        parsedInput = []
        for line in inputFile.read().splitlines():
            parsedInput.append(line)
    return parsedInput

def main():
    parsedInput = parseInputFile("")

if __name__ == "__main__":
    main()

