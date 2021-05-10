from getTokens import parse,getTokens
from RemComments import commentRemover

fileName = input("Enter filename : ")
cFile = open(fileName, 'r')
text = cFile.read()
uncmtFile = commentRemover(text)
parse(uncmtFile)
getTokens(uncmtFile)
f.close()   
