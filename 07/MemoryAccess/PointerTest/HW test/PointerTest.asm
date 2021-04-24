// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/PointerTest/PointerTest.vm

// Executes //pop and //push commands using the 
// pointer, this, and that segments.

//push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M= M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M= M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D

//push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M= M+1

//pop this 2
@SP
A=M
D=A-1
@SP
M=D
@THIS
A=M
D=A
@2
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M= M+1

//pop that 6
@SP
A=M
D=A-1
@SP
M=D
@THAT
A=M
D=A
@6
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D


//push pointer 0
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

//push pointer 1
@THAT
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

//push this 2
@THIS
A=M
D=A
@2
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

//push that 6
@THAT
A=M
D=A
@6
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

