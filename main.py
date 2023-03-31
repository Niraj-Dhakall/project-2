def computer(userInput):
    userInput = userInput.split()
    programMemory = []
    randomMemory = []
    for x in range(int(userInput[1])):
        randomMemory.append("0")
    print(randomMemory)



if __name__ == '__main__':
    userInput = input("What file should we assemble, and what size of ram should we use?")
    computer(userInput)