import time

def parsePositions(criteria):
  hyphenIndex = criteria.find('-')
  spaceIndex = criteria.find(' ')

  first = int(criteria[0:hyphenIndex])
  second = int(criteria[hyphenIndex + 1:spaceIndex])
  letter = criteria[spaceIndex + 1]

  return (first, second, letter)

def checkIfValidPosition(criteria = ""):
  (first, second, letter) = parsePositions(criteria)

  firstPos = first - 1
  secondPos = second - 1

  passwordStr = criteria[criteria.find(' ') + 4:]

  return ((passwordStr[firstPos] == letter and passwordStr[secondPos] != letter) or (passwordStr[firstPos] != letter and passwordStr[secondPos] == letter))

def checkIfValidCount(criteria = ""):
  # majority of code will be in here

  (lowest, highest, letter) = parsePositions(criteria)

  # don't include first instance of letter
  count = criteria.count(letter) - 1

  return (lowest <= count and count <= highest)  # boolean expression

def getNumPasswordsValid(listPasswordsCriteria):
  passwordsValidCount = 0
  passwordsValidPos = 0

  for item in listPasswordsCriteria:
    if (checkIfValidCount(item)):
      passwordsValidCount += 1
    if (checkIfValidPosition(item)):
      passwordsValidPos += 1

  return (passwordsValidCount, passwordsValidPos)

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day2.txt', 'r') as inputFile:
    inputText = inputFile.read()

  inputList = inputText.split('\n')
  counts = getNumPasswordsValid(inputList)

  print("Policy #1:", counts[0])
  print("Policy #2:", counts[1])
  
  print(f"--- {time.time() - startTime} seconds ---")