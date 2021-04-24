#! python3

import sys, os
from JackTokenizer import *
from CompilationEngine import *




def isValidFile(userInput):
    return userInput[-5] + userInput[-4] + userInput[-3] + userInput[-2] + userInput[-1] == '.jack'


##def getCurrentFileName(file):
##    if isDir:
##        return os.path.basename(file)[0:-3]
##    else:
##        return file[0:-3]

# get input from user
if len(sys.argv) < 2:
    print('Usage: JackAnalyser.py file or folder')
    sys.exit()
userInput = sys.argv[1]

fileList = []
##outputFileName = ''
isDir = False
# check if what user typed exists.
if os.path.exists(userInput):

    if os.path.isdir(userInput):
        isDir = True
        # goto folder and loop the files
        os.chdir('.\\' + userInput)
        tempFileList = os.listdir()

        for file in tempFileList:
            if isValidFile(file):
                fileList.append(os.path.join(os.getcwd(), file))

##        outputFileName = userInput
        os.chdir('..')

    else:
        if isValidFile(userInput):
##            fileList.append(userInput)
            fileList.append(os.path.join(os.getcwd(), userInput))
##            outputFileName = userInput[0:-3]

else:
     print('Your input is invalid. Try again')
     sys.exit()


for i in fileList:
    print(i)

for filePath in fileList:
    atoms = JackTokenizer(filePath)
    CompilationEngine(atoms)
