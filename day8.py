import time

def runProgram(listInstructions):
  accumulator = 0
  executedInstructions = []  # track indices of executed and current instruction
  terminatedProperly = False
  currentInstruction = 0

  while not currentInstruction in executedInstructions:
    try:
      instructionText = listInstructions[currentInstruction]
    except:
      terminatedProperly = True
      break  # program has terminated; index doesn't exist

    executedInstructions.append(currentInstruction)
    
    if (listInstructions[currentInstruction][:3] == 'nop'): 
      # move to next instruction
      currentInstruction += 1
    elif (listInstructions[currentInstruction][:3] == 'acc'):
      accumulator += int(listInstructions[currentInstruction][4:])
      currentInstruction += 1
    elif (listInstructions[currentInstruction][:3] == 'jmp'):
      currentInstruction += int(listInstructions[currentInstruction][4:])

  return (accumulator, executedInstructions, terminatedProperly)  # we'll need the executed instructions to fix the program

def fixProgram(listInstructions, executedInstructions):
  fixedInstructions = list(listInstructions)
  reversedList = list(executedInstructions)
  reversedList.reverse()

  for i in reversedList:
    instruction = listInstructions[i][:3]

    if (instruction != "jmp" and instruction != "nop"): continue

    if (instruction == "jmp"):
      fixedInstructions[i] = f"nop {fixedInstructions[i][4:]}"
    elif (instruction == "nop"):
      fixedInstructions[i] = f"jmp {fixedInstructions[i][4:]}"

    if (runProgram(fixedInstructions)[2]):
      break
    else:
      fixedInstructions = list(listInstructions)  # we keep going

  return fixedInstructions

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day8.txt', 'r') as inputFile:
    inputText = inputFile.read()

  listInstructions = inputText.split('\n')
  (accumulator, executedInstructions, terminatedProperly) = runProgram(listInstructions)
  print('Accumulator value:', accumulator)

  fixedInstructions = fixProgram(listInstructions, executedInstructions)
  newAccumulator = runProgram(fixedInstructions)[0]
  print('Accumulator value (for fixed program):', newAccumulator)

  print(f'--- {time.time() - startTime} seconds ---')