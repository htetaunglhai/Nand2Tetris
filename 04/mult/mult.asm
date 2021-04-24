// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

(START)
@R2 // variable for the answer created
M=0

@i // i = 0
M=0

(LOOP)
@i
D=M
@R1
D= D-M
@END
D;JEQ // if @sNum == 0, goto END

@R0
D=M
@R2
M= M+D // @R2 + @R0

@i
M= M+1 // i++
@LOOP
0;JMP

(END)
@END
0;JMP
