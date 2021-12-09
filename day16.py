import time

def getBounds(inputList: "list[str]"):
  """Get the valid values for the ticket."""
  # Get all lines before "your ticket"
  indexBounds = inputList.index("your ticket:")
  boundsData = inputList[:indexBounds]

  result: "list[tuple[int]]" = []

  for line in boundsData:
    indexColon = line.index(":")
    boundsStrList = line[indexColon + 1:].split(" or ")

    for bounds in boundsStrList:
      boundsSplit = bounds.split("-")
      result.append((int(boundsSplit[0]), int(boundsSplit[1])))

  return result

def getCodedBounds(inputList: "list[str]"):
  """Get the marked valid values for the ticket."""

  indexBounds = inputList.index("your ticket:")
  boundsData = inputList[:indexBounds]

  result: "dict" = {}

  for line in boundsData:
    indexColon = line.index(":")
    boundsStrList = line[indexColon + 1:].split(" or ")
    code = line[:indexColon]

    boundsOfCode: "list[tuple[int]]" = []

    for bounds in boundsStrList:
      boundsSplit = bounds.split("-")
      boundsOfCode.append((int(boundsSplit[0]), int(boundsSplit[1])))

    result[code] = boundsOfCode

  return result

def getNearbyTickets(inputList: "list[str]"):
  """Return a list of tuples representing the nearby tickets."""
  indexNearbyTickets = inputList.index("nearby tickets:")
  nearbyTicketData = inputList[indexNearbyTickets + 1:]

  result: "list[tuple[int]]" = []

  for line in nearbyTicketData:
    result.append(tuple([int(x) for x in line.split(",")]))

  return result

def getYourTicket(inputList: "list[str]"):
  """Return the ticket marked under 'your ticket'."""

  indexNearbyTickets = inputList.index("your ticket:")
  yourTicket = [int(x) for x in inputList[indexNearbyTickets + 1].split(",")]

  return yourTicket

def getValuesOfNearbyTickets(inputList: "list[str]"):
  """Return a list of ints with the nearby ticket values."""
  indexNearbyTickets = inputList.index("nearby tickets:")
  nearbyTicketData = inputList[indexNearbyTickets + 1:]

  result: "list[int]" = []
  for line in nearbyTicketData:
    result += [int(x) for x in line.split(",")]
  
  return result

def getErrorRate(inputList: "list[str]"):
  """Calculate and return the error rate of the nearby tickets."""
  bounds = getBounds(inputList)
  nearbyTicketData = getValuesOfNearbyTickets(inputList)

  invalidValues: "list[int]" = []

  for i in nearbyTicketData:
    valid = False

    for boundsData in bounds:
      if (i >= boundsData[0] and i <= boundsData[1]):
        valid = True

    if (not valid):
      invalidValues.append(i)

  return sum(invalidValues)

def getCodedTicket(inputList: "list[str]"):
  """Return the ticket with the fields marked."""

  bounds = getBounds(inputList)
  nearbyTicketData = getNearbyTickets(inputList)
  validatedTicketData: "list[tuple[int]]" = []

  # Remove nearby tickets with invalid fields
  for ticket in nearbyTicketData:
    invalidValues = []

    for i in ticket:
      valid = False
      for boundsData in bounds:
        if (i >= boundsData[0] and i <= boundsData[1]):
          valid = True

      if (not valid):
        # validatedTicketData.append(ticket)
        invalidValues.append(i)

    if (len(invalidValues) == 0):
      validatedTicketData.append(ticket)

  codedBounds = getCodedBounds(inputList)

  columnData: "list[list[int]]" = []

  # Index of the column
  for i in range(len(validatedTicketData[0])):
    columnData.append([])

    for ticket in validatedTicketData:
      columnData[i].append(ticket[i])

  remainingBounds: "list[str]" = list(codedBounds.keys())

  isInBounds = lambda num, bounds : (num >= bounds[0][0] and num <= bounds[0][1]) or (num >= bounds[1][0] and num <= bounds[1][1])

  yourTicket = getYourTicket(inputList)
  codedTicket = {}

  # Go through each column of validated ticket data
  while len(remainingBounds) > 0:
    for column in columnData:
      possibleBounds = remainingBounds.copy()
      
      for i in column:
        for bound in possibleBounds.copy():
          if (not isInBounds(i, codedBounds[bound])):
            possibleBounds.remove(bound)
      
      # May not be true on first run
      if (len(possibleBounds) == 1):
        # Put in coded ticket
        codedTicket[possibleBounds[0]] = yourTicket[columnData.index(column)]
        
        # Remove from remaining bounds
        remainingBounds.remove(possibleBounds[0])

  return codedTicket

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day16.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [x for x in inputFromFile.split("\n") if x]

  errorRate = getErrorRate(inputList)
  print(f"Error rate of nearby tickets: {errorRate}")
  
  codedTicket = getCodedTicket(inputList)
  departureValues = [codedTicket[field] for field in list(codedTicket.keys()) if field.startswith("departure")]

  product = 1
  for i in departureValues:
    product *= i

  print(f"Product of departure values: {product}")

  print(f"--- {time.time() - startTime} seconds ---")