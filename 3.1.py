# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Concatenate first name and last name
full_name = first_name + " " + last_name

# Slice the first three characters of the first name
sliced_name = first_name[:3]

# Create a greeting message using string formatting
greeting_message = f"Hello, {sliced_name}! Welcome. You are {age} years old"

# Display the results
print("\nFull name:", full_name)
print("Sliced name:", sliced_name)
print("Greeting Message:", greeting_message)
