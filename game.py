print("Welcome to the Adventure Game!")  
print("Your journey begins here...")
class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []


def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("\nYou found the treasure and the rare herbs.")
        print("You win the game!")
        exit()


def check_lose(player):
    if player.health <= 0:
        print("\nYour health has dropped to 0.")
        print("You lost the game.")
        exit()


def show_status(player):
    print(f"\nHealth: {player.health}")
    print(f"Inventory: {player.inventory}")


def explore_dark_woods(player):
    print("\nYou explore the Dark Woods.")
    if "lantern" not in player.inventory:
        print("You found a lantern.")
        player.inventory.append("lantern")
    else:
        print("There is nothing else to find here.")


def explore_mountain_pass(player):
    print("\nYou explore the Mountain Pass.")
    if "map" not in player.inventory:
        print("You found a map.")
        player.inventory.append("map")
    else:
        print("There is nothing else to find here.")


def explore_cave(player):
    print("\nYou explore the Cave.")
    if "lantern" not in player.inventory:
        print("It is too dark without a lantern. You get hurt.")
        player.health -= 10
    else:
        if "treasure" not in player.inventory:
            print("Using your lantern, you find the treasure!")
            player.inventory.append("treasure")
        else:
            print("You already found the treasure here.")


def explore_hidden_valley(player):
    print("\nYou explore the Hidden Valley.")
    if "map" not in player.inventory:
        print("You are lost without a map and get hurt.")
        player.health -= 10
    else:
        if "rare herbs" not in player.inventory:
            print("Using your map, you find the rare herbs!")
            player.inventory.append("rare herbs")
        else:
            print("You already found the rare herbs here.")


def stay_still(player):
    print("\nYou stay still and waste time.")
    print("You lose 10 health.")
    player.health -= 10


def main():
    player = Player()

    while True:
        print("\n=== Adventure Game ===")
        print("1. Explore Dark Woods")
        print("2. Explore Mountain Pass")
        print("3. Explore Cave")
        print("4. Explore Hidden Valley")
        print("5. Stay Still")
        print("6. Quit")

        choice = input("Choose an action: ")

        if choice == "1":
            explore_dark_woods(player)
        elif choice == "2":
            explore_mountain_pass(player)
        elif choice == "3":
            explore_cave(player)
        elif choice == "4":
            explore_hidden_valley(player)
        elif choice == "5":
            stay_still(player)
        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

        show_status(player)
        check_lose(player)
        check_win(player)


main()