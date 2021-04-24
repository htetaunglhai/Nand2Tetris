       
def isLable(line):
    if(line.startswith('(')):
        return True
    else: 
        return False

def isC(line):
    if('=' in line or ';' in line):
        return True
    else:
        return False

def isA(line):
    if(line[0] == '@'):
        return True
    else: return False


def isVar(line):
    if(not (line[1:].isdigit())):
        return True
    else: False

def decToBin(string):
    num = bin(int(string))
    return num[2:]


def removeCmt(lines):
    string = []
    for line in lines:
        if(line[:2] == '//'):
            continue
        string.append(line)


    return string

def clearInlineCmt(line):
    word = ''
    for char in line:
        if(char == "/"):
            break
        word += char
    return word

def  isBlankLine(line):
    if(line == '\n'):
        return True
    else:
        return False


def parseCInst(code):
    dest = ''
    jump = ''
    comp = ''

    for char in range(len(code)):    
        if code[char] == '=':
            dest = code[:char]
            comp = code[char+1:]
            
        if code[char] == ';':
            jump = code[char+1:]
            comp = code[:char]            

    return [dest, comp, jump]

def genDBits(dest):
    d1, d2, d3, = '0', '0', '0'

    if dest == '':
        return d1+d2+d3

    if 'A' in dest:
        d1 = '1'
    
    if 'D' in dest:
        d2 = '1'
    
    if 'M' in dest:
        d3 = '1'

    return d1+d2+d3

def genCBit(compTable, comp):
    #tbl = compTable
    return compTable[comp]

def genJBit(jump):

    jumpTable = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

    return jumpTable[jump]
    
def hasAOrNot(comp):
    if 'M' in comp:
        return '1'
    else: return '0'
    
def addExtraZero(aBits):
    neededZero = 16 - len(aBits) 
    extraZero = '0' * neededZero
    return extraZero + aBits 
