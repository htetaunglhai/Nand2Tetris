//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 0
@SP
A=M
D=A-1
@SP
M=D
@LCL
A=M
D=A
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

//label LOOP_START
(BasicLoop.LOOP_START)

//push argument 0
@ARG
A=M
D=A
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 0
@LCL
A=M
D=A
@0
D=D+A
A=D
D=M
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

//pop local 0
@SP
A=M
D=A-1
@SP
M=D
@LCL
A=M
D=A
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

//push argument 0
@ARG
A=M
D=A
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push constant 1
@1
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

//pop argument 0
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
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

//push argument 0
@ARG
A=M
D=A
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//if-goto LOOP_START
@SP
A=M-1
D=M
@SP
M=M-1
@BasicLoop.LOOP_START
D;JNE

//push local 0
@LCL
A=M
D=A
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

