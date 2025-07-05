#Tip Calculator Program

# Print a welcome message to the user.
print("Welcome to KIzito's Tip calculator!") 
# Prompt the user to enter the total bill amount and convert it to a floating-point number.
total_bill = float(input("What is your Total Bill? R ")) 
# Prompt the user to enter the tip percentage (as an integer) they want to give.
tip_per = int(input("How much tip would you like to give? 10, 12, or 15? "))
# Prompt the user to enter the number of people splitting the bill and convert it to an integer.
Amount_of_people = int(input("How many people will be splitting the Bill? "))

# Calculate the tip amount by multiplying the total bill by the tip percentage (divided by 100).
tip_amount = total_bill * (tip_per / 100)
# Calculate the total bill including the tip by adding the tip amount to the original total bill. (Note: this overwrites the original total_bill value).
total_bill = total_bill + tip_amount
# Calculate the final amount each person should pay by dividing the total bill (including tip) by the number of people.
final_amount = total_bill / Amount_of_people
# Round the final amount to two decimal places for currency formatting.
final_amount = round(final_amount, 2)

# Print the final amount each person should pay, formatted as a currency string using an f-string.
print(f"Each Person Should Pay: R{final_amount}")

