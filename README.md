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
/**
  * commented line.
  */
  int main(){
  float a;
  a = 1.1;
  int i, inc, j;
  i = 0;
  j=2;
  inc = 2;
  while (i < j){
    i = i + inc;
    a = a*i;
  }
  if (a > 10.0){
    printf(a + i);
  }
}
```

### OUTPUT

1c IS NOT A VALID IDENTIFIER




} is a Delimiter

} is a Delimiter 

int is a keyword 

main is a keyword 

( is a Delimiter  

) is a Delimiter

{ is a Delimiter  

float is a keyword

a is a identifiers

; is a Delimiter  

a is a identifiers

= is a Operator 

; is a Delimiter 

int is a keyword

i is a identifiers

, is a Delimiter  

inc is a identifiers

, is a Delimiter

j is a identifiers

; is a Delimiter

i is a identifiers

= is a Operator

; is a Delimiter

j is a identifiers

= is a Operator

; is a Delimiter

inc is a identifiers

= is a Operator

; is a Delimiter

while is a keyword

( is a Delimiter

i is a identifiers

< is a Operator

j is a identifiers

) is a Delimiter

{ is a Delimiter

i is a identifiers

= is a Operator

i is a identifiers

\+ is a Operator

inc is a identifiers

; is a Delimiter

a is a identifiers

= is a Operator

\* is a Special symbol

ai is a identifiers

; is a Delimiter

} is a Delimiter

if is a keyword

( is a Delimiter

a is a identifiers

> is a Operator

) is a Delimiter

{ is a Delimiter

printf is a keyword

( is a Delimiter

a is a identifiers

\+ is a Operator

i is a identifiers

) is a Delimiter

; is a Delimiter

} is a Delimiter

} is a Delimiter

No of tokens =  68

No. of keywords =  5

No. of keywords =  6
['main', 'int', 'if', 'printf', 'while', 'float']

No. of special symbols =  1
['*']

No. of operators =  10
['=', '=', '=', '=', '<', '=', '+', '=', '>', '+']

No. of identifiers =  5
['i', 'a', 'j', 'inc', 'ai']

No. of constants =  5
['1.1', '0', '2', '2', '10.0']

No. of delimiters =  27
['}', '}', '(', ')', '{', ';', ';', ',', ',', ';', ';', ';', ';', '(', ')', '{', ';', ';', '}', '(', ')', '{', '(', ')', ';', '}', '}'] 
