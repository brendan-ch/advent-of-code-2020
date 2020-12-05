import time

def countTrees(inputList, right, down = 1):
  count = 0

  trackRight = 0
  trackDown = down - 1  # might delete this later

  for item in inputList:
    trackDown += 1

    if (down - trackDown != 0):
      continue
    
    trackDown = 0
    
    if (len(item) <= trackRight):
      trackRight -= len(item)  # reset position to start

    spot = item[trackRight]

    if (spot == "#"):
      count += 1
    
    trackRight += right

  return count

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day3.txt', 'r') as inputFile:
    inputText = inputFile.read()
  inputList = inputText.split('\n')

  # count = countTrees(inputList, 3)
  counts = (countTrees(inputList, 1), countTrees(inputList, 3), countTrees(inputList, 5), countTrees(inputList, 7), countTrees(inputList, 1, 2))

  multipliedTrees = 1
  for i in counts:
    multipliedTrees *= i

  print("Trees according to first criteria:", counts[1])
  print("Multiplied trees:", multipliedTrees)

  print(f"--- {time.time() - startTime} seconds ---")
  