import time

def constructRuleDict(rule: str):
  """Construct a dictionary containing bag color and the bags that it can contain"""
  ruleArgs = rule.split(' ')

  # get list of bags as sublists
  # take everything after word 'contains', split it using commas
  bags = [bag.split(' ') for bag in rule[rule.find('contain') + 8:].split(', ')]
  
  # construct rule dictionary
  ruleDict = {
    "color": " ".join(ruleArgs[:2]),
    "contains": [{
      "color": " ".join(bag[1:3]),
      "quantity": int(bag[0])
    } for bag in bags if bag[0] != 'no']
  }  

  return ruleDict

def searchForOptions(bagColor: str, ruleDicts: list):
  """Search the rule to see if it contains bagColor. 
  Returns list of bags that match the bagColor."""
  # this function takes significantly less time to run than the previous algorithm used.

  # lambda returns boolean depending on whether rule has color
  contains = lambda rule, color: len([bag for bag in rule['contains'] if (bag['color'] == color)]) != 0

  # for every rule, runs lambda to see if bag color exists directly inside rule
  listRulesWithColor = lambda color, rules: [rule for rule in rules
    if (contains(rule, color))
  ]

  # store rules directly (and indirectly) containing bagColor
  ruleDictsContainingColor = listRulesWithColor(bagColor, ruleDicts)

  # we need to append rules that indirectly contain bagColor to ruleDictsContainingColor
  # to do this, we need to loop through each rule in ruleDictsContainingColor,
  # and append rules containing that color to ruleDictsContainingColor.
  for x in ruleDictsContainingColor:
    # we iterate through rules that directly contain the color of x
    for y in listRulesWithColor(x['color'], ruleDicts):
      if (not y in ruleDictsContainingColor): 
        ruleDictsContainingColor.append(y)  # ...and append that rule.
      # if there are no rules, this for statement won't run

  return ruleDictsContainingColor

def getNumBagColors(bagColor: str, ruleDicts: list):
  """Get the number of bag colors that can contain at least one bagColor."""
  matchingRuleDicts = searchForOptions(bagColor, ruleDicts)

  return len(matchingRuleDicts)

def getNumBagsReq(bagColor: str, ruleDicts: list):
  """Get the number of required bags inside a single bag."""
  numBagsReq = 0

  # get the initial ruleDict that we need to check
  initialBag = [ruleDict for ruleDict in ruleDicts if ruleDict['color'] == bagColor][0]
  initialBag['quantity'] = 1  # only check the initial dict once

  # shit to track
  listRuleDicts = [initialBag]

  for ruleDictToSearch in listRuleDicts:
    for bag in ruleDictToSearch['contains']:
      numBagsReq += bag['quantity']  # add the bag quantity (# of bags)

      # search for the bag that we need to check later
      bagToAppend = [ruleDict for ruleDict in ruleDicts if (ruleDict['color'] == bag['color'])][0]

      # we want to check # of req. bags for each bag, so we add it to the tracker
      # loop x number of times based on quantity of bag
      for i in range(bag['quantity']):
        listRuleDicts.append(bagToAppend)

  return numBagsReq

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day7.txt', 'r') as inputFile:
    inputText = inputFile.read()

  rules = inputText.split('\n')
  ruleDicts = [constructRuleDict(ruleStr) for ruleStr in rules]
  print(f'--- {time.time() - startTime} seconds: constructed ruleDicts ---')

  numBagColors = getNumBagColors('shiny gold', ruleDicts)
  print(f'--- {time.time() - startTime} seconds: got numBagColors')
  
  print('Number of bag colors:', numBagColors)

  numBagsReq = getNumBagsReq('shiny gold', ruleDicts)
  print(f'--- {time.time() - startTime} seconds: got numBagsReq')
  print('Number of bags required:', numBagsReq)