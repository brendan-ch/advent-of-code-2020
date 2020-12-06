import time

def getListQuestionsAll(group):
  """Return the list of questions that anyone in the group answered "yes" to."""

  listQuestions = []

  for line in group.split('\n'):
    for letter in line:
      if (not letter in listQuestions): listQuestions.append(letter)

  return listQuestions

def getListQuestions(group):
  """Return the list of questions that everyone in the group answered "yes" to."""

  listQuestionsAll = []  # this will track all questions that at least one person answered "yes" to
  listQuestions = []  # this will track questions that all members of the group answered "yes" to

  groupMap = group.split('\n')

  for line in groupMap:
    for letter in line:
      if (not letter in listQuestionsAll): 
        listQuestionsAll.append(letter)  # start tracking letter
        listQuestions.append(letter)

    for letter in listQuestionsAll:  # remove items from listQuestions that aren't in all lines
      listConditionals = [letter in line for line in groupMap]

      if (not all(listConditionals) and letter in listQuestions):
        listQuestions.remove(letter)

  return listQuestions

def getSum(inputText):
  """Get both sums for both puzzles."""

  groups = inputText.split('\n\n')
  sumQuestions = 0
  sumQuestionsStrict = 0

  for group in groups:
    sumQuestions += len(getListQuestionsAll(group))
    sumQuestionsStrict += len(getListQuestions(group))

  return (sumQuestions, sumQuestionsStrict)

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day6.txt', 'r') as inputFile:
    inputText = inputFile.read()

  sumQuestions, sumQuestionsStrict = getSum(inputText)
  print("Sum of questions (part 1):", sumQuestions)
  print("Sum of questions (part 2):", sumQuestionsStrict)
  
  print(f"--- {time.time() - startTime} seconds ---")