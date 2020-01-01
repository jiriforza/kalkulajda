def charsToString(charArray): 
    string = "" 
    for x in charArray: 
        string += x  
    return string 

print("Please input 2 nubers and an operation")
vstup = "none"
result = 0

vstup = str(input('-> '))
while(vstup != '0'):

    vstupCharArray = list(vstup)

    for x in range(len(vstup)):
        if vstupCharArray[x] == '+':
            op = 0
            opPosition = x						
        if vstupCharArray[x] == '-':
            op = 1
            opPosition = x
        if vstupCharArray[x] == '*':
            op = 2
            opPosition = x
        if vstupCharArray[x] == '/':
            op = 3
            opPosition = x


    leight2 = len(vstup) - (opPosition + 1)				

    firstNumString = [None] * opPosition
    secondNumString = [None] * leight2


    for x in range(opPosition):
        firstNumString[x] = vstupCharArray[x]
    firstNumString = charsToString(firstNumString)
    

    for x in range(leight2):
        secondNumString[x] = vstupCharArray[x + opPosition + 1]
    secondNumString = charsToString(secondNumString)



    if 'ans' in firstNumString or 'ANS' in firstNumString:
        firstInt = result
    else:
        firstInt = int(firstNumString)

    if 'ans' in secondNumString or 'ANS' in firstNumString:
        secondInt = result
    else:
        secondInt = int(secondNumString)



    if op == 0:																
        result = firstInt + secondInt
    elif op == 1:
        result = firstInt - secondInt
    elif op == 2:
        result = firstInt * secondInt
    elif op == 3:
        result = firstInt / secondInt
    
    



    print(result)

    vstup = str(input('-> '))