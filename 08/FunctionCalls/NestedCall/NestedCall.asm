//Bootstrap
@256
D=A
@SP
M=D
@Sys.init.Return
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init.Return)
//function Sys.init 0
(Sys.init)

//push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D

//call Sys.main 0
@Sys.main.Return.0
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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(Sys.main.Return.0)

//pop temp 1
@SP
M=M-1
@SP
A=M
D=M
@6
M=D

//label LOOP
(Sys.vm.LOOP)

//goto LOOP
@Sys.vm.LOOP
0;JMP

//function Sys.main 5
(Sys.main)
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
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D

//push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 1
@SP
A=M
D=A-1
@SP
M=D
@LCL
A=M
D=A
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 2
@SP
A=M
D=A-1
@SP
M=D
@LCL
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

//push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 3
@SP
A=M
D=A-1
@SP
M=D
@LCL
A=M
D=A
@3
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

//call Sys.add12 1
@Sys.add12.Return.1
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(Sys.add12.Return.1)

//pop temp 0
@SP
M=M-1
@SP
A=M
D=M
@5
M=D

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

//push local 2
@LCL
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

//push local 3
@LCL
A=M
D=A
@3
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

//push local 4
@LCL
A=M
D=A
@4
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

//return
@LCL
D=M
@R13
M=D
@5
D=A
@R13
D=M-D
A=D
D=M
@R15
M=D
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
@R14
M=D
@SP
A=M
D=M
@R14
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@R13
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@R13
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@R13
D=M-D
A=D
D=M
@LCL
M=D
@R15
A=M
0;JMP

//function Sys.add12 0
(Sys.add12)

//push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 0
@SP
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@THAT
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

//push constant 12
@12
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

//return
@LCL
D=M
@R13
M=D
@5
D=A
@R13
D=M-D
A=D
D=M
@R15
M=D
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
@R14
M=D
@SP
A=M
D=M
@R14
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M-1
A=D
D=M
@THAT
M=D
@2
D=A
@R13
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@R13
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@R13
D=M-D
A=D
D=M
@LCL
M=D
@R15
A=M
0;JMP

