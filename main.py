def interrupt(userInput, memory):
    printString = ['print', 'PRINT']
    inputString = ['input','INPUT']
    if(userInput[1] in printString):
        printMessage = userInput[2:]
        print(' '.join(printMessage))
    elif(userInput[1] in inputString):
        intterruptInput = int(input(''))
        inputIndex = userInput[2].strip('[]')
        memory[int(inputIndex)] = intterruptInput
def jump(userInput, memory):
    jlString = ['jl','JL']
    jgString = ['jg','JG']
    jeString = ['je','JE']
    jneString = ['jne','JNE']
    print("this is jumping shit")
def operationCommands(userInput,memory):
    print("Hello world")
def moveCommand(line,memory):
    bracketString = '['
    moveSource = line[2]
    moveDestination = int(line[1].strip('[]'))
    if (bracketString in moveSource):
        tempMoveSource = 0
        sourceValue = 0
        tempMoveSource = int(line[2].strip('[]'))
        sourceValue = memory[int(moveDestination)]
        memory[int(moveDestination)] = memory[tempMoveSource]
        memory[tempMoveSource] = int(sourceValue)
    else:
        moveSource = int(line[2])
        memory[int(moveDestination)] = moveSource
def compareCommand(line,memory):
    bracketString = '['
    lessThan = False
    equalTo = False
    compareValue1 = line[1]
    compareValue2 = line[2]
    if (bracketString in compareValue1) and (bracketString in compareValue2):
        compareValue1 = int(line[1].strip('[]'))
        compareValue2 = int(line[2].strip('[]'))
        if memory[compareValue1] < memory[compareValue2]:
            lessThan = True
        elif memory[compareValue1] == memory[compareValue2]:
            equalTo = True
    else:
        compareValue1 = int(line[1].strip('[]'))
        compareValue2 = int(line[2])
        if memory[compareValue1] < compareValue2:
            lessThan = True
        elif memory[compareValue1] == compareValue2:
            equalTo = True

def runCommands(line,memory, programMemory):

    haltString = ['hlt','HLT']
    movString = ['mov','MOV']
    addString = ['add','ADD']
    subString = ['sub','SUB']
    mulString = ['mul','MUL']
    divString = ['div','DIV']
    modString = ['mod','MOD']
    jmpString = 'j'
    cmpString = ['cmp','CMP']
    intString = ['int','INT']
    if (line[0] in intString):
        interrupt(line,memory)
        programMemory.append(line)
    if(line[0] in movString):
        moveCommand(line,memory)
        programMemory.append(line)
    if(line[0] in cmpString):
        compareCommand(line,memory)
        programMemory.append(line)
    if(jmpString in line[0].lower()):
        jump(line,memory)
        programMemory.append(line)
def computer(userInput):
    userInput = userInput.split()
    randomMemory = []
    programMemory = []

    for x in range(int(userInput[1])):
        randomMemory.append(0)
    infile = open(userInput[0],'r')
    for j in range(len(randomMemory)):
        line = infile.readline().split()
        runCommands(line,randomMemory,programMemory)



if __name__ == '__main__':
    userInput = 'is_prime.ret 10'

    computer(userInput)