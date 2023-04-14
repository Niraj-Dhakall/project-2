"""
File:         retriever_asm.py
Author:       Niraj Dhakal
Date:         4/13/2023
Section:      16
E-mail:       nirajd1@umbc.edu
Description: simulate a very simplified computer running a very simplified assembly language which is modeled after the
x86 assembly language.

"""



'''
The intterupt() funtion is used to run the INT command. This function takes in the userInput, which in this case is the
line and takes in the ram. Then it checks if the command after INT is PRINT. If it is then it will check if the command
after PRINT has brackets or not. If it does then it will print the value in RAM at that given index, else it will print
the value. If the command after INT is INPUT then it will prompt an input from the user and store it in the given index
in RAM
'''
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
        intterruptInput = int(input('>>> '))
        inputIndex = strip(userInput[2],'[]')
        memory[int(inputIndex)] = intterruptInput
'''
The jump() function is used to jump lines. It takes in the user input, the RAM, and a list that has two
bools from the compare() function. The first bool representing lessThan, the second equalTo. The jump
function then will check the command against seven different conditions and will return 1 if the condition(s)
are met. 
'''
def jump(userInput, memory, compareList):
    jlString = ['jl','JL']
    jgString = ['jg','JG']
    jeString = ['je','JE']
    jneString = ['jne','JNE']
    jgeString = ['jge','JGE']
    jleString = ['jle','JLE']
    jmpString = ['jmp','JMP']
    # compare list in the format : lessThan, equalTo
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
    if userInput[0] in jmpString:
        print("jump 5 just happened")
        return 1
'''
The operationCommands() function represents addition, subtraction, multiplication, division, and modulus operations.
It takes in the userInput and RAM. Then it checks if the command given in the userInput is either of the different
operators. It then checks for the four different cases for each command. An example command could be: ADD [1] [1] 1 

It then checks for the different conditions being:
[location1][location2]
value [location2]
[location1] value
value value

And do the operations correctly depending on the conditon.

'''
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
    printValue = -1
    if parameterOne in addString:
        if (bracketString in parameterThree) and (bracketString in parameterFour):
            locationOne = strip(parameterThree,'[]')
            locationTwo = strip(parameterFour,'[]')
            printValue = memory[locationOne] + memory[locationTwo]
        elif(bracketString not in parameterThree and bracketString in parameterFour):
            locationTwo = strip(parameterFour,'[]')
            printValue = int(parameterThree) + memory[locationTwo]
        elif(bracketString in parameterThree and bracketString not in parameterFour):
            locationOne = strip(parameterThree,'[]')
            printValue = int(parameterFour) + memory[locationOne]
        else:
            printValue = int(parameterThree) + int(parameterFour)
    elif parameterOne in subString:
        if (bracketString in parameterThree) and (bracketString in parameterFour): # this is [location1] - [location2]
            locationOne = strip(parameterThree,'[]')
            locationTwo = strip(parameterFour,'[]')
            printValue = memory[locationOne] - memory[locationTwo]
        elif(bracketString not in parameterThree and bracketString in parameterFour): # this is value1 (parameter3) - (p4)[location2]
            locationTwo = strip(parameterFour,'[]')
            printValue =  int(parameterThree) - memory[locationTwo]
        elif(bracketString in parameterThree and bracketString not in parameterFour):# this is [location1](parameter3) - value2(p4)
            locationOne = strip(parameterThree,'[]')
            printValue = memory[locationOne] - int(parameterFour)
        else:
            printValue = parameterFour - parameterThree
    elif parameterOne in mulString:
        if (bracketString in parameterThree) and (bracketString in parameterFour):
            locationOne = strip(parameterThree,'[]')
            locationTwo = strip(parameterFour,'[]')
            printValue = memory[locationOne] * memory[locationTwo]
        elif(bracketString not in parameterThree and bracketString in parameterFour):
            locationTwo = strip(parameterFour,'[]')
            printValue = int(parameterThree) * memory[locationTwo]
        elif(bracketString in parameterThree and bracketString not in parameterFour):
            locationOne = strip(parameterThree,'[]')
            printValue = parameterFour * memory[locationOne]
        else:
            printValue = parameterThree * parameterFour
    elif parameterOne in divString:
        if (bracketString in parameterThree) and (bracketString in parameterFour):
            locationOne = strip(parameterThree,'[]')
            locationTwo = strip(parameterFour,'[]')
            if memory[locationTwo] != 0: # checks if second value is zero or not
                printValue = memory[locationOne] // memory[locationTwo]
        elif(bracketString not in parameterThree and bracketString in parameterFour):
            locationTwo = strip(parameterFour,'[]')
            if memory[locationTwo] != 0:
                printValue = int(parameterThree) // memory[locationTwo]
        elif(bracketString in parameterThree and bracketString not in parameterFour):
            locationOne = strip(parameterThree,'[]')
            if int(parameterFour) != 0:
                printValue = memory[locationOne] // int(parameterFour)
        else:
            if int(parameterFour) != 0:
                printValue = parameterThree // parameterFour
    elif parameterOne in modString:
        if (bracketString in parameterThree) and (bracketString in parameterFour):
            locationOne = strip(parameterThree,'[]')
            locationTwo = strip(parameterFour,'[]')
            printValue = memory[locationOne] % memory[locationTwo]
        elif(bracketString not in parameterThree) and (bracketString in parameterFour):
            locationTwo = strip(parameterFour,'[]')
            printValue = int(parameterThree) % memory[locationTwo]
        elif(bracketString in parameterThree) and (bracketString not in parameterFour):
            locationOne = strip(parameterThree,'[]')
            printValue = memory[locationOne] % int(parameterFour)
        else:
            printValue = parameterThree % parameterFour

    memory[strip(parameterTwo,'[]')] = printValue
