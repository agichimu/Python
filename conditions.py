"""
Python Conditionals

> --> greater than
>=--> greater than or equal to
< --> less than
<= --> less than or equal to
== --> equality
!= --> not equal

"""

x = int(input("What is the value of x? "))
y = int(input("What is the value of y? "))

if x < y or x > y:
    print("Sorry x and y are not equal")
else:
    print("x and y are equal")
