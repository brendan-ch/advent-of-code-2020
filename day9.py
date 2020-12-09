import time

def findFirstNumber(numbers: list, preambleLength: int):
  number = 0
  
  for i in range(len(numbers)):
    # loop to next number if preamble (skip)
    if (preambleLength > i): continue
    
    # function to check if number is sum of 2 numbers in prevNumbers
    def checkIfSum(number: int, prevNumbers: list):
      for x in prevNumbers:
        for y in prevNumbers:
          if (x + y == number and x != y): return True

      return False
    
    if (not checkIfSum(numbers[i], numbers[i - preambleLength:i])):
      number = numbers[i]
      break

  return number

def findEncryptionWeakness(number: int, numbers: list):
  # amount of indices to "go back"
  crawlerIndex = 1
  # contiguous set of numbers in list
  contiguousNumbers = []

  while (len(contiguousNumbers) == 0):
    for i in range(crawlerIndex, numbers.index(number)):
      if (sum(numbers[i - crawlerIndex:i + 1]) == number):
        contiguousNumbers = numbers[i - crawlerIndex:i + 1]

    # if we don't find the number, we increment the crawlerIndex by 1 and try again
    crawlerIndex += 1

  contiguousNumbers.sort()
  return contiguousNumbers[0] + contiguousNumbers[-1]

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day9.txt', 'r') as inputFile:
    inputText = inputFile.read()

  # get list of integers
  numbers = [int(x) for x in inputText.split('\n')]
  number = findFirstNumber(numbers, 25)
  encryptionWeakness = findEncryptionWeakness(number, numbers)
  print("First number:", number)
  print("Encryption weakness:", encryptionWeakness)

  print(f"--- {time.time() - startTime} seconds ---")