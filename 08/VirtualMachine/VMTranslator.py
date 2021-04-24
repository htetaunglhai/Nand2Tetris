#! python3

import CodeWriter, Parser, sys, os



def isValidFile(userInput):
    return userInput[-3] + userInput[-2] + userInput[-1] == '.vm'


def getCurrentFileName(file):
    if isDir:
        return os.path.basename(file)[0:-3]
    else:
        return file[0:-3]

# get input from user
if len(sys.argv) < 2:
    print('Usage: VMTranslator.py file or folder')
    sys.exit()
userInput = sys.argv[1]

fileList = []
outputFileName = ''
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

        outputFileName = userInput
        os.chdir('..')

    else:
        if isValidFile(userInput):
            fileList.append(userInput)
            outputFileName = userInput[0:-3]

else:
     print('Your input is invalid. Try again')
     sys.exit()

#numOfLine = 0
ps = Parser.Parser()
cw = CodeWriter.CodeWriter()
outputFile = open(outputFileName + '.asm', 'a')

#Add bootstrap codes first
bootStrapCode = cw.writeBootstrapCode()
for codes in bootStrapCode:
    outputFile.write(codes + '\n')


for file in fileList:
    currentFileContent = open(file).readlines()
    currentFileName = getCurrentFileName(file)
    cw.fileName = currentFileName

    for line in currentFileContent:
        commandType, command = ps.parse(line)
        asmCodes = cw.writeCode(commandType, command)
        if not asmCodes ==  None:
            outputFile.write('//' + ' '.join(command) + '\n') # write the comment
            for codes in asmCodes:
                outputFile.write(codes + '\n')
            outputFile.write("\n") #add newline for clearness






