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
@EQ1
D;JEQ

@SP
A=M-1
M=0
@END_EQ1
0;JMP

(EQ1)
@SP
A=M-1
M=-1
(END_EQ1)

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
@EQ3
D;JEQ

@SP
A=M-1
M=0
@END_EQ3
0;JMP

(EQ3)
@SP
A=M-1
M=-1
(END_EQ3)

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
@EQ2
D;JEQ

@SP
A=M-1
M=0
@END_EQ2
0;JMP

(EQ2)
@SP
A=M-1
M=-1
(END_EQ2)

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
@LT1
D;JLT

@SP
A=M-1
M=0
@END_LT1
0;JMP

(LT1)
@SP
A=M-1
M=-1
(END_LT1)

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
@LT2
D;JLT

@SP
A=M-1
M=0
@END_LT2
0;JMP

(LT2)
@SP
A=M-1
M=-1
(END_LT2)

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
@LT3
D;JLT

@SP
A=M-1
M=0
@END_LT3
0;JMP

(LT3)
@SP
A=M-1
M=-1
(END_LT3)

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
@GT1
D;JGT

@SP
A=M-1
M=0
@END_GT1
0;JMP

(GT1)
@SP
A=M-1
M=-1
(END_GT1)

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
@GT2
D;JGT

@SP
A=M-1
M=0
@END_GT2
0;JMP

(GT2)
@SP
A=M-1
M=-1
(END_GT2)

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
@GT3
D;JGT

@SP
A=M-1
M=0
@END_GT3
0;JMP

(GT3)
@SP
A=M-1
M=-1
(END_GT3)

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
