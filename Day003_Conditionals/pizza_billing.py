print("🍕 Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

# Check size and apply base price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("❌ Invalid pizza size selected.")
    bill = None

# Add toppings only if size input was valid
if bill is not None:
    if pepperoni == "Y":
        bill += 2 if size == "S" else 3
    if extra_cheese == "Y":
        bill += 1

    print(f"💵 Your final bill is: **${bill}**")

