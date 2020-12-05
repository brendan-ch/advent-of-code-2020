import time

def getPassportFields(passportStr):
  # return dict of passport fields
  reqFields = ["byr", "iyr", "eyr", "ecl", "pid", "hcl", "hgt"]
  passport = {}

  for line in passportStr.split('\n'):
    fields = line.split(' ')  # 'eyr:1990', 'cid:100', etc

    for field in fields:
      indexColon = field.find(':')
      
      fieldName = field[0:indexColon]
      fieldData = field[indexColon + 1:]
      
      if (fieldName in reqFields): passport[fieldName] = fieldData
  
  return passport

def validateDate(year, minDate, maxDate):  # used for byr, iyr, and eyr
  return int(year) >= minDate and int(year) <= maxDate

def validateHeight(height):
  validUnits = ['in', 'cm']
  
  if (len(height) <= 2):
    return False

  number = int(height[:-2])
  numberValid = (height[-2:] == "cm" and number >= 150 and number <= 193) or (height[-2:] == "in" and number >= 59 and number <= 76)

  return height[-2:] in validUnits and numberValid  # apparently this is valid syntax?

def validateHex(hexValue):  # used for hcl
  values = "#0123456789abcdef"
  validHex = True
  for i in hexValue:
    if (validHex == False): break  # if one hexValue is invalid then break

    validHex = i in values

  return len(hexValue) == 7 and hexValue[0] == "#" and validHex

def validateColor(color):
  listColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  return color in listColors

def validateId(passportId):
  values = '0123456789'
  validId = True
  for i in passportId:
    if (validId == False): break

    validId = i in values

  return validId and len(passportId) == 9

def getNumValidPassports(inputText):
  numValidPassports = 0
  numValidPassportsStrict = 0
  
  reqFields = ["byr", "iyr", "eyr", "ecl", "pid", "hcl", "hgt"]
  # if all seven fields are present, passport is valid

  passports = inputText.split('\n\n')

  for passport in passports:
    passportMap = getPassportFields(passport)

    if (len(passportMap) != len(reqFields)): continue
    else: numValidPassports += 1

    passportValid = (validateDate(passportMap['byr'], 1920, 2002) 
      and validateDate(passportMap['iyr'], 2010, 2020) 
      and validateDate(passportMap['eyr'], 2020, 2030) 
      and validateHeight(passportMap['hgt']) 
      and validateHex(passportMap['hcl']) 
      and validateColor(passportMap['ecl']) 
      and validateId(passportMap['pid']))

    if (passportValid): numValidPassportsStrict += 1

  return (numValidPassports, numValidPassportsStrict)


if __name__ == "__main__":
  startTime = time.time()
  
  with open("inputFiles/day4.txt", "r") as inputFile:
    inputText = inputFile.read()

  numValidPassports, numValidPassportsStrict = getNumValidPassports(inputText)
  print("Number of valid passports:", numValidPassports)
  print("Number of valid passports (strict):", numValidPassportsStrict)

  print(f"--- {time.time() - startTime} seconds ---")