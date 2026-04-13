# Inventory list
inventory = []

# Function: welcome player
def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")
    return name

# Function: describe the area
def describe_area():
    print("""
You find yourself at the edge of a dark forest.
The trees are tall and block out most of the light.
You see two paths ahead:
1. A path leading deeper into the forest.
2. A path leading toward a river.
(Type 'i' at any time to check your inventory)
""")

# Function: add item to inventory
def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")

# Start game
player_name = welcome_player()
describe_area()

# Game loop
while True:
    choice = input("What do you do? (1/2/i/quit): ").lower()

    if choice == "1":
        print("You walk deeper into the forest...")
        add_to_inventory("lantern")

    elif choice == "2":
        print("You head toward the river...")
        add_to_inventory("map")

    elif choice == "i":
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in inventory:
                print(f"- {item}")

    elif choice == "quit":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice. Try again.")