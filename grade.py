grade = int(input("Score: "))

if 90 <= grade <= 100:
    print("Your Grade is: A")
elif 80 <= grade < 90:
    print("Your Grade is: B")
elif 70 <= grade < 80:
    print("Your Grade is: C")
elif 60 <= grade < 70:
    print("Your Grade is: D")
elif 50 <= grade < 60:
    print("Your Grade is: E")
else:
    print("Your Grade is: F")
