print("===== GROCERY SHOPPING BILL =====")

name = input("Enter customer name: ")

n = int(input("Enter number of items: "))

total = 0

for i in range(n):
    print("\nItem", i + 1)

    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

    print("Item:", item)
    print("Amount:", amount)

print("\n===== FINAL BILL =====")
print("Customer Name:", name)
print("Total Amount: Rs.", total)

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_amount)

print("Thank you for shopping!")
