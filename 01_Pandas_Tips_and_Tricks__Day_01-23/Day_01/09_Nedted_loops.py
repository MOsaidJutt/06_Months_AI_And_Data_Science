# Nested for loops

colors = ["red", "green", "blue"]
items = ["book", "pen", "copy"]

for color in colors:
    for item in items:
        print(color, item)

# Nested while loops
        
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(i, j)
        j += 1
    i += 1

# for loop inside while loop

i = 1
while i < 4:
    for j in range(3):
        print(i, j)
    i += 1


# for loop to iterate over a range of numbers
for i in range(1, 4):  # This will iterate over i values 1 to 3
    j = 0  # Initialize j to 0
    # while loop inside the for loop
    while j < 3:  # This will iterate as long as j is less than 3
        print(i, j)  # Print the current values of i and j
        j += 1  # Increment j by 1
