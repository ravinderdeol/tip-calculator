bill = int(input("Enter Total Bill: "))
tip_percentage = 0.20
tax_percentage = 0.067

tip = bill * tip_percentage
print(f"Tip: {tip}")

tax = bill * tax_percentage
print(f"Tax: {tax}")

total = bill + tip + tax
print(f"Total: {total}")
