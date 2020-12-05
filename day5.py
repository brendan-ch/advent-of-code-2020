import time

def getSeatId(row, column):
  return row * 8 + column  # equation to determine seating ID

def getColumn(boardingPass):
  columns = list(range(0, 8))  # construct list of columns ([0, 1, 2, 3, ...])
  lastThree = boardingPass[-3:]  # get last three letters of boarding pass

  for letter in lastThree:
    # slice columns in half depending on letter
    if (letter == 'R'): columns = columns[int(len(columns) / 2):]
    elif (letter == 'L'): columns = columns[:int(len(columns) / 2)]

  # there should only be one value in columns, so we return that
  return columns[0]

# this and the columns function are very similar, might combine them into one later
def getRow(boardingPass):
  rows = list(range(0, 128))  # construct list of rows ([0, 1, 2, 3, ...])
  firstSeven = boardingPass[:7]  # get first seven letters of boarding pass

  for letter in firstSeven:
    # slice rows in half depending on letter
    if (letter == 'B'): rows = rows[int(len(rows) / 2):]
    elif (letter == 'F'): rows = rows[:int(len(rows) / 2)]

  # there should only be one value in columns, so we return that
  return rows[0]

def getHighestSeatingId(listPasses):
  # track highest ID here
  highestId = 0

  for item in listPasses:
    # get row and column to calculate ID
    row, column = getRow(item), getColumn(item)
    seatingId = getSeatId(row, column)
    # if ID is higher than existing one, we replace it
    if (seatingId > highestId): highestId = seatingId

  return highestId

def getMissingSeatingId(listPasses):
  seatingIds = []  # make a list of unique seat IDs
  missingId = 0  # track missing ID

  # construct list of seating IDs
  for item in listPasses:
    row, column = getRow(item), getColumn(item)
    seatingId = getSeatId(row, column)
    seatingIds.append(seatingId)

  # sort to easily access lowest and highest seat IDs
  seatingIds.sort()

  # count up from lowest seat id
  # every seat is filled, so only one missing seat
  for i in range(seatingIds[0], seatingIds[-1] + 1):
    if (not i in seatingIds):
      missingId = i
      break

  return missingId

if __name__ == "__main__":
  startTime = time.time()

  # read input file
  with open('inputFiles/day5.txt', 'r') as inputFile:
    inputText = inputFile.read()

  listPasses = inputText.split('\n')

  print("Highest seat ID:", getHighestSeatingId(listPasses))
  print("Missing seat ID:", getMissingSeatingId(listPasses))

  print(f"--- {time.time() - startTime} seconds ---")