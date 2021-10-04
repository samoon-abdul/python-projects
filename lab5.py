from random import choice,randint
global testDict

# names, cities tuples are given
names = ("Masha", "Kevin", "Ruigang", "Vlad", "Ramesh", \
         "Aditi", "Caroline", "Panos", "Chuck", "Grani", \
         "Rutha", "Stan", "Qiong", "Alexi", "Carlos")
cities = ("Toronto", "Ottawa", "Hamilton")

# test dictionary  given - only two cities, 4 people
testDict = {"Richard": "Toronto", "Jia-Tao": "Toronto", "Justin": "Ottawa", "Lars": "Ottawa"}


def getRandomItem(item):
    return choice(item)

def createNameDictionary():
    global testDict
    testDict = {}
    for x in range(len(names)):
        y = getRandomItem(cities)
        testDict.update({names[x]:y})
    return testDict

def fromCity(stringvalue,dict):
    empty_list = []
    for key, value in dict.items():
        if stringvalue == value:
            empty_list.append(key)
    return empty_list

def printNameDict(dict,tuple):
    x = len(tuple)
    toronto_list = []
    hamilton_list = []
    ottawa_list = []
    if x == 3:
        for x in tuple:
            if x == "Toronto":
                for key, value in dict.items():
                    if x == value:
                        toronto_list.append(key)
            elif x == "Hamilton":
                for key, value in dict.items():
                    if x == value:
                        hamilton_list.append(key)
            elif x == "Ottawa":
                for key, value in dict.items():
                    if x == value:
                        ottawa_list.append(key)
        if len(toronto_list) == 0:
            blankcity("Toronto")
            mainprint("Ottawa",ottawa_list)
            blankcity("Hamilton")
        else:
            mainprint("Toronto", toronto_list)
            mainprint("Ottawa", ottawa_list)
            mainprint("Hamilton", hamilton_list)
    elif x == 2:
        toronto_list = []
        ottawa_list = []
        for x in tuple:
            if x == "Toronto":
                for key, value in dict.items():
                    if x == value:
                        toronto_list.append(key)
            elif x == "Ottawa":
                for key, value in dict.items():
                    if x == value:
                        ottawa_list.append(key)
        if len(ottawa_list) == 0:
            mainprint("Toronto",toronto_list)
            blankcity("Ottawa")
        else:
            mainprint("Toronto", toronto_list)
            mainprint("Ottawa", ottawa_list)

#function to print out cities that aren't blank
def mainprint(city, list):
    print(f"People from {city}:")
    for i, item in enumerate(list, 1):
        print(i, '. ' + item, sep='', end='\n')

#function to print out cities that are blank
def blankcity(city):
    print(f"People from {city}:")
    print("*None*")

def removePeopleFrom(diction,string):
    new = {key: val for key, val in diction.items() if val != string}
    global testDict
    testDict = new

def main():
  # part 1 (Function testing)
  print("Part 1 - Testing functions with `testDict' \n")
  print("Testing getRandomItem() function")
  print(cities)
  test_1_item = getRandomItem(cities)
  print(f"Item = {test_1_item}")
  print("\nTesting fromCity() function")
  print(fromCity("Toronto",testDict))
  print(fromCity("Ottawa",testDict))
  print("\nTesting printNameDict() function")
  printNameDict(testDict,("Toronto", "Ottawa",))
  print("\nTesting removePeopleFrom() function")
  removePeopleFrom(testDict,"Ottawa")
  printNameDict(testDict,("Toronto", "Ottawa",))

  # part 2 (Main program with generated Dictionary)
  print("\nPart 2 - Main\n")
  createNameDictionary()
  printNameDict(testDict,cities)
  print("\nPeople from Toronto:")
  print(fromCity("Toronto",testDict))
  print("\nPeople from Ottawa:")
  print(fromCity("Ottawa",testDict))
  print("\nPeople from Hamilton:")
  print(fromCity("Hamilton",testDict))
  print("\nRemoving all people from Toronto")
  print("Removing all people from Hamilton")
  removePeopleFrom(testDict,"Toronto")
  removePeopleFrom(testDict,"Hamilton")
  printNameDict(testDict,("Toronto", "Ottawa","Hamilton"))
  input("Press enter to exit: ")


if __name__=="__main__":
    main()
