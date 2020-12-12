def getDifferences(inputList: list):
  listAdapters = inputList[:]
  listAdapters.sort()
  differences1jolt = 0
  differences3jolts = 0
  currentJolts = 0

  for i in listAdapters:
    if (i - currentJolts == 1): differences1jolt += 1
    elif (i - currentJolts == 3): differences3jolts += 1

    currentJolts = i

  differences3jolts += 1

  return (differences1jolt, differences3jolts)

def getNumWays(inputList: list):
  listAdapters = inputList[:]
  listAdapters.append(0)
  listAdapters.sort()
  numWays = 1

  consecutiveNums = []
  continueAt = 0

  # count and append consecutive numbers here
  for i in range(len(listAdapters)):
    # i'm gonna have a fucking stroke
    if (i < continueAt): 
      continue

    tracker = []
    isConsecutive = True
    iterator = i

    while isConsecutive and iterator < len(listAdapters):
      if (len(tracker) == 0 or listAdapters[iterator] == tracker[-1] + 1): 
        tracker.append(listAdapters[iterator])
      else: isConsecutive = False
      iterator += 1

    iterator -= 1

    if (len(tracker) > 1): 
      consecutiveNums.append(tracker)
      continueAt = iterator

  for i in consecutiveNums:
    numWays *= (2 ** (len(i) - 2)) - max(0, -9 + (len(i) * 2))

  print(consecutiveNums)

  return numWays

if __name__ == "__main__":
  with open('inputFiles/day10.txt', 'r') as inputFile:
    inputText = inputFile.read()

  inputList = [int(x) for x in inputText.split('\n') if x]
  differences = getDifferences(inputList)
  numWays = getNumWays(inputList)

  multiple = 1
  for i in differences:
    multiple *= i

  print("Multiplied differences:", multiple)
  print("Number of ways:", numWays)