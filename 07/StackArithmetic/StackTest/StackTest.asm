//push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.1
D;JEQ
@SP
A=M-1
M=0
@END_CLOOP.1
0;JMP
(CLOOP.1)
@SP
A=M-1
M=-1
(END_CLOOP.1)
//push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16

@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.2
D;JEQ
@SP
A=M-1
M=0
@END_CLOOP.2
0;JMP
(CLOOP.2)
@SP
A=M-1
M=-1
(END_CLOOP.2)
//push constant 16

@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17

@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.3
D;JEQ
@SP
A=M-1
M=0
@END_CLOOP.3
0;JMP
(CLOOP.3)
@SP
A=M-1
M=-1
(END_CLOOP.3)
//push constant 892

@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891

@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.4
D;JLT
@SP
A=M-1
M=0
@END_CLOOP.4
0;JMP
(CLOOP.4)
@SP
A=M-1
M=-1
(END_CLOOP.4)
//push constant 891

@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892

@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.5
D;JLT
@SP
A=M-1
M=0
@END_CLOOP.5
0;JMP
(CLOOP.5)
@SP
A=M-1
M=-1
(END_CLOOP.5)
//push constant 891

@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891

@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.6
D;JLT
@SP
A=M-1
M=0
@END_CLOOP.6
0;JMP
(CLOOP.6)
@SP
A=M-1
M=-1
(END_CLOOP.6)
//push constant 32767

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.7
D;JGT
@SP
A=M-1
M=0
@END_CLOOP.7
0;JMP
(CLOOP.7)
@SP
A=M-1
M=-1
(END_CLOOP.7)
//push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.8
D;JGT
@SP
A=M-1
M=0
@END_CLOOP.8
0;JMP
(CLOOP.8)
@SP
A=M-1
M=-1
(END_CLOOP.8)
//push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
A=M
D=A-D
@CLOOP.9
D;JGT
@SP
A=M-1
M=0
@END_CLOOP.9
0;JMP
(CLOOP.9)
@SP
A=M-1
M=-1
(END_CLOOP.9)
//push constant 57

@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31

@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53

@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//add

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
//push constant 112

@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub

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
//neg

@SP
A=M-1
A=M
D=-A
@SP
A=M-1
M=D
//and

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M&D
//push constant 82

@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or

@SP
M=M-1
@SP
A=M
D=M
@SP
A=M-1
M=M|D
//not

@SP
A=M-1
A=M
D=!A
@SP
A=M-1
M=D
