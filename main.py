def interrupt(userInput, memory):
    printString = ['print', 'PRINT']
    inputString = ['input','INPUT']
    brackString = '['
    if(userInput[1] in printString):
        if brackString in userInput[2]:
            print(memory[int(strip(userInput[2],'[]'))])
        else:
            printMessage = userInput[2:]
            print(' '.join(printMessage))
    elif(userInput[1] in inputString):
        intterruptInput = int(input(''))
        inputIndex = strip(userInput[2],'[]')
        memory[int(inputIndex)] = intterruptInput

def jump(userInput, memory, compareList):
    jlString = ['jl','JL']
    jgString = ['jg','JG']
    jeString = ['je','JE']
    jneString = ['jne','JNE']
    jgeString = ['jge','JGE']
    jleString = ['jle','JLE']
    if userInput[0] in jlString: # this is for jumping if less than. Returns 1 if values are less than each other
        if compareList[0]:
            return 1
    if userInput[0] in jgString: # this is for jumping if greater than. Returns 1 if both less than and equal to are false
        if not compareList[0] and not compareList[1]:
            return 1
    if userInput[0] in jeString: # this is for jumping if equal to. Returns 1 if the values are equal to each other
        if compareList[1]:
            return 1
    if userInput[0] in jneString: # this is for jumping if not equal to. Returns 1 if the values are not equal to each other
        if not compareList[1]:
            return 1
    if userInput[0] in jgeString: # this is is for jumping if greater than or equal to. Returns 1 if not less than or  equal to
        if not compareList[0] or compareList[1]:
            return 1
    if userInput[0] in jleString: # this is for jumping if less than or equal to. Returns 1 if values are less than or equal to
        if compareList[0] or compareList[1]:
            return 1
def operationCommands(userInput,memory):
    parameterOne = userInput[0]
    parameterTwo = userInput[1]
    parameterThree = userInput[2]
    parameterFour = userInput[3]
    addString = ['add','ADD']
    subString = ['sub','SUB']
    mulString = ['mul','MUL']
    divString = ['div','DIV']
    modString = ['mod','MOD']
    bracketString = '['
    locationOne = -1
    locationTwo = -1
    addedValue = -1
    if parameterOne in addString:
        if (bracketString in parameterThree) and (bracketString in parameterFour):
            locationOne = strip(parameterThree,'[]')
            locationTwo = strip(parameterFour,'[]')
            addedValue = memory[locationOne] + memory[locationTwo]
        elif(bracketString not in parameterThree and bracketString in parameterFour):
            locationTwo = strip(parameterFour,'[]')
            addedValue = int(parameterThree) + memory[locationTwo]
        elif(bracketString in parameterThree and bracketString not in parameterFour):
            locationOne = strip(parameterThree,'[]')
            addedValue = int(parameterFour) + memory[locationOne]
        else:
            addedValue = parameterThree + parameterFour
    memory[strip(parameterTwo,'[]')] = addedValue

def moveCommand(line,memory):
    bracketString = '['
    moveSource = line[2]
    moveDestination = int(strip(line[1] ,'[]' ))
    if (bracketString in moveSource):
        tempMoveSource = 0
        sourceValue = 0
        tempMoveSource = int(strip(line[2],'[]'))
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
        compareValue1 = int(strip(line[1],'[]'))
        compareValue2 = int(strip(line[2],'[]'))
        if memory[compareValue1] < memory[compareValue2]:
            lessThan = True
        elif memory[compareValue1] == memory[compareValue2]:
            equalTo = True
    else:
        compareValue1 = int(strip(line[1],'[]'))
        compareValue2 = int(line[2])
        if memory[compareValue1] < compareValue2:
            lessThan = True
        elif memory[compareValue1] == compareValue2:
            equalTo = True
    compareList.append(lessThan)
    compareList.append(equalTo)
    return compareList
# def runCommands(line,memory, programMemory, compareList):

def strip(string, value):
    returnValue = string.strip(value)
    return int(returnValue)

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
    instructionCounter = 0
    stopReading = False
    for x in range(int(userInput[1])):
        randomMemory.append(0)
    infile = open(userInput[0],'r')

    line = infile.readline().split()
    while not stopReading:
        if line[0] in haltString:
            programMemory.append(line)
            stopReading = True
        else:
            programMemory.append(line)
            line = infile.readline().split()

    while programMemory[instructionCounter] not in haltString:
        if haltString not in programMemory[instructionCounter]:
            line = programMemory[instructionCounter]
            if (programMemory[instructionCounter][0] in intString):
                interrupt(line,randomMemory)
                if instructionCounter + 1 < len(programMemory):
                    instructionCounter+=1
            elif(programMemory[instructionCounter][0] in movString):
                moveCommand(line,randomMemory)
                if instructionCounter + 1 < len(programMemory):
                    instructionCounter+=1
            elif(programMemory[instructionCounter][0] in cmpString):
                compareList = compareCommand(line,randomMemory)
                if instructionCounter + 1 < len(programMemory):
                    instructionCounter+=1
            elif(jmpString in programMemory[instructionCounter][0].lower()):
                if jump(line,randomMemory,compareList) == 1:
                    jumpLine = programMemory[instructionCounter][1]
                    instructionCounter = int(jumpLine)
                else:
                    if instructionCounter + 1 < len(programMemory):
                        instructionCounter+=1
            elif(programMemory[instructionCounter][0] in operationStrings):
                operationCommands(line,randomMemory)
                if instructionCounter + 1 < len(programMemory):
                    instructionCounter+=1


if __name__ == '__main__':
    userInput = 'fib.ret 20'

    computer(userInput)
