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

(LOOP)
@i
D=M
@n
D=D-M
@END
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
@LOOP
0;JMP // goto LOOP


(END)
@END   // program's end
0;JMP // infinite loop

