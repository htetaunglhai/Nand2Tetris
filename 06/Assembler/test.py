def getCInst(code):
    dest = ''
    jump = ''
    comp = ''
    gotComp = False
    for char in range(len(code)):
        
        if code[char] == '=':
            dest = code[:char]
            comp = code[char+1:]
            
        if code[char] == ';':
            jump = code[char+1:]
            comp = code[:char]
            

    return [dest, comp, jump]
        

def genDBits(dBits):
    d1, d2, d3, = '0', '0', '0'
    if dBits == '':
        return d1+d2+d3
    
    if 'A' in dBits:
        d1 = '1'
    
    if 'D' in dBits:
        d2 = '1'
    
    if 'M' in dBits:
        d3 = '1'

    return d1+d2+d3


def genJBit(jump):

    jumpTable = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

    return jumpTable[jump]

def hasAOrNot(comp):
    if 'M' in comp:
        return '1'
    else: return '0'








compTable = {

'0': '101010', 
'1': '111111', 
'-1': '111010', 
'D': '001100', 
'A': '110000', 
'M': '110000', 
'!D': '001101', 
'!A': '110001', 
'!M': '110001', 
'-D': '001111', 
'-A': '110011', 
'-M': '110011', 
'D+1': '011111', 
'A+1': '110111', 
'M+1': '110111',
'D-1': '001110', 
'A-1': '110010', 
'M-1': '110010', 
'D+A': '000010', 
'D+M': '000010', 
'D-A': '010011', 
'D-M': '010011', 
'A-D': '000111', 
'M-D': '000111',
'D&A': '000000', 
'D&M': '000000', 
'D|A': '010101', 
'D|M': '010101'
}



for key, value in compTable.items():
    if len(value) != 6:
        print(key + ': ' + value)

































'''
code = 'D=M M=D D;JGT M=D+M 0;JMP D;JNE D=D-M D;JEQ D;JNE D=D-M'.split()
for i in code:
    
    print(getCInst(i))
    print()


dest = ''
print(genDBits(dest))

jumpTable = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

jumps = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
for i in jumps:
    print(jumpTable[i])
    

    
'''
    
