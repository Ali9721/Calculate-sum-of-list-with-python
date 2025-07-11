# Define "numbers" as a variable & use "list" & "map" & "split"
numbers = list(map(int, input("Please enter numbers separated by spaces: ").split()))

# Define "total" as a variable & use "sum"
total = sum(numbers)

# Output the result.
print(f"The sum of the numbers is: {total}")