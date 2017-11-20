; ModuleID = "main.bc"
target triple = "<Target x86-64 (64-bit X86: EM64T and AMD64)>"
target datalayout = ""

@".str" = global [13 x i8] c"Hello World!!"
declare i32 @"puts"(i8* %".1")

define i32 @"main"()
{
entrada:
  %".2" = call i32 @"puts"(i8* getelementptr ([13 x i8], [13 x i8]* @".str", i32 0, i32 0))
  ret i32 0
}
