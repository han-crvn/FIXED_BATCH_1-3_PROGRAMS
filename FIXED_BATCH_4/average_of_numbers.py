# Create an empty lists
numbers_list = []

# Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = float(input("Enter the number: "))

        # Add the number to the list
        numbers_list.append(number)

    except ValueError:
        print("Invalid")
        break

# Calculate the average of the numbers in the list
average_num = sum(numbers_list) / len(numbers_list)

# Print the result
print(f"Result: {average_num}")