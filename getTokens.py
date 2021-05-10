import re
from symbols import keywords,delimiters,operators,symbols,numerals
def isDelimiter(ch):
    if ch in delimiters:return (True)
    return (False)
def isOperator(ch):
    if ch in operators:return (True)
    return (False)
def validIdentifier(str):
    if str[0] in numerals or isDelimiter(str[0]) == True:return (False)
    return (True)
def isKeyword(str):
    if str in keywords:return (True)
    return (False)
def isInteger(str):
    length = len(str)
    if (length == 0):return (False)
    for i in range(0, length):
        if not str[i] in numerals or (str[i] == '-' and i > 0):return (False)
    return (True)
def isRealNumber(str):
    length = len(str)
    hasDecimal = False
    if (length == 0):
        return (False)
    for i in range(0, length):
        if not str[i] in numerals and str[i] != '.' or (str[i] == '-' and i > 0):return (False)
        if (str[i] == '.'):hasDecimal = True
    return (hasDecimal)
def osubString(str,left,right):
    return (str[left:right])
def parse(str):
    left,right = 0,0
    lenh =len(str)
    while (right < lenh and left <= right): 
        if (isDelimiter(str[right]) == False):right=right+1
        if (isDelimiter(str[right]) == True and left == right):
            if not (isOperator(str[right]) == True):pass
            right=right+1
            left = right
        elif (isDelimiter(str[right]) == True and left != right or (right == lenh and left != right)):
            subStr = osubString(str, left, right)
            if  (isKeyword(subStr) == True):pass
            elif  (isInteger(subStr) == True):pass
            elif  (isRealNumber(subStr) == True):pass
            elif  (validIdentifier(subStr) == True  and isDelimiter(str[right - 1]) == False):pass
            elif  (validIdentifier(subStr) == False and isDelimiter(str[right - 1]) == False):print(subStr,"IS NOT A VALID IDENTIFIER" )
            left = right
    return 0

def getTokens(text):
    tokenKeyWords = []
    tokensplSymbols = []
    tokenOperators= []
    tokenDelimiters = []
    tokenIdentifiers = []
    tokenConstants = []
    tokenLibrarys=[]
    tokens = []
    isString = False
    isWord = False
    isCmt = 0
    token = ''
    program =  text.split('\n')
    for line in program:
        tokens = line.split(' ')
        for token in tokens:
            if '#' in token:
                match = re.search(r'#\w+', token)
                tokenKeyWords.append(token)
            if '.h' in token:
                tokenLibrarys.append(token)
    for i in text:
        if i == '/':
            isCmt = isCmt+1
        elif isCmt == 2:
            if i == '\n':
                token = ''
                isCmt = 0
        elif i == '"' or i == "'":
            if isString:
                tokens.append(token)
                token = ''
            isString = not isString 
        elif isString:
            token = token+i
        elif i in symbols:
            tokens.append(i)
        elif i.isalnum() and not isWord:
            isWord = True
            token = i
        elif (i in delimiters) or (i in operators):
            if token:
                tokens.append(token)
                token = ''
            if not (i==' ' or i=='\n' or i=='	'):
                tokens.append(i)
        elif isWord:
            token = token+i

    for token in tokens:
        if token in symbols:
            tokensplSymbols.append(token)
            print(token,"is a Special symbol")
        elif token in operators:
            tokenOperators.append(token)
            print(token,"is a Operator")
        elif token in keywords:
            tokenKeyWords.append(token)
            print(token,"is a keyword")
        elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",token) :
            if not 'include' in token:
                tokenIdentifiers.append(token)
                print(token,"is a identifiers")
        elif token in delimiters:
            tokenDelimiters.append(token)
            print(token,"is a Delimiter")
        else:
            if not '.h'  in token:
                tokenConstants.append(token)
    tokenIdentifiers=list(set(tokenIdentifiers))
    tokenKeyWords=list(set(tokenKeyWords))
    print("No of tokens = ", len(tokens))   
    print("\nNo. of keywords = ",len(tokenKeyWords))
    print(tokenKeyWords)
    print("\nNo. of libararys = ",len(tokenLibrarys))
    print(tokenLibrarys)
    print("\nNo. of special symbols = ",len(tokensplSymbols))
    print(tokensplSymbols)
    print("\nNo. of operators = ",len(tokenOperators))
    print(tokenOperators)
    print("\nNo. of identifiers = ",len(tokenIdentifiers))
    print(tokenIdentifiers)
    print("\nNo. of constants = ",len(tokenConstants))
    print(tokenConstants)
    print("\nNo. of delimiters = ",len(tokenDelimiters))
    print(tokenDelimiters)
    return 0



