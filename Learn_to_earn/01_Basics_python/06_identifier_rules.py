""" 123abc = 23 123abc = 23
      ^
SyntaxError: invalid decimal literal """

abc = 2 # identifier name should always be start with A-Z or a-z
print(abc)

_1 = 3 # identifier name can also start with _ followed by a number or character
print(_1)

__A ="Name"
print(__A)

_1to9 = "identifier name could also include digits from 0 to 9" # "identifier name could also include digits from 0 to 9"
print(_1to9)

# identifier names follows case sensitive

Age = 50
print("print")

age = 60
print(age)
print(Age)
#print(me)

