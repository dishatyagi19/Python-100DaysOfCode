#Quick summary of what we learned today:

### 1️⃣ Subscripting:

```
print("Hello"[0])   #get element at index 0 = H
print("Hello"[-1])   #get element at index -1 = o
```
↳ H  
   o

### 2️⃣ Primitive data types:

- String
```
print("48" + "12")   #although the numbers are of int type, but after being wrapped in double quotes ("") they become str   #string concatenation
```
↳ 4812

- Integer = whole number
```
print(123+456)
print(56_732_981)   #large integer - using comma would print space in the result, so we will use underscore instead for writing big numbers
```
↳ 579  
   56732981

- Float
```
print(3.14)
```
↳ 3.14

-Boolean
```
print(True)
print(False)
```
↳ True   
   False

### 3️⃣ Type checking:

```
print(type("wolves"))
print(type(True))
print(type(9891))
print(type(98.9))
```
↳ <class 'str'>  
   <class 'bool'>  
   <class 'int'>  
   <class 'float'>  

### 4️⃣ Type error:

```
print(len(1998))
print(type(345,234))
print(int("asd") + int("jkl"))
print(int("wer") + int("729"))
print(int("puppy"))

```

### 5️⃣ Type conversion:

```
print(int("478") + int("111"))   #converting strings to integers before adding
print("My age: " + str(12))    #int and str cannot be concatenated, but type converting int to str can help in concatenation
```
↳ 589  
   My age: 12

### 6️⃣ Mathematical Operations:

```
print(1+2, 2-1, 3*4, 15/3, 15//3, 2**3)   #`//` is used for removing numerals after decimal point

```
↳ 3 1 12 5.0 5 8


```
print(7/3)
print(7//3)
print(76/6)
print(76//6)
```
↳ 2.33333333335  
   2  
   12.66666666666  
   12

```
print(round(76/6))   #round function can be used to round-off the resulting value
print(type(76/6))   #result of division always is of type float
print(int(76/6))    #using type conversion with '/' can round-off resulting value towards the floor or ceiling
print(int(7/3))    #eg. 2.3 ~ 2 (floor value), 5.7 ~ 6 (ceiling value)
```
↳ 13  
   <class 'float'>  
   13  
   2

```
print(3 * 3 + 3 / 3 - 3)   #Bodmas will be applied from left to right
print(3 * (3 + 3) / 3 - 3)
```
↳ 7  
   3

### 7️⃣ Number manipulation:

```
bmi = 84 / 1.65 ** 2
print(bmi)
print(round(bmi, 2))   #rounding-off results till 2 decimal places
```
↳ 30.85399449035813  
   30.85

```
a = 2
a+=1   
print( a)
```
↳ 3

```
a = 2
a-=1  
print( a)
```
↳ 1

```
a = 2
a*=3   
print( a)
```
↳ 6

```
a = 5
a/=2   
print( a)
```
↳ 2.5

### 8️⃣ f Strings:

```
age = 12
print(f"My age is: {age}")
```
↳ My age is: 12