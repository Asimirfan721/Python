a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("Select Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter  Your choice 1/2/3/4): ")

if choice == '1':
    result=a+b
    print("Result:", result)
elif choice == '2':
    result=a-b
    print("Result:", result)
elif choice == '3':
    result=a*b
    print("Result:", result)
elif choice == 4:
    if b!=0:
        result=a/b
        print("Result:", result)
    else:
        print("Error: can not divide by zero")
else:
    print("Invalid choice")