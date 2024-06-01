x = 15
y = 4   
z = 5.5
a = "Codanics"
b  = "Pakistan "
# Arithmatic operators
print(x+y)
# print (a)
print(a+b)  #addition
print(x-y)  #subtraction

print(x-z)   #subtraction
print(x*y)    #multiplication
print(x/y)  # division

# print(x-z*4/y+3) #DMAS #PEMDAS #BODMAS

x = 11

z = 5.2
# comparison operators
print(x > y)
print(x < z)
print(x == z)
print(x != z)

# how to combine two or more comparison operator in one line of code
print((x > y) and (x < z))  # True if x is greater than y AND x is less than z
print((x < z) or (x == z))  # True if x is less than z OR x is equal to z
print((x > y) and (x < z) or (x == z))  # True if x is greater than y AND x is less than z, OR x is equal to z
print((x > y) and ((x < z) or (x == z)))  # True if x is greater than y AND (x is less than z OR x is equal to z)
print(not(x == z))  # True if x is NOT equal to z, equivalent to print(x != z)
print((x > y) and (x < z) or (x == z) and not (x != z))

print((x > y), (x < z), (x == z), (x != z))
