def is_even(x):
    """
    Checks if x divided by 2 its remainder is 0.
    """
    if x % 2 == 0:
        return True
    else:
        return False


def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("odd")


main()
