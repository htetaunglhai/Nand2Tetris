//function SimpleFunction.test 2
(SimpleFunction.test)

@0
D=A
@SP
A=M
M=D
@SP
M=M+1

@0
D=A
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

//push local 1
@LCL
A=M
D=A
@1
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

//not
@SP
A=M-1
A=M
D=!A
@SP
A=M-1
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

//push argument 1
@ARG
A=M
D=A
@1
D=D+A
A=D
D=M
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

//return

	//push the topmost value to ARG 0
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

	// save LCL in R13 to use as a base frame 
@LCL
D=M
@R13
M=D

	//Set *ARG+1 to SP
@ARG
D=M+1
@SP
M=D

	//Restore THAT
@R13
D=M-1
A=D
D=M
@THAT
M=D

	//Restore THIS
@2
D=A
@R13
D=M-D
A=D
D=M
@THIS
M=D

	//Restore ARG
@3
D=A
@R13
D=M-D
A=D
D=M
@ARG
M=D

	//Restore LCL
@4
D=A
@R13
D=M-D
A=D
D=M
@LCL
M=D

	//Goto return address 
@5
D=A
@R13
D=M-D
A=D
D=M
A=D
0;JMP

