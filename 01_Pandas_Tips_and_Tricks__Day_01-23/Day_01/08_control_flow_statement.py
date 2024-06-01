# Conditional statements
# >
# <
# <=
# >=
# ==
# !=

x = 10

if x != 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# Conditional statements allow for branching logic based on conditions.

# Comparison operators used in conditions:
# > (greater than), < (less than), == (equal to), != (not equal to)

# Assign a value to 'x'
x = 0

# Check if 'x' is not equal to zero
if x > 0:  # If true, 'x' is positive
    print("x is positive")
elif x < 0:  # If previous condition is false, check if 'x' is less than zero
    print("x is negative")
else:  # If all above conditions are false, execute this block
    print("x is zero")


# for loop
    
menu = ["Dahi Bhallay", "Biryani", "Daal", "Samosay", "Shami", "Palak Paneer"]

# print(menu[0])
# print(menu[1])
# print(menu[2])
# print(menu[3])
# print(menu[4])
# print(menu[5])

for item in menu:
    print(item)


# While loop

i = 1
while i < 6:
    print(i)
    i = i + 1

for letters in "Python" :
    if letters == 'h':  
        pass
    print(letters)

for letters in "Python" :
    if letters == 'h':  
        continue
    print(letters)

for letters in "Python" :
    if letters == 'h':  
        break
    print(letters)

