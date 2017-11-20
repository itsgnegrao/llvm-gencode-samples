from llvmlite import ir
from llvmlite import binding as llvm
import sys

'''
Este módulo contém uma função main e criação de um array unidimensional como variável global e outro como local.
Será gerado um código em LLVM como este em C:

<<Colocar o Código do Exemplo de Referência.>>

'''
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

def main():

    #define tipos
    i32 = ir.IntType(32)
    i8 = ir.IntType(8)

    #carrega o modulo
    builder = ir.IRBuilder()
    module = ir.Module("main.bc")
    module.triple = llvm.Target.from_triple("x86_64-pc-linux-gnu")

    #string hello world
    hellostr = "Hello World!!"

    #cria a var hello
    stringtype = ir.ArrayType(i8, len(hellostr))
    hello = ir.GlobalVariable(module, stringtype, '.str')
    hello.initializer = ir.Constant(stringtype, bytearray(hellostr, 'utf8'))


    fntype = ir.FunctionType(i32, [i8.as_pointer()])
    puts = ir.Function(module, fntype, 'puts')


    fntype = ir.FunctionType(i32, [])
    func = ir.Function(module, fntype, name='main')
    bb_entry = func.append_basic_block("entrada")

    builder.position_at_end(bb_entry)

    #constant 0
    zero = ir.Constant(i32, 0)
    builder.call(puts, [hello.gep((zero, zero))])

    builder.ret(zero)

    #salva o arquivo
    arquivo = open('main.ll', 'w')
    arquivo.write(str(module))
    arquivo.close()
    print(module)


if __name__ == '__main__':
    main()
