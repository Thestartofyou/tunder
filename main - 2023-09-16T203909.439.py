import random

# Sample pet data (you can replace this with real data)
pets = [
    {"name": "Buddy", "type": "Dog", "age": 3},
    {"name": "Whiskers", "type": "Cat", "age": 2},
    {"name": "Rex", "type": "Dog", "age": 4},
]

# List to store matched pets
matches = []

def swipe_right():
    if not pets:
        print("No more pets to swipe!")
        return
    pet = pets.pop(0)
    print(f"You swiped right on {pet['name']} ({pet['type']}, {pet['age']} years old)!")
    matches.append(pet)

def swipe_left():
    if not pets:
        print("No more pets to swipe!")
        return
    pet = pets.pop(0)
    print(f"You swiped left on {pet['name']} ({pet['type']}, {pet['age']} years old)!")

def show_matches():
    if not matches:
        print("You haven't matched with any pets yet.")
    else:
        print("Your matches:")
        for pet in matches:
            print(f"{pet['name']} ({pet['type']}, {pet['age']} years old)")

while True:
    print("\nOptions:")
    print("1. Swipe right (like)")
    print("2. Swipe left (pass)")
    print("3. Show matches")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        swipe_right()
    elif choice == "2":
        swipe_left()
    elif choice == "3":
        show_matches()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
