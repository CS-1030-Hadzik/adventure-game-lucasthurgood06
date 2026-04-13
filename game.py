class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False


def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return Player(name)


def describe_area():
    print("\nYou find yourself in a dark forest...")
    print("You see several paths ahead:")
    print("1. Take the left path into the dark woods.")
    print("2. Take the right path toward the mountain pass.")
    print("3. Explore a nearby cave.")
    print("4. Search for a hidden valley.")
    print("Type 'i' to view your inventory.")
    print("Type 'q' to quit.")


def add_to_inventory(player, item):
    if item not in player.inventory:
        player.inventory.append(item)
        print(f"You picked up {item}!")
    else:
        print(f"You already have {item}.")


def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods...")
    if not player.has_lantern:
        add_to_inventory(player, "lantern")
        player.has_lantern = True
    else:
        print("You already found the lantern here.")


def explore_mountain_pass(player):
    print(f"{player.name}, you head toward the mountain pass...")
    if not player.has_map:
        add_to_inventory(player, "map")
        player.has_map = True
    else:
        print("You already found the map here.")


def explore_cave(player):
    if player.has_lantern:
        print(f"{player.name}, you explore the cave with your lantern.")
        add_to_inventory(player, "treasure")
    else:
        print("It's too dark to explore the cave without a lantern.")


def explore_hidden_valley(player):
    if player.has_map:
        print(f"{player.name}, you use your map to find the hidden valley.")
        add_to_inventory(player, "rare herbs")
    else:
        print("You can't find the hidden valley without a map.")


def show_inventory(player):
    if len(player.inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Inventory:")
        for item in player.inventory:
            print(f"- {item}")


player = welcome_player()
describe_area()

while True:
    choice = input("\nWhat will you do (1, 2, 3, 4, i, or q): ").lower()

    if choice == "1":
        explore_dark_woods(player)

    elif choice == "2":
        explore_mountain_pass(player)

    elif choice == "3":
        explore_cave(player)

    elif choice == "4":
        explore_hidden_valley(player)

    elif choice == "i":
        show_inventory(player)

    elif choice == "q":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice. Try again.")