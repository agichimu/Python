"""
Created on Saturday 27 April 2024
@author: Alexander Gichimu
"""
from intengers import intengers

"""
# Ask users for their name

name = input("Whats your name? \n ").strip().upper().split()

# Name in this case is a variable

# Say Hello to users

# print("Holla, " + name)

print(f"Hello {name}")
"""


def main():
    name = input("Whats your name? \n ").strip().upper()
    hello(name)


def hello(to="World"):
    print("Hello,", to)


main()
intengers()
