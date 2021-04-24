//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 456
@456
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Call.fn 2
@Call.Call.fn.Return.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Call.Call.fn
0;JMP
(Call.Call.fn.Return.0)

//label loop
(Call.loop)

//goto loop
@Call.loop
0;JMP

//function Call.fn 0
(Call.Call.fn)

//label halt
(Call.halt)

//goto halt
@Call.halt
0;JMP

