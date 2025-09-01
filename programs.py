"""num = int(input("enter the number"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
#Find the greatest of three numbers.

arr = list(map(int, (input("Enter numbers: ").split())))
max = arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max
#A shop gives a discount of 10% if purchase is above ₹1000. Ask the user for the bill amount and calculate the final amount.
bill = int(input("how much is your bill"))
if bill>1000:
    bill -= bill*(10/100)
    print(bill)
else:
    print("no discount"))"""

bill = int(input("how much is your bill"))
final_amount = bill - bill * 0.1 if bill > 1000 else bill
print(final_amount)





