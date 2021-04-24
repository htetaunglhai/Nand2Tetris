class CodeWriter():

    def __init__(self):
        self.fileName = ''
        self.cLabel = 0  #for generating unique label number used in eq, gt, lt
        self.retAddrCount = 0

    def writeCode(self, cmdType, cmd):

        if cmdType == 'C_PUSH':
            return self._writeCPush(cmd[1:])

        elif cmdType == 'C_POP':
            return self._writeCPop(cmd[1:])

        elif cmdType == 'C_ARITHMETIC':
            return self._writeArithmetic(cmd[0])

        elif cmdType == 'C_LABEL':
            return self._writeLabel(cmd[1])


        elif cmdType == 'C_GOTO':
            return self._writeGoto(cmd[1])


        elif cmdType == 'C_IF':
            return self._writeIfGoto(cmd[1])


        elif cmdType == 'C_FUNCTION':
            return self._writeFunction(cmd[1:])

        elif cmdType == 'C_CALL':
            return self._writeCallFunction(cmd[1:])

        elif cmdType == 'C_RETURN':
            return self._writeReturn()

    def _getSegmentName(self, segment):
        segmentList = {'local': 'LCL', 'argument': 'ARG',
                       'this': 'THIS', 'that': 'THAT'}

        segment = segmentList[segment]
        return segment


    def _writeCPush(self, cmd):

        if cmd[0] == 'constant':
            return self._writePushConstant(cmd[1])

        elif cmd[0] in "local argument this that temp" .split():
            if cmd[0] == 'temp':
                return self._writePushTemp(cmd[1])
            else:
                return self._writePushSegment(cmd)

        elif cmd[0] == 'static':
            return self._writePushStatic(cmd[1])

        elif cmd[0] == 'pointer':
            return self._writePushPointer(cmd[1])

    def _writeCPop(self, cmd):

        if cmd[0] in "local argument this that temp".split():
            if cmd[0] == 'temp':
                return self._writePopTemp(cmd[1])
            else:
                return self._writePopSegment(cmd)

        elif cmd[0] == 'static':
            return self._writePopStatic(cmd[1])

        elif cmd[0] == 'pointer':
            return self._writePopPointer(cmd[1])

    def _writeArithmetic(self, opr):

        if opr == 'add':
            return self._writeAdd()
        elif opr == 'sub':
            return self._writeSub()
        elif opr == 'neg':
            return self._writeNeg()
        elif opr == 'and':
            return self._writeAnd()
        elif opr == 'or':
            return self._writeOr()

        elif opr == 'not':
            return self._writeNot()

        if opr in 'eq gt lt'.split():
            self.cLabel += 1
            if opr == 'eq':
                return self._writeComp('JEQ')

            elif opr == 'gt':
                return self._writeComp('JGT')

            elif opr == 'lt':
                return self._writeComp('JLT')


    def _writePushConstant(self, consantNum):
        asm1 = '@' + consantNum
        asm1 = [asm1]
        asm2 = """
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """.split()

        return asm1+asm2

    def  _writePushSegment(self, cmd):
            segment = self._getSegmentName(cmd[0])
            addr = cmd[1]
            asm1 = '@' + segment
            asm1 = [asm1]
            asm2 = """
                    A=M
                    D=A
                    """.split()

            asm3 = '@' + addr
            asm3 = [asm3]
            asm4 = """
                    D=D+A
                    A=D
                    D=M
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1
                    """.split()

            return asm1 + asm2 + asm3 + asm4


    def _writePushStatic(self, staticNum):
        asm1 = '@' + self.fileName + '.' + staticNum
        asm1 = [asm1]
        asm2 = """
                D=M
                @SP
                A=M
                M=D
                @SP
                 M=M+1
                """.split()

        return asm1 + asm2


    def _writePushPointer(self, ptNum):
        pointer = {'0': 'THIS', '1': 'THAT'}
        asm1 = ['@' + pointer[ptNum]]
        asm2 = """
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """.split()

        return asm1 + asm2

    def _writePushTemp(self, tempAddr):
        baseAddress = 5
        tempAddr = str(baseAddress + int(tempAddr))
        asm1 = ['@' + tempAddr]
        asm2 = """
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
            """.split()
        return asm1 + asm2


    def  _writePopSegment(self, cmd):

        segment = self._getSegmentName(cmd[0])
        addr = cmd[1]
        asm1 = """
                @SP
                A=M
                D=A-1
                @SP
                M=D
                """.split()
        asm2 = ['@' + segment]
        asm3 = """
                A=M
                D=A
                """.split()
        asm4 = ['@' + addr]
        asm5 = """
                D=D+A
                @R13
                M=D
                @SP
                A=M
                D=M
                @R13
                A=M
                M=D
                """.split()
        return asm1 + asm2 + asm3 + asm4 + asm5


    def _writePopStatic(self, staticNum):
        asm1 = """
                @SP
                M=M-1
                @SP
                A=M
                D=M
                """.split()
        asm2 = ['@' + self.fileName + '.' + staticNum]
        asm3 = ['M=D']
        return asm1 + asm2 + asm3


    def _writePopPointer(self, ptNum):

        pointer = {'0': 'THIS', '1': 'THAT'}
        asm1 = """
                @SP
                M=M-1
                @SP
                A=M
                D=M
                """.split()
        asm2 = ['@' + pointer[ptNum]]
        asm3 = ["M=D"]
        return asm1 + asm2 + asm3



    def _writePopTemp(self, tempAddr):
        baseAddress = 5
        tempAddr = str(baseAddress + int(tempAddr))

        asm1 = """
                @SP
                M=M-1
                @SP
                A=M
                D=M
                """.split()

        asm2 =['@'+ tempAddr]
        asm3 = ['M=D']

        return asm1 + asm2 + asm3

    def _writeAdd(self):
        asm = """
                @SP
                M=M-1
                @SP
                A=M
                D=M
                @SP
                A=M-1
                A=M
                D=A+D
                @SP
                A=M-1
                M=D
                """.split()
        return asm

    def _writeSub(self):
        asm = """
                @SP
                M=M-1
                @SP
                A=M
                D=M
                @SP
                A=M-1
                A=M
                D=A-D
                @SP
                A=M-1
                M=D
                """.split()

        return asm

    def _writeNeg(self):
        asm = """
				@SP
				A=M-1
				A=M
				D=-A
				@SP
				A=M-1
				M=D
                """.split()
        return asm

    def _writeAnd(self):
        asm = """
		      @SP
		      M=M-1
		      @SP
		      A=M
		      D=M
		      @SP
		      A=M-1
		      M=M&D
         """.split()

        return asm

    def _writeOr(self):
         asm = """
				@SP
				M=M-1
				@SP
				A=M
				D=M
				@SP
				A=M-1
				M=M|D
                """.split()
         return asm

    def _writeNot(self):
         asm = """
				@SP
				A=M-1
				A=M
				D=!A
				@SP
				A=M-1
				M=D
                """.split()
         return asm

    def _writeComp(self, compType):             #for eq, gt and lt

         loopNum = str(self.cLabel)
         asm1 = """
                @SP
                M=M-1
                @SP
                A=M
                D=M
                @SP
                A=M-1
                A=M
                D=A-D
                """.split()
         asm2 = ['@CLOOP.' + loopNum]
         asm3 = ['D;' + compType]
         asm4 = """
                @SP
                A=M-1
                M=0
                """.split()
         asm5 = ['@END_CLOOP.' + loopNum]
         asm6 = ['0;JMP']
         asm7 = ['(' + 'CLOOP.' + loopNum + ')']
         asm8 = """
                @SP
                A=M-1
                M=-1
                """.split()
         asm9 = ['(' + 'END_CLOOP.' + loopNum + ')']
         return asm1 + asm2 + asm3 + asm4 + asm5 + asm6 + asm7 + asm8 + asm9

    def _writeLabel(self, label):
        lableName = self.fileName + '.' + label

        return ['(' + lableName + ')']

    def _writeGoto(self, label):
        lableName = '@' + self.fileName + '.' + label
        return [lableName, '0;JMP']

    def _writeIfGoto(self, label):

        lableName = '@' + self.fileName + '.' + label
        asm1 = """
                @SP
                A=M-1
                D=M
                @SP
                M=M-1
                """.split()
        asm2 =  [lableName, 'D;JNE']
        return asm1 + asm2

    def _writeFunction(self, cmd):    # cmd=[funcName, i]
        functionName = '(' + cmd[0] + ')'
        pushAsm = []
        if int(cmd[1]) > 0:
            pushCodes = """
                            @0
                            D=A
                            @SP
                            A=M
                            M=D
                            @SP
                            M=M+1
                            """.split()
            pushAsm = pushCodes * int(cmd[1])
        return [functionName] + pushAsm


    def _getRetAddr(self, funcName):
        addr = self.retAddrCount
        self.retAddrCount += 1
        return funcName + '.' + 'Return' + '.' + str(addr)

    def _writeCallFunction(self, cmd): # cmd = ['func', 'argi']
        functionName = cmd[0]
        retAddr = self._getRetAddr(cmd[0])
        asm1 = [ '@' + retAddr]
        asm2 = """
                    D=A
					@SP
					A=M
					M=D
					@SP
					M=M+1
					@LCL
					D=M
					@SP
					A=M
					M=D
					@SP
					M=M+1
					@ARG
					D=M
					@SP
					A=M
					M=D
					@SP
					M=M+1
					@THIS
					D=M
					@SP
					A=M
					M=D
					@SP
					M=M+1
					@THAT
					D=M
					@SP
					A=M
					M=D
					@SP
					M=M+1
                    """.split()
        asm3 = """
                    @SP
					D=M
					@5
					D=D-A
                    """.split()
        asm4 = ['@' + cmd[1]]
        asm5 = """
                    D=D-A
					@ARG
					M=D
					@SP
					D=M
					@LCL
					M=D
                    """.split()
        gotoFunc = '(' + retAddr + ')'
        asm6 = ['@' + cmd[0],'0;JMP', gotoFunc]
        asm = asm1 + asm2 + asm3 + asm4 + asm5 + asm6
        return asm

    def _writeReturn(self):
        asm = """
					@LCL
					D=M
					@R13
					M=D
					@5
					D=A
					@R13
					D=M-D
					A=D
					D=M
					@R15
					M=D
					@SP
					A=M
					D=A-1
					@SP
					M=D
					@ARG
					A=M
					D=A
					@0
					D=D+A
					@R14
					M=D
					@SP
					A=M
					D=M
					@R14
					A=M
					M=D
					@ARG
					D=M+1
					@SP
					M=D
					@R13
					D=M-1
					A=D
					D=M
					@THAT
					M=D
					@2
					D=A
					@R13
					D=M-D
					A=D
					D=M
					@THIS
					M=D
					@3
					D=A
					@R13
					D=M-D
					A=D
					D=M
					@ARG
					M=D
					@4
					D=A
					@R13
					D=M-D
					A=D
					D=M
					@LCL
					M=D
					@R15
					A=M
					0;JMP
                    """.split()
        return asm

    def writeBootstrapCode(self):
        asm = """
				//Bootstrap
				@256
				D=A
				@SP
				M=D
				@Sys.init.Return
				D=A
				@SP
				A=M
				M=D
				@SP
				M=M+1
				@LCL
				D=M
				@SP
				A=M
				M=D
				@SP
				M=M+1
				@ARG
				D=M
				@SP
				A=M
				M=D
				@SP
				M=M+1
				@THIS
				D=M
				@SP
				A=M
				M=D
				@SP
				M=M+1
				@THAT
				D=M
				@SP
				A=M
				M=D
				@SP
				M=M+1
				@SP
				D=M
				@5
				D=D-A
				@0
				D=D-A
				@ARG
				M=D
				@SP
				D=M
				@LCL
				M=D
				@Sys.init
				0;JMP
				(Sys.init.Return)""".split()
        return asm
