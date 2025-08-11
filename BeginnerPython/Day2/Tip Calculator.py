print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? Rs"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

result = (bill * ( tip / 100 ) + bill) / people

print(f"Each person should pay: Rs{round(result, 2)}")