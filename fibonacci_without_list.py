# Program to generate the Fibonacci sequence up to a user-defined number of terms.
# It prompts the user for the number of terms, checks input validity,
# and calculates each term without storing them in a list.

# Initialize the first two terms of the Fibonacci sequence
first_term = 0
second_term = 0

# Prompt the user for the number of terms in the Fibonacci sequence
number_of_terms = int(input("Please enter a positive number of terms: "))

# Validate the input to ensure it is non-negative
if number_of_terms < 0:
    print("Please enter a positive number.")
else:
    # Generate each term up to the specified number
    for term_index in range(number_of_terms):
        if term_index == 0:
            print(first_term)  # Print the first term
        elif term_index == 1:
            second_term = 1
            print(second_term)  # Print the second term
        else:
            # Calculate the next term as the sum of the previous two terms
            next_term = first_term + second_term
            print(next_term)  # Print the current term
            # Update the terms for the next iteration
            first_term = second_term
            second_term = next_term
