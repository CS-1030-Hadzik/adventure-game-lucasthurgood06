# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False


# Function: welcome player (now returns Player object)
def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return Player(name)


# Function: describe area
def describe_area():
    print("\nYou find yourself in a dark forest...")
    print("You see two paths ahead:")
    print("1. Take the left path into the dark woods.")
    print("2. Take the right path toward the mountain pass.")
    print("3. Enter the cave.")
    print("Type 'i' to view your inventory.")


# Function: add to inventory (UPDATED)
def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")


# Start game
player = welcome_player()
describe_area()

# Game loop
while True:
    choice = input("\nWhat will you do (1, 2, 3, or i): ").lower()

    if choice == "1":
        print(f"{player.name}, you step into the dark woods...")
        if not player.has_lantern:
            add_to_inventory(player, "lantern")
            player.has_lantern = True
        else:
            print("You already have a lantern.")

    elif choice == "2":
        print(f"{player.name}, you head toward the mountain pass...")
        if not player.has_map:
            add_to_inventory(player, "map")
            player.has_map = True
        else:
            print("You already have a map.")

    elif choice == "3":
        # 🔥 Stretch goal condition
        if not player.has_lantern:
            print("It's too dark to enter the cave without a lantern.")
        else:
            print(f"{player.name}, you enter the cave safely with your lantern!")

    elif choice == "i":
        if len(player.inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in player.inventory:
                print(f"- {item}")

    else:
        print("Invalid choice. Try again.")