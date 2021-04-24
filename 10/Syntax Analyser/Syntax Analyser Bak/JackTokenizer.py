class JackTokenizer():
    def __init__(self, JackFilePath):

        with open(JackFilePath) as fileObj:
            self.jackCodes = fileObj.readlines()

        self.jackCodes = self._removeCW(self.jackCodes)

        for i in self.jackCodes:
            print(i)



    def _removeCW(self, inputCodeList): #Remove comments and whitespaces
       tempList = []

       for line in inputCodeList:
        if self._isComment(line) or line == '\n':
            continue
        else:
            tempList.append(self._clearInlineComment(line))


       return tempList


    def _clearInlineComment(self, inputString):
        pureCodes = ""

        for i in range(len(inputString)):
            if i < (len(inputString)- 1):
                if (inputString[i] + inputString[i+1] == "//"):
                    break

            pureCodes += inputString[i]

        return pureCodes


    def _isComment(self, inputString):
        inputString = inputString.strip()
        return inputString[0:2] == '//'





filePath = "D:\\2. Personal Project\\Nand2Tetris\\projects\\10\\Syntax Analyser\\Square\\Main.jack"
jc = JackTokenizer(filePath)






