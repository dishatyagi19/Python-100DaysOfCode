# Quick recap:-

### 1️⃣ Random module:

```
import random   #to use random function we have to import the package first

print(random.randint(1, 10))   #here we are generating random integer numbers

print(random.random())   #this function generates random float numbers in range 0.0 <= num < 1.0

print(random.random() * 10)   #we increased the range of generated numbers - 0*10 <= num <1.0*10

print(random.uniform(1, 10))   #prints random float numbers as well but this time you can explicitly give the range and can have the second number be included in the range
``` 

*Module : Using modules can help us import required functions, variables, etc. from different packages or files. Eg:-*

```
file1 : temp_file.py :-
a = 10

file2 : task.py :-
import random
import temp_file

print(random.randint(1,10))
print(a)
``` 
↳ 7  
   10

```
import random

num = random.randint(0,1)

if num == 0:
    print("Heads")
else:
    print("Tails")
```

### 2️⃣ Offset and appending items to list:

*List : a type of [data structure](https://docs.python.org/3/tutorial/datastructures.html), used for storing/organizing datas.*

```
fruits = ["apple", "kiwi", "orange", "banana", "kiwi"]

print(fruits[-2])

fruits[0] = "cherry"
print(fruits)

fruits.append("apple")
print(fruits)

fruits.extend(["watermelon", "muskmelon", "kiwi", "strawberry"])
print(fruits)

fruits.insert(3, "guava")
print(fruits)

fruits.remove("guava")
print(fruits)

fruits.pop(5)
print(fruits)

print(fruits.count("kiwi"))

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits.clear()
print(fruits)
```
↳ banana  
['cherry', 'kiwi', 'orange', 'banana', 'kiwi']  
['cherry', 'kiwi', 'orange', 'banana', 'kiwi', 'apple']  
['cherry', 'kiwi', 'orange', 'banana', 'kiwi', 'apple', 'watermelon', 'muskmelon', 'kiwi', 'strawberry']  
['cherry', 'kiwi', 'orange', 'guava', 'banana', 'kiwi', 'apple', 'watermelon', 'muskmelon', 'kiwi', 'strawberry']  
['cherry', 'kiwi', 'orange', 'banana', 'kiwi', 'apple', 'watermelon', 'muskmelon', 'kiwi', 'strawberry']  
['cherry', 'kiwi', 'orange', 'banana', 'kiwi', 'watermelon', 'muskmelon', 'kiwi', 'strawberry']  
3  
['strawberry', 'kiwi', 'muskmelon', 'watermelon', 'kiwi', 'banana', 'orange', 'kiwi', 'cherry']  
['banana', 'cherry', 'kiwi', 'kiwi', 'kiwi', 'muskmelon', 'orange', 'strawberry', 'watermelon']  
[]

### 3️⃣ Random selection from list:

Method 1: using choice() function

```
import random

friends = ["Pip", "Ravi", "Andy", "Sal", "Emanuel"]

print(random.choice(friends))
```

Method 2:
```
import random

friends = ["Pip", "Ravi", "Andy", "Sal", "Emanuel"]

index = random.randint(0, 4)

print(friends[index])
```

### 4️⃣ IndexErrors:

```
import random

friends = ["Pip", "Ravi", "Andy", "Sal", "Emanuel"]

num = random.randint(0, len(friends))   #suppose num = 5 (because len(friends) = 5)

print(friends[num])
```
↳ ERROR!  
Traceback (most recent call last):  
  File "<main.py>", line 7, in <module>  
IndexError: list index out of range

*To resolve this, remember to -1 from len of list:-*

```
import random

friends = ["Pip", "Ravi", "Andy", "Sal", "Emanuel"]

num = random.randint(0, len(friends)-1)

print(friends[num])
```

### 5️⃣ Nested lists:

```
fruits = ["Strawberries", "Grapes", "Peaches", "Cherries", "Nectarines", "Pears", "Apples", "Blackberries", "Blueberries"]
vegetables = ["Spinach", "Kale, Collard, and Mustard Greens", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][0])
print(dirty_dozen[1][1])
```
↳ [['Strawberries', 'Grapes', 'Peaches', 'Cherries', 'Nectarines', 'Pears', 'Apples', 'Blackberries', 'Blueberries'], ['Spinach', 'Kale, Collard, and Mustard Greens', 'Potatoes']]  
['Strawberries', 'Grapes', 'Peaches', 'Cherries', 'Nectarines', 'Pears', 'Apples', 'Blackberries', 'Blueberries']  
['Spinach', 'Kale, Collard, and Mustard Greens', 'Potatoes']  
Strawberries  
Kale, Collard, and Mustard Greens


