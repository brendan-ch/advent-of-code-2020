import time

def findTwoEntriesProduct(listNum = [], sum = 0):
  # returns product of first numbers that add to sum

  for i in listNum:
    for j in listNum:
      if (i + j == sum):
        return i * j

def findThreeEntriesProduct(listNum = [], sum = 0):
  # returns tuple with first numbers that add to sum
  # what the fuck is this
  # my python knowledge is failing me

  for i in listNum:
    for j in listNum:
      for k in listNum:
        if (i + j + k == sum):
          return i * j * k

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day1.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [int(x) for x in inputFromFile.split('\n') if x]
  twoEntries = findTwoEntriesProduct(inputList, 2020)
  threeEntries = findThreeEntriesProduct(inputList, 2020)
  
  print("Two entries:", twoEntries)
  print("Three entries:", threeEntries)
  
  print("--- %s seconds ---" % (time.time() - startTime))