'''write a code to print the required attribute given as input such as
name, age, email id to each person'''
# Initialize lists to store attributes
names = []
ages = []
emails = []

# Define the number of people
num_people = int(input("Enter the number of people: "))

# Collect attributes for each person
for i in range(num_people):
    print(f"\nEnter details for person {i+1}:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email ID: ")

    names.append(name)
    ages.append(age)
    emails.append(email)

# Function to find and print the required attribute for a person
def print_attribute(name, attribute):
    index = names.index(name)
    if attribute == "age":
        print(f"{name}'s age is {ages[index]}")
    elif attribute == "email":
        print(f"{name}'s email is {emails[index]}")
    else:
        print("Invalid attribute!")

# Search for a person and print the desired attribute
search_name = input("\nEnter the name of the person to search for: ")
search_attribute = input("Enter the attribute (age/email) to retrieve: ")

if search_name in names:
    print_attribute(search_name, search_attribute)
else:
    print("Person not found!")

