list1 = []
list2 = []
differences = []
i, j = 0, 0
total_difference = 0

# Open and read the file line by line
with open('input.txt', 'r') as file:
    for line in file:
        # Strip whitespace and split the line into numbers
        numbers = line.strip().split()
        # Convert each number to an integer
        num1, num2 = map(int, numbers)

        list1.append(num1)
        list2.append(num2)

        list1.sort()
        list2.sort()

for i in range(min(len(list1), len(list2))):
    # Calculate the absolute difference between elements at the same index
    diff = abs(list1[i] - list2[i])
    total_difference += diff

# Print the list of differences
print(total_difference)