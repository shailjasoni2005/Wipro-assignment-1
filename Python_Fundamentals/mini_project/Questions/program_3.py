
# Q3. Check if two numbers have the same last digit

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 10 == num2 % 10:
    print("True")
else:
    print("False")