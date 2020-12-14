import time

# get a value in directions based on direction (0, 90, 180, 270)
def getBaseDirection(direction):
  newDirection = direction
  while newDirection < 0 or newDirection > 270:
    newDirection += 360 if (newDirection < 0) else -360
  return newDirection

# jump table for actions, can be used for ship and waypoint
actions = {
  'N': lambda value, coords: [coords[0], coords[1] + value],
  'E': lambda value, coords: [coords[0] + value, coords[1]],
  'S': lambda value, coords: [coords[0], coords[1] - value],
  'W': lambda value, coords: [coords[0] - value, coords[1]],
}

def getManhattanDistShip(instructions: list):
  shipCoords = [0, 0]  # standard x-y coordinates
  direction = 90

  # table for direction value
  directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
  }

  # loop through instructions
  for instruction in instructions:
    value = int(instruction[1:]) # get value of action
    if (instruction[0] in actions): # move ship based on instr.
      shipCoords = actions[instruction[0]](value, shipCoords)
    elif (instruction[0] == 'F'):
      shipCoords = actions[directions[getBaseDirection(direction)]](value, shipCoords)
    else: # change direction based on instr.
      direction += value if (instruction[0] == 'R') else -value

  # return Manhattan distance
  return sum([abs(shipCoords[0]), abs(shipCoords[1])])

def getManhattanDistWaypoint(instructions: list):
  shipCoords = [0, 0]
  waypointCoords = [10, 1]

  getDistCoords = lambda coords1, coords2: [
    abs(coords1[0] - coords2[0]),
    abs(coords1[1] - coords2[1])
  ]

  # counterclockwise rotations
  rotateCoords = {
    0: lambda distCoords: distCoords,
    90: lambda distCoords: [-distCoords[1], distCoords[0]],
    180: lambda distCoords: [-distCoords[0], -distCoords[1]],
    270: lambda distCoords: [distCoords[1], -distCoords[0]],
    360: lambda distCoords: distCoords
  }

  for instruction in instructions:
    value = int(instruction[1:]) # get value of action
    if (instruction[0] in actions): # change waypoint coords
      waypointCoords = actions[instruction[0]](value, waypointCoords)
    elif (instruction[0] == 'F'): # change ship distance
      # distCoords = getDistCoords(shipCoords, waypointCoords)
      shipCoords[0] += waypointCoords[0] * value # multiply coords by value
      shipCoords[1] += waypointCoords[1] * value
    elif (instruction[0] == 'L'): # rotate counterclockwise
      # distCoords = getDistCoords(shipCoords, waypointCoords)
      waypointCoords = rotateCoords[getBaseDirection(value)](waypointCoords)
    elif (instruction[0] == 'R'):
      # distCoords = getDistCoords(shipCoords, waypointCoords)
      waypointCoords = rotateCoords[360 - getBaseDirection(value)](waypointCoords)

  return sum(getDistCoords(shipCoords, [0, 0]))

if __name__ == "__main__":
  startTime = time.time()
  with open('inputFiles/day12.txt', 'r') as inputFile:
    inputText = inputFile.read()

  instructions = inputText.split('\n')
  print("Manhattan distance from origin:", getManhattanDistShip(instructions))
  print("Manhattan distance from origin with waypoint:", getManhattanDistWaypoint(instructions))

  print(f"--- {time.time() - startTime} seconds ---")