'''
The moveCommand() function is used to move values within RAM. 
It checks if the last parameter has brackets or not and 
if it does have a bracket, will move according to the index 
given in the parameters. If no brackets are given, it will
move the given value to the index that is given following 
the MOV command.
'''
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
'''
The compareCommand() is used to compare two given value or indexes of RAM.
It takes in the line and the RAM and return a list that has two bools.
In the form of [bool1, bool2] where bool1 represents if the value1 is 
less than value2. And bool2 where it represents if value1 is equal to value2
'''
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

'''
This function is used to remove a given value from a string and return the given string as an int.
'''
def strip(string, value):
    returnValue = string.strip(value)
    return int(returnValue)
'''
This is the main function that acts as the computer. It checks the line command given against all the 
avaliable commands and calls the correct functions for the commands.

[randomMemory] - this is the RAM of the computer, it is a list that first starts off with value all equal to 0
[programMemory] - this is the program memory that stores all the commands from the file
[halt,cmp,mov,operation,j,cmp,int] string lists- these are all the lists for the commands that can be run in the program
[compareList] - this is used to hold the return of the compareCommand() function
[instructionCounter] - this keeps track of which line in programMemory we have ran. Each time a command is run, this
incrememts up one.

'''
def computer(userInput):
    userInput = userInput.split()
    randomMemory = []
    programMemory = []
    haltString = 'hlt'
    compareList = []
    cmpString = ['cmp','CMP']
    movString = ['mov','MOV']
    operationStrings = ['mod','MOD','div','DIV','mul','MUL','sub','SUB','add','ADD']
    jString = 'j'
    cmpString = ['cmp','CMP']
    intString = ['int','INT']
    instructionCounter = 0
    stopReading = False
    keepRunning = True
    for x in range(int(userInput[1])): # initializes the RAM to specified size
        randomMemory.append(0)
    infile = open(userInput[0],'r')

    line = infile.readline().split()
    while not stopReading:
        if haltString in line[0].lower():
            programMemory.append(line)
            stopReading = True
        else:
            programMemory.append(line)
            line = infile.readline().split()


    while keepRunning:
        line = programMemory[instructionCounter]
        print(programMemory[instructionCounter])
        if (programMemory[instructionCounter][0] in intString): # for interrupt command
            interrupt(line,randomMemory)
            if instructionCounter + 1 < len(programMemory):
                instructionCounter+=1
        elif(programMemory[instructionCounter][0] in movString):# for move command
            moveCommand(line,randomMemory)
            if instructionCounter + 1 < len(programMemory):
                instructionCounter+=1
        elif(programMemory[instructionCounter][0] in cmpString):# for compare command
            compareList = compareCommand(line,randomMemory)
            if instructionCounter + 1 < len(programMemory):
                instructionCounter+=1
        elif(jString in programMemory[instructionCounter][0].lower()): # for jumping commands
            if jump(line,randomMemory,compareList) == 1: # if condition for jump is met, this runs
                jumpLine = programMemory[instructionCounter][1]
                print("jump just happened")
                instructionCounter = int(jumpLine)
            else:
                if instructionCounter + 1 < len(programMemory): # if condition for jump is not met, this run
                    instructionCounter+=1
        elif(programMemory[instructionCounter][0] in operationStrings): # for the operation: add,sub,mul,div,mod
            operationCommands(line,randomMemory)
            if instructionCounter + 1 < len(programMemory):
                instructionCounter+=1
        if haltString in programMemory[instructionCounter][0].lower():
            keepRunning = False
            infile.close()





if __name__ == '__main__':
    userInput = input("What file should we assemble, and what size of ram should we use? ")
    computer(userInput)
