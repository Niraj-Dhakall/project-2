def computer(userInput):
    userInput = userInput.split()
    programMemory = []
    randomMemory = []
    haltString = ['hlt','HLT']
    movString = ['mov','MOV']
    addString = ['add','ADD']
    subString = ['sub','SUB']
    mulString = ['mul','MUL']
    divString = ['div','DIV']
    modString = ['mod','MOD']
    jmpString = ['jmp','JMP']
    cmpString = ['cmp','CMP']
    jlString = ['jl','JL']
    jgString = ['jg','JG']
    jeString = ['je','JE']
    jneString = ['jne','JNE']
    for x in range(int(userInput[1])):
        randomMemory.append("0")
    print(randomMemory)
    infile = open(userInput[0],'r')
    for j in range(len(randomMemory)):
        line = infile.readline().split()
        print(line)



if __name__ == '__main__':
    userInput = input("What file should we assemble, and what size of ram should we use?")
    computer(userInput)