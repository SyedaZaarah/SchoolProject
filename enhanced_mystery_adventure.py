class Game:
    def __init__(self):  # Constructor method to initialize game attributes
        self.inventory = []  # An empty inventory list
        self.room = 1  # Initialize the starting room

    def start(self):
        print("Welcome to the Mystery Adventure!")
        while True:
            if self.room == 1:
                self.room_one()
            elif self.room == 2:
                self.room_two()
            elif self.room == 3:
                self.room_three()
            elif self.room == 4:
                self.room_four()
            elif self.room == 5:
                self.end_game()

    def room_one(self):
        print("\nYou are in a dark  room with two doors: one to the left and one to the right.")
        choice = input("Do you want to go left or right? ").strip().lower()

        if choice == "left":
            print("You find a key on the floor and add it to your inventory.")
            self.inventory.append("key")
            self.room = 2
        elif choice == "right":
            print("You walk into a trap and have to go back!")
        else:
            print("Invalid choice! Try again.")

    def room_two(self):
        print("\nYou enter a room with a locked door. There’s a puzzle on the wall.")
        print("Solve this riddle: 'I speak without a mouth and hear without ears. What am I?'")
        answer = input("Your answer: ").strip().lower()

        if answer == "echo":
            if "key" in self.inventory:
                print("You unlock the door with the key and move to the next room.")
                self.room = 3
            else:
                print("You need a key to escape! Try to find it.")
        else:
            print("Incorrect answer! You need to solve the puzzle.")

    def room_three(self):
        print("\nYou find yourself in a library filled with dusty books. A large bookshelf blocks the exit.")
        print("There is a strange book titled 'The Secret of the Hidden Door.'")
        choice = input("Do you want to read the book or search the room? ").strip().lower()

        if choice == "read":
            print("The book reveals a secret passage behind the bookshelf!")
            self.room = 4
        elif choice == "search":
            print("You find a dusty old map that might help you later.")
            self.inventory.append("map")
        else:
            print("Invalid choice! Try again.")

    def room_four(self):
        print("\nYou enter a secret passage leading to a dark room. There's a safe on the wall.")
        print("To open the safe, you need a code. The clue is: 'The first prime number.'")
        answer = input("What is the code? ").strip()

        if answer == "2":
            print("The safe opens, and you find a mysterious artifact!")
            self.inventory.append("artifact")
            self.room = 5
        else:
            print("Wrong code! You need to find the correct number.")

    def end_game(self):
        print("\nCongratulations! You've escaped the mystery room with the following items:")
        print(", ".join(self.inventory) if self.inventory else "No items collected.")
        print("Thanks for playing! Your adventure ends here.")
        exit()

# Main block to run the game
if __name__ == "__main__":
    game = Game()
    game.start()
