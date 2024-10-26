# This program generates a Fibonacci sequence up to a user-defined number of terms
# using a list to store and display the sequence.

# Prompt the user for the number of terms in the Fibonacci sequence
number = int(input("Enter the number of Fibonacci terms to generate: "))

# Initialize a list with the first two terms of the Fibonacci sequence
fibonacci_list = [0, 1]
next_term = 0  # Variable to hold the next term in the sequence

# Handle edge cases for 0 or 1 term(s)
if number == 0:
    print("0")  # If the user enters 0, output only the first term
elif number == 1:
    print("0, 1")  # If the user enters 1, output the first two terms
else:
    # Generate the sequence for more than 1 term
    for n in range(2, number):
        # Calculate the next term as the sum of the last two terms in the list
        next_term = fibonacci_list[n - 1] + fibonacci_list[n - 2]
        fibonacci_list.append(next_term)  # Append the new term to the list

    # Print the entire Fibonacci sequence list
    print(fibonacci_list)
