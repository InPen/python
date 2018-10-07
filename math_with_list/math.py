# Save a list with the numbers 2, 4, 6, and 8 into a variable called numbers.
numbers = [2, 4, 6, 8]
# Print the max of numbers.
print(max(numbers))
# Pop the last element in numbers off; re-insert it at index 2.
numbers.pop()
numbers.insert(2, 8)

# current array is [2, 4, 8, 6]

# Pop the second number in numbers off.
numbers.pop(2)
# Append 3 to numbers.
numbers.append(3)
# Print out the average number (divide the sum of numbers by the length).
average_number = sum(numbers)

# *why didn't average_number/len() did not work?
average_number/4

# Print numbers.
print(average_number)
