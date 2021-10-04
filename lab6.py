# data for Task1
rList = [[1, 10, 9, 4, 50],[3, 40, 99, 37, 5, 1],[8, 11, 10, 94],[100, 9, 2, 88, 44],[4, 9, 2, 19]]

# data for Task 2
encodedData1 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')],
                [(9, ' '), (3, '8'), (1, 'l')], [(8, ' '), (1, 'j'), (4, '8'), (1, '.')],
                [(7, ' '), (1, '.'), (6, '8'), (1, '.')], [(6, ' '), (1, '.'), (8, '8'), (1, '.')],
                [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
                [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')],
                [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')], [(1, '.'), (21, '8')], [(22, '8')],
                [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
                [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'),
                 (1, "'")],
                [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'),
                 (1, '-'), (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'),
                 (1, 'h')]]
encodedData2 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')],
                [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')],
                [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'),
                 (3, ' '), (2, '|'), (17, '.')],
                [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'),
                 (7, '.'), (7, ' '), (3, '.')],
                [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'),
                 (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')],
                [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'),
                 (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')],
                [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'),
                 (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')],
                [(52, '.')]]

# data for Task 3
stringData = "1 H Hydrogen,2 He Helium,3 Li Lithium,4 Be Beryllium,5 B Boron,6 C Carbon,7 N Nitrogen,8 O Oxygen,9 F Fluorine,10 Ne Neon,11 Na Sodium,12 Mg Magnesium,13 Al Aluminum,14 Si Silicon,15 P Phosphorus,16 S Sulfur,17 Cl Chlorine,18 Ar Argon,19 K Potassium,20 Ca Calcium,21 Sc Scandium,22 Ti Titanium,23 V Vanadium,24 Cr Chromium,25 Mn Manganese"

def printRaggedList(listitem):
    count = 1
    print("Unsorted List")
    for x in listitem:
        print(f"Row {count}:{x}")
        count=count+1

def sortRaggedList(listitem):
    count = 1
    print("\nSorted List")
    for x in listitem:
        x.sort()
        print(f"Row {count}:{x}")
        count=count+1

def decodeTupleList(tuplelist):
    x = len(tuplelist)
    emptystr = ""
    for j in range(x):
        multipier = tuplelist[j][0]
        letter = tuplelist[j][1]
        string = multipier * letter
        emptystr = emptystr + string
    print(emptystr)

def printEncodedAsciiImage(decodedlist):
    x = len(decodedlist)
    for rows in range(x):
        decodeTupleList(decodedlist[rows])

def buildElementDictionary(string):
    emptydict = {}
    first_split = string.split(sep=",")
    joiner = ' '.join([str(elem) for elem in first_split])
    finalsplit = joiner.split()
    numbersonly = finalsplit[::3]
    clone = finalsplit
    symbolsandelements = [x for x in clone if x not in numbersonly]
    clone2 = symbolsandelements
    symbolsonly = symbolsandelements[::2]
    elements = [x for x in clone2 if x not in symbolsonly]
    for x in range(len(elements)):
        emptydict[symbolsonly[x]] = [elements[x],numbersonly[x]]
    return emptydict

def printElements(dict):
    for sym, elem in dict.items():
        print(f"{sym} [{elem[0]}] #{elem[1]}")

def main():
    print("Task 1 - Sorting and printing a ragged list")
    printRaggedList(rList)
    sortRaggedList(rList)
    print("\nTask 2 - Decoding Ascii Art")
    printEncodedAsciiImage(encodedData1)
    printEncodedAsciiImage(encodedData2)
    print("\nTask 3 - Elements String to Dictionary")
    stringdictionary = buildElementDictionary(stringData)
    printElements(stringdictionary)
    input()

if __name__=="__main__":
    main()