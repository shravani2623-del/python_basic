
numbers = [10, 25, 7, 45, 32]

largest = float('-inf')
second_largest = float('-inf')

# Check each number in the list
for num in numbers:

    # If current number is greater than largest
    if num > largest:

        # Previous largest becomes second largest
        second_largest = largest

        # Current number becomes largest
        largest = num

    # Check if current number is greater than second largest
    elif num > second_largest and num != largest:

        # Update second largest
        second_largest = num

# Display the results
print("Largest:", largest)
print("Second largest:", second_largest)