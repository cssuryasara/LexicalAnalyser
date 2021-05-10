## Lexical Analyzer for C written in Python

```python
from getTokens import parse,getTokens
from RemComments import commentRemover

fileName = input("Enter filename : ")
cFile = open(fileName, 'r')
text = cFile.read()
uncmtFile = commentRemover(text)
parse(uncmtFile)
getTokens(uncmtFile)
cFile.close()   
```
Give the C file location as input


### INPUT
```C
//Addition of two number
/**
  * This Program Add two numbers.
  */
#include <stdio.h>
#include <string.h>
int main()
{
  /*
   * This program add two integer numbers.
   */
  int a = 5, b = 10, c;
  c = a+b*1c;
  printf("Sum = %d\n", c);
  return 0;
}
```

### OUTPUT

1c IS NOT A VALID IDENTIFIER




} is a Delimiter

} is a Delimiter

\# is a Special symbol  

< is a Operator

\> is a Operator

\# is a Special symbol 

\< is a Operator

\> is a Operator

int is a keyword

main is a keyword

\( is a Delimiter

\) is a Delimiter

\{ is a Delimiter

int is a keyword

a is a identifiers

= is a Operator

, is a Delimiter

b is a identifiers

= is a Operator

, is a Delimiter

c is a identifiers

; is a Delimiter

c is a identifiers

= is a Operator

a is a identifiers

\+ is a Operator

\* is a Special symbol

1c is a identifiers

; is a Delimiter

printf is a keyword

( is a Delimiter

, is a Delimiter

c is a identifiers

) is a Delimiter

; is a Delimiter

return is a keyword

; is a Delimiter

} is a Delimiter

No of tokens =  46

No. of keywords =  5
['int', 'main', 'return', 'printf', '#include']

No. of libararys =  2
['<stdio.h>', '<string.h>']

No. of special symbols =  3
['#', '#', '*']

No. of operators =  8
['<', '>', '<', '>', '=', '=', '=', '+']

No. of identifiers =  4
['c', 'b', 'b1c', 'a']

No. of constants =  4
['5', '10', 'Sum = %d\\n', '0']

No. of delimiters =  15
['}', '}', '(', ')', '{', ',', ',', ';', ';', '(', ',', ')', ';', ';', '}']
