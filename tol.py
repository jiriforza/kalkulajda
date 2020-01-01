def charsToString(charArray): 
    string = "" 
    for x in charArray: 
        string += x  
    return string 

print("please input 2 numbers and operation")
vstup = str(input('-> '))
print(vstup)
vstupCharArray = list(vstup)
print(vstupCharArray)

for x in range(len(vstup)):					#rozpoznání operace
    if vstupCharArray[x] == '+':
        op = 0
        opPosition = x						#souřadnice operace
    if vstupCharArray[x] == '-':
        op = 1
        opPosition = x
    if vstupCharArray[x] == '*':
        op = 2
        opPosition = x
    if vstupCharArray[x] == '/':
        op = 3
        opPosition = x
        
leight2 = len(vstup) - (opPosition + 1)				#leight2 délka druhého čísla (chars)

firstNumString = [None] * opPosition
secondNumString = [None] * leight2




for x in range(opPosition):												#rozdělení na dvě čísla do int 
    firstNumString[x] = vstupCharArray[x]
firstInt = int(charsToString(firstNumString))

for x in range(leight2): 												#rozdělení na dvě čísla do int 
    secondNumString[x] = vstupCharArray[x + opPosition + 1]
secondInt = int(charsToString(secondNumString))

if op == 0:																# operace
    result = firstInt + secondInt
elif op == 1:
    result = firstInt - secondInt
elif op == 2:
    result = firstInt * secondInt
elif op == 3:
    result = firstInt / secondInt

print(result)