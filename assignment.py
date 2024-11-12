def calc(a,b ,option):
    if (option =="+"):
          return a + b
    elif(option =="-"):
           return a-b
    elif (option =="*"):
          return a*b
    elif (option =="/"):
          return a/b
    elif (option =="^"):
          return a^b
    else:
        return"bad option"

op=input ("Please enter the operation you want\nsum(+)\nsubtraction(-)\nmultiplication(*)\nDivision(/)\nEmpowerment(^)\nYour option:")
a =int(input("Please enter the number a:"))
b =int(input("Please enter the number b:"))
result =calc(a,b,op)
print (result)
