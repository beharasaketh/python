num = int(input("Enter any number: "))
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")