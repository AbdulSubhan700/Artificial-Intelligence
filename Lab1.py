# Input/output
text = "ABdul Subhan"
print(text)

# Multiple statements on a single line
print("First statement"); print("Second statement")

# Indentation with Tab space
num = 10
if num > 0:
    print("This statement has tab indentation")

# Indentation with single space
num = 10
if num > 0:
 print("This statement has single space indentation")

# Indentation with tab + single space
num = 10
if num > 0:
    print("This statement has tab + single space indentation")

# Assigning integer values
num1 = 2024
print(type(num1))  # <class 'int'>

num2 = -3600
print(type(num2))  # <class 'int'>

num3 = 7
print(type(num3))  # <class 'int'>

# Assigning float values
flt1 = 3.14
print(type(flt1))  # <class 'float'>

flt2 = -9.81
print(type(flt2))  # <class 'float'>

flt3 = .987
print(type(flt3))  # <class 'float'>

flt4 = 1.62e-19
print(type(flt4))  # <class 'float'>

flt5 = 8E307
print(type(flt5))  # <class 'float'>

# Creating a complex number
cmp1 = complex(3, 4)
print(type(cmp1))  # <class 'complex'>
print(cmp1)  # Output: (3+4j)

# Performing addition with complex numbers
cmp2 = 3 + 4j
print(cmp2)  # Output: (3+4j)
cmp3 = 1 + cmp2
print(type(cmp3))  # <class 'complex'>
print(cmp3)  # Output: (4+4j)

# Creating boolean values
bool1 = True
print(type(bool1))  # <class 'bool'>
print(bool1)  # Output: True
bool2 = False
print(type(bool2))  # <class 'bool'>
print(bool2)  # Output: False

# Performing actions on strings
string1 = "Learning Python"
print(string1[0])
print(string1[-15])
print(string1[9])

# List indices
colors_list = [10, 20, 30, 40, 50, 60]
fruit_list = ['apple', 'banana', 'cherry', 'date']
mixed_list = ['orange', 200, 345.67]
print(colors_list[2])
print(fruit_list[1:-2])
print(mixed_list[:3])