def calculate_total_difference(filename):
    list1 = []
    list2 = []
    total_difference = 0

    # Read the file and populate the lists
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            num1, num2 = map(int, numbers)
            list1.append(num1)
            list2.append(num2)

    # Sort the lists
    list1.sort()
    list2.sort()

    # Calculate the total sum of absolute differences
    for i in range(min(len(list1), len(list2))):
        diff = abs(list1[i] - list2[i])
        total_difference += diff

    return total_difference


def calculate_weighted_sum(filename):
    total_sum = 0
    list1 = []
    list2 = []

    with open(filename, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            num1, num2 = map(int, numbers)
            list1.append(num1)
            list2.append(num2)

    # Iterate through each unique number in list1
    for num in list1:
        count_in_list2 = list2.count(num)  # Count occurrences of num in list2
        weighted_sum = num * count_in_list2  # Multiply num by its count in list2
        total_sum += weighted_sum  # Add to the total sum

    return total_sum

# Call the function and print the result
filename = 'input.txt'
print(calculate_total_difference(filename))
print(calculate_weighted_sum(filename))