def interrupt(userInput, memory):
    printString = ['print', 'PRINT']
    inputString = ['input','INPUT']
    brackString = '['
    if(userInput[1] in printString):
        if brackString in userInput[2]:
            print(memory[int(userInput[2].strip('[]'))])
        else:
            printMessage = userInput[2:]
            print(' '.join(printMessage))
    elif(userInput[1] in inputString):
        intterruptInput = int(input(''))
        inputIndex = userInput[2].strip('[]')
        memory[int(inputIndex)] = intterruptInput
def jump(userInput, memory, compareList):
    jlString = ['jl','JL']
    jgString = ['jg','JG']
    jeString = ['je','JE']
    jneString = ['jne','JNE']
    if userInput[0] in jlString:
        print("hello")

def operationCommands(userInput,memory):
    print("this is adding and all that shit")
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
    compareList = []
    if (bracketString in compareValue1) and (bracketString in compareValue2):
        compareValue1 = int(line[1].strip('[]'))
        compareValue2 = int(line[2].strip('[]'))
        if memory[compareValue1] < memory[compareValue2]:
            lessThan = True
            print(f"{memory[compareValue1]} is smaller than {memory[compareValue2]}")
        elif memory[compareValue1] == memory[compareValue2]:
            equalTo = True
            print(f"{memory[compareValue1]} is equal to {memory[compareValue2]}")
    else:
        compareValue1 = int(line[1].strip('[]'))
        compareValue2 = int(line[2])
        if memory[compareValue1] < compareValue2:
            lessThan = True
        elif memory[compareValue1] == compareValue2:
            equalTo = True
    compareList.append(lessThan)
    compareList.append(equalTo)
    return compareList
# def runCommands(line,memory, programMemory, compareList):


def computer(userInput):
    userInput = userInput.split()
    randomMemory = []
    programMemory = []
    haltString = ['hlt','HLT']
    compareList = []
    cmpString = ['cmp','CMP']
    haltString = ['hlt','HLT']
    movString = ['mov','MOV']
    operationStrings = ['mod','MOD','div','DIV','mul','MUL','sub','SUB','add','ADD']
    jmpString = 'j'
    cmpString = ['cmp','CMP']
    intString = ['int','INT']
    lineJump = False
    for x in range(int(userInput[1])):
        randomMemory.append(0)
    infile = open(userInput[0],'r')

    line = infile.readline().split()
    while line[0] not in haltString:
        if (line[0] in intString):
            interrupt(line,randomMemory)
            programMemory.append(line)
        if(line[0] in movString):
            moveCommand(line,randomMemory)
            programMemory.append(line)
        if(line[0] in cmpString):
            compareList = compareCommand(line,randomMemory)
            programMemory.append(line)
        if(jmpString in line[0].lower()):
            jump(line,randomMemory,compareList)
            programMemory.append(line)
        if(line[0] in operationStrings):
            operationCommands(line,randomMemory)
        if not lineJump:
            line = infile.readline().split()
        else:
            tempLine = line
            line = programMemory[tempLine[1]]


if __name__ == '__main__':
    userInput = 'for_loop.ret 10'

    computer(userInput)