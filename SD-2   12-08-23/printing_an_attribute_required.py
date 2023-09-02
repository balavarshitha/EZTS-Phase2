'''write a code to print the required attribute given as input such as
name, age, email id to each person'''

people_data = {}

num_people = int(input("Enter the number of people: "))

for i in range(num_people):
    print(f"\nEnter details for person {i+1}:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email ID: ")
    gender = input("Gender: ")

    people_data[name] = {
        "age": age,
        "email": email,
        "gender": gender
    }
search_name = input("\nEnter the name of the person to search for: ")
if search_name in people_data:
    attribute = input("Enter the attribute (age/email/gender) to retrieve: ")
    if attribute in people_data[search_name]:
        print(f"{search_name}'s {attribute} is {people_data[search_name][attribute]}")
    else:
        print("Invalid attribute!")
else:
    print("Person not found!")
