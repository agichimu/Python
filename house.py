"""
Match Statement is similar to switch statement in java
"""
middleName = input("Enter your Middle name: ") .capitalize()
match middleName:
    case "Wanjiku":
        print("Wanjikus Family")
    case "Wairimu":
        print("Wairimus Family")
    case "Wangechi":
        print("Wangechi Family")
    case "Muthoni":
        print("Muthoni Family")
    case _:
        print("Who are you?")
