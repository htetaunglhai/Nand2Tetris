import sys, os, JackTokenizer, CompilationEngine


def getUserInput():
    if len(sys.argv) < 2:
        print('Usage: JackAnalyzer.py source (file or folder)')
        sys.exit()
    return sys.argv[1]

def makeInputFileList(userInput):
    tempInputFileList = []

    if os.path.exists(userInput):
        if os.path.isdir(userInput):
            os.chdir('.\\' + userInput)
            tempFileList = os.listdir()

            for file in tempFileList:
                if isValidFile(file):
                    tempInputFileList.append(os.path.join(os.getcwd(), file))
            os.chdir('..')

        else:
            if isValidFile(userInput):
                tempInputFileList.append(os.path.abspath(userInput))
    else:
        print('Your input is invalid. Try again.')
        sys.exit()

    return tempInputFileList


def isValidFile(file):
    return os.path.splitext(file)[1] == '.jack'

def createOutputFile():   #:write
    pass


def main():
    pass

##def test_tokenize():
##    inputFileList = makeInputFileList(getUserInput())
##    tokens = ""
##
##    for file in inputFileList:
##        jkt= JackTokenizer.JackTokenizer()
##        tokens = jkt.tokenize(file) # return token list
##
##
##        print(tokens)

       # outputFile = createOutputFile(file)
        #CompilationEngine(tokens, outputFile)
##    for i in tokens:
##        print(i)
##
##    print(len(tokens))
##    #print(inputFileList)




##def test_makeInputFileList():
##    usrinput = getUserInput()
##    inputFileList = makeInputFileList(usrinput)
##    print(inputFileList)
##    print(len(inputFileList))
##
##
##def test_getUserInput():
##    print(getUserInput())
##
##
##test_makeInputFileList()

def test_compiler():
    inputFileList = makeInputFileList(getUserInput())
    #tokens = ""

    for file in inputFileList:
        jkt= JackTokenizer.JackTokenizer()
        tokens = jkt.tokenize(file) # return token list
        comp = CompilationEngine.CompilationEngine(tokens, file)
        compiledTokens = comp.compile()
        print(compiledTokens)




test_compiler()







