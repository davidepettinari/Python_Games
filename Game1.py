import time

# Define the player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def has_item(self, item_name):
        return item_name in self.inventory

    def add_item(self, item_name):
        self.inventory.append(item_name)

# Define the room class
class Room:
    def __init__(self, name, description, exits, items):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items

# Define the game class
class AdventureGame:
    def __init__(self):
        self.player = None
        self.current_room = None
        self.rooms = {}

    # Method to add a room to the game
    def add_room(self, room):
        self.rooms[room.name] = room

    # Method to start the game
    def start(self):
        print("Welcome to the adventure game!")
        self.player = Player(input("What is your name? "))
        self.current_room = self.rooms['start']
        print(self.current_room.description)

        # Loop until the game ends
        while True:
            command = input("> ")
            if command.startswith("go "):
                direction = command.split()[1]
                if direction in self.current_room.exits:
                    self.current_room = self.rooms[self.current_room.exits[direction]]
                    print(self.current_room.description)
                else:
                    print("You can't go that way!")
            elif command.startswith("take "):
                item_name = command.split()[1]
                if item_name in self.current_room.items:
                    self.player.add_item(item_name)
                    self.current_room.items.remove(item_name)
                    print(f"You took the {item_name}.")
                else:
                    print("That item is not in this room.")
            elif command.startswith("use "):
                item_name = command.split()[1]
                if self.player.has_item(item_name):
                    if self.current_room.name == "final" and item_name == "key":
                        print("You won the game!")
                        break
                    else:
                        print("Nothing happens.")
                else:
                    print("You don't have that item.")
            elif command == "inventory":
                if len(self.player.inventory) == 0:
                    print("Your inventory is empty.")
                else:
                    print("Your inventory contains: ")
                    for item in self.player.inventory:
                        print(item)
            elif command == "quit":
                print("Goodbye!")
                break
            else:
                print("Invalid command.")

# Create the game object and add rooms
game = AdventureGame()
game.add_room(Room("start", "You are in a dark room. There is a door to the north.", {"north": "room1"}, []))
game.add_room(Room("room1", "You are in a hallway. There is a door to the east and to the west.", {"east": "room2", "west": "start"}, ["key"]))
game.add_room(Room("room2", "You are in a bright room. There is a door to the south.", {"south": "final"}, []))
game.add_room(Room("final", "You are in a room with a locked door. There is a key on the table.", {}, ["key"]))


# Start the game
game.start()
