# Q10. Check if a number is Palindrome
num = int(input("Enter a number: "))
original_num = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original_num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")