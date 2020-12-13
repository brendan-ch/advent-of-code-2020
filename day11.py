import time

def runSimulationOnce(allSeats: list):
  # for every list in allSeats
  # for every seat in list
  # get all seats around seat
  # count # times occupied seat
  # make decision based on # times occupied seat (fill, empty, ignore)

  simulationData = allSeats[:]
  # surprisingly, this works
  getAllSeatsAround = lambda seatX, seatY, allSeats: "".join([
    row[max(0, seatX - 1):min(len(row), seatX + 2)]  # get all data around seat
    for row in allSeats[max(0, seatY - 1):min(len(allSeats), seatY + 2)]
  ]).replace(allSeats[seatY][seatX], "", 1)  # remove single occurence of seat

  for y in range(len(allSeats)):
    row = list(allSeats[y])

    for x in range(len(row)):
      if (row[x] == "."): continue  # floor never changes
      # passing allSeats instead of simulationData is important
      allSeatsAround = getAllSeatsAround(x, y, allSeats)
      countOccupied = allSeatsAround.count('#')
      
      if (countOccupied >= 4):
        row[x] = "L"
      elif (countOccupied == 0):
        row[x] = "#"
    
    simulationData[y] = "".join(row)

  return simulationData

def runSimulationFirstSeat(allSeats: list):
  def getSeatsInDirections(seatX: int, seatY: int, allSeats: list):
    seatExists = lambda coords, allSeats: (
      coords[1] >= 0 and coords[1] < len(allSeats) and
      coords[0] >= 0 and coords[0] < len(allSeats[coords[1]])
    )
    
    # list of coordinates around the seat
    listCoords = [
      (x, y) if (seatExists((x, y), allSeats)) else None
      for y in range(seatY - 1, seatY + 2)
      for x in range(seatX - 1, seatX + 2)
    ]
    listCoords.remove((seatX, seatY))

    lambdaDict = {
      0: (lambda coords: (coords[0] - 1, coords[1] - 1)),  # top left
      1: (lambda coords: (coords[0], coords[1] - 1)),  # directly above
      2: (lambda coords: (coords[0] + 1, coords[1] - 1)),  # top right
      3: (lambda coords: (coords[0] - 1, coords[1])),  # directly left
      4: (lambda coords: (coords[0] + 1, coords[1])),  # directly right
      5: (lambda coords: (coords[0] - 1, coords[1] + 1)),  # bottom left
      6: (lambda coords: (coords[0], coords[1] + 1)),  # directly below
      7: (lambda coords: (coords[0] + 1, coords[1] + 1))  # bottom right
    }

    seats = ['.' if (i) else None for i in listCoords]
    allSeatsFound = lambda seats: all([seat != '.' for seat in seats])

    # keep looping until all seats are truthy value
    while not allSeatsFound(seats):
      newSeats = seats[:]

      for i in range(len(listCoords)):
        if ((seats[i] == '.') and seatExists(listCoords[i], allSeats)): 
          newSeats[i] = allSeats[listCoords[i][1]][listCoords[i][0]]
        if (listCoords[i]): 
          listCoords[i] = lambdaDict[i](listCoords[i])

      if (all([not seatExists(i, allSeats) for i in listCoords if i])):
        break
        
      seats = newSeats

    # remove None values
    seats = [i for i in seats if i]

    return seats

  simulationData = allSeats[:]

  for y in range(len(allSeats)):
    row = list(allSeats[y])

    for x in range(len(row)):
      if (row[x] == "."): continue  # floor never changes
      # passing allSeats instead of simulationData is important
      allSeatsAround = getSeatsInDirections(x, y, allSeats)
      countOccupied = allSeatsAround.count('#')
      
      if (countOccupied >= 5):
        row[x] = "L"
      elif (countOccupied == 0):
        row[x] = "#"
    
    simulationData[y] = "".join(row)

  return simulationData

def returnFinalSeating(allSeats: list):
  # run simulation a bunch of times
  simulationData = [allSeats[:], allSeats[:]]

  # run simulation #1
  while 1:
    newSimulationData = runSimulationOnce(simulationData[0])
    if (newSimulationData == simulationData[0]): break
    simulationData[0] = newSimulationData

  print("First simulation finished.")

  while 1:
    newSimulationData = runSimulationFirstSeat(simulationData[1])
    if (newSimulationData == simulationData[1]): break
    simulationData[1] = newSimulationData

  print("Second simulation finished.")

  return simulationData

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day11.txt', 'r') as inputFile:
    inputText = inputFile.read()

  allSeats = inputText.split('\n')

  finalSeating = returnFinalSeating(allSeats)

  countSeats = lambda seatType, allSeats: "".join(allSeats).count(seatType)
  print("Number of occupied seats (simulation #1):", countSeats("#", finalSeating[0]))
  print("Number of occupied seats (simulation #2):", countSeats('#', finalSeating[1]))

  print(f"--- {time.time() - startTime} seconds ---")