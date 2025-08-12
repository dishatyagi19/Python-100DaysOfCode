# Quick summary of what we learned today:-

### 1️⃣ if-else, elif and conditional operators:

```
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the rollercoaster")
else:
	print("Sorry, you have to grow taller before you can ride.")
```
↳ - Welcome to the rollercoaster!  
     What is your height in cm? 150  
     You can ride the rollercoaster  

- Welcome to the rollercoaster!  
  What is your height in cm? 119  
  Sorry, you have to grow taller before you can ride.

```
print("Device selection on the basis of room temperature")

temp = int(input("What is the current room temperature? "))

if temp >= 35:
	print("Turn on AC")
elif temp <= 15:
	print("Turn on heater")
else:
	print("No device")
```
↳  - Device selection on the basis of room temperature  
        What is the current room temperature? 16  
     No device  

- Device selection on the basis of room temperature  
  What is the current room temperature? 35  
  Turn on AC

- Device selection on the basis of room temperature  
  What is the current room temperature? 1  
  Turn on heater

### 2️⃣ Modulo operator:

```
print(10%3)
```
↳  1

```
print("Determining even and odd")

num = int(input("Enter number: "))

if num == 0:
	print("can't divide zero")
elif num % 2 == 0:
	print("even")
else:
	print("odd")
```
↳ - Determining even and odd  
    Enter number: 2  
    even

- Determining even and odd  
  Enter number: 1  
  odd

- Determining even and odd  
  Enter number: 0  
  can't divide zero

### 3️⃣ if-else and conditional operators:

```
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?\n"))

if height >= 120:
	print("You can ride the rollercoaster.")
	age = int(input("What is your age?\n"))
	if age <= 18:
		print("Please pay Rs50.")
	else:
		print("Please pay Rs100.")
else:
	print("Sorry, you have to grow taller before you can ride.")
```
↳ - Welcome to the rollercoaster!  
    What is your height in cm?  
    120  
    You can ride the rollercoaster.  
    What is your age?  
    55  
    Please pay Rs100.  

- Welcome to the rollercoaster!  
  What is your height in cm?  
  176  
  You can ride the rollercoaster.  
  What is your age?  
  16  
  Please pay Rs50.

### 4️⃣ BMI Calculator:

```
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")
```
↳ normal weight

### 5️⃣ Multiple if statements:

```
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
	print("You can ride the rollercoaster.")
	age = int(input("What is your age?\n"))
	if age <= 18:
	    bill = 50
	    print("Underage. Pay Rs50.")
	else:
	    bill = 70
	    print("Adult. Pay Rs70.")
	
	photo = input("Do you want photo? Press y for yes, n for no: ")	
	if photo == "y":
	    bill += 30
	
	print(f"Your total bill is: Rs{bill}")
    
else:
	print("Sorry, you have to grow taller before you can ride.")
```
↳ Welcome to the rollercoaster!  
  What is your height in cm?  
  610  
  You can ride the rollercoaster.  
  What is your age?  
  78  
  Adult. Pay Rs70.  
  Do you want photo? Press y for yes, n for no: y  
  Your total bill is: Rs100

### 6️⃣ Pizza order practice:

```
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
	bill += 150
elif size == "M":
	bill += 200
elif size == "L":
	bill += 250
else:
	print("Invalid selection")	

if pepperoni == "Y":
    if size == "S":
        bill += 20
    else:
        bill += 30

if extra_cheese == "Y":
	bill += 10


print(f"Your final bill: Rs{bill}")
```
↳ Welcome to Python Pizza Deliveries!  
  What size pizza do you want? S, M or L: L  
  Do you want pepperoni on your pizza? Y or N: Y  
  Do you want extra cheese? Y or N: N  
  Your final bill: Rs280

### 7️⃣ Logical operators:

```
a=10
print(a>9)
print(a<9)

print(True and True)
print(a>5 and a<15)

print(True and False)
print(False and True)
print(a>15 and a<11)

print(True or True)
print(a>5 or a<15)

print(True or False)
print(False or True)
print(a>9 or a<8)

print(not True)
print(not False)
print(not a<0)

if 1 < a < 99:
    print("yes!!!!!")
```
↳ True  
  False  
  True  
  True  
  False  
  False  
  False  
  True  
  True  
  True  
  True  
  True  
  False  
  True  
  True  
  yes!!!!!