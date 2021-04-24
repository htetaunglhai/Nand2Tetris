// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed. 

// Put your code here.

(MAINLOOP)
	@KBD
	D=M
	@PRESSED
	D;JNE
	@KBD
	D=M
	@NOTPRESSED
	D;JEQ

(NOTPRESSED)
//WHITEN
@SCREEN
D=A
@addr
M=D // addr = 16384 (Screen's base address)

@8192
D=A
@n
M=D // n = 8192

@i
M=0 // i=0

(NOTPRESSEDLOOP)
@i
D=M
@n
D=D-M
@MAINLOOP
D;JGT // if i>n goto END

@addr
A=M
M=0 // RAM[addr]=1111111111111111

@i
M=M+1 // i = i+1

@1
D=A
@addr
M=M+D // 
@NOTPRESSEDLOOP
0;JMP // goto LOOP

///
@MAINLOOP
0;JMP



(PRESSED)
//BLACKEN

@SCREEN
D=A

@addr
M=D // addr = 16384 (Screen's base address)

@8192
D=A
@n
M=D // n = 8192


@i
M=0 // i=0

(PRESSEDLOOP)
@i
D=M
@n
D=D-M
@MAINLOOP
D;JGT // if i>n goto END

@addr
A=M
M=-1 // RAM[addr]=1111111111111111

@i
M=M+1 // i = i+1

@1
D=A
@addr
M=M+D // 
@PRESSEDLOOP
0;JMP // goto LOOP




///

			@MAINLOOP
			0;JMP

