

# Inventory list
inventory = []

# Function: welcome player
def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return name

# Function: describe area
def describe_area():
    print("\nYou find yourself in a dark forest...")
    print("You see two paths ahead:")
    print("1. Take the left path into the dark woods.")
    print("2. Take the right path toward the mountain pass.")
    print("3. Stay where you are.")
    print("Type 'i' to view your inventory.")

# Function: add to inventory
def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")

# Start game
player_name = welcome_player()
describe_area()

# Game loop
while True:
    choice = input("\nWhat will you do (1, 2, 3, or i): ").lower()

    if choice == "1":
        print(f"{player_name}, you step into the dark woods...")
        add_to_inventory("lantern")

    elif choice == "2":
        print(f"{player_name}, you head toward the mountain pass...")
        add_to_inventory("map")

    elif choice == "3":
        print(f"{player_name}, you decide to stay where you are.")

    elif choice == "i":
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in inventory:
                print(f"- {item}")

    else:
        print("Invalid choice. Try again.")