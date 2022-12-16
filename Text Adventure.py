# Text Adventure Game by Aden Chen

# Import modules
import random
import time

# Global Variables
inventory = []
luck = random.randint(0, 100)
password = random.randint(0, 9999)

# End
def you_died(why):
    print(why)
    print("Game Over!")
    exit()

def freedom():
    print("You have escaped from the cave! Congratuations!")
    print("You have "+str(len(inventory))+" treasures in your bag!")
    time.sleep(2)
    print("Thanks for playing :)")
    exit()

# NPC's/Enemies
def dragon():
    if "Sword" in inventory:
        haveSword = True
    elif "Bow and arrow" in inventory:
        haveBow = True

    print("You walk down a set of stairs into a new room. ")
    time.sleep(2)
    print("Suddenly, you stop dead in your tracks when you see a red fierce dragon sleeping in front of you.")
    action = input("Do you run away from the dragon or do you fight it? Type run/fight > ").lower()

    while True:
        if action == "run" and luck >= 75:
            print("The dragon wakes up and sees you running away.")
            time.sleep(2)
            print("By the time the dragon tries to chase you, you have already escaped from the room.")
            exit()
        elif action == "run" and luck <= 75:
            print("The dragon wakes up and sees you running away.")
            time.sleep(2)
            you_died("He is faster than he looks and you are killed by the dragon...")
        elif action == "fight":
            print("You attempt to fight the dragon and throw a rock at it to get its attention.")
            time.sleep(2)
            print("The dragon is instantly mad at you!")

            if haveSword:
                fight = input("Type s to use your sword.")
                while True:
                    if fight == "s" and luck > 50:
                        print("The dragon is no match for your sword!")
                        time.sleep(2)
                        print("You win!")
                        freedom()
                    else:
                        you_died("The dragon burns your sword into ashes and you die like a crisp bacon.")
            elif haveBow:
                fight = input("Type b to use your bow.")
                while True:
                    if fight == "b" and luck > 50:
                        print("You shoot the dragon with an arrow and it instantly dies!")
                        time.sleep(2)
                        print("You win!")
                        freedom()
                    else:
                         you_died("The dragon burns your bow into ashes and you die like a crisp bacon.")
            else:
                you_died("You are no match for the dragon...")

        else:
            print("Didn't really get you there. Try again.")
            action = input("Do you run away from the dragon or do you fight it? Type run/fight > ").lower()

def slime():
    time.sleep(2)
    print("You take a step in and you see a great green slime up ahead looking at you through its narrow eye.")
    while True:
        next_move = input("Do you flee for your life or fight? Type flee/fight > ").lower()
        if next_move == "flee" and luck > 50:
            print()
            print("You managed to escape from the slime!")
            time.sleep(2)
            bridge()
        elif next_move == "flee" and luck < 50:
            you_died("You got slimed! Well that was tasty...")
        elif next_move == "fight" and luck > 50:
            print("You try to attack the slime and it disappears.")
            print("You collect a coin.")
            print("Your inventory: "+str(inventory))
            inventory.append("Coin")
            break
        elif next_move == "fight" and luck < 50:
            you_died("You got slimed! Well that was tasty...")
        else:
            print("That is not a valid answer.")
            continue

def wizard():
    global password
    print("You have a talk with the wizard and he tells you that there is secret room full of treasure.")
    time.sleep(2)
    print("The wizard says that a password is required to get in.")
    code = input("Type password to figure out the code or exit to stop talking with the wizard > ").lower()
    while True:
        if code == "password":
            print("He tells you the password is "+str(password))
            treasure()
        elif code == "exit":
            print("You move deeper into the cave.")
            treasure()
        else:
            print("Invalid answer.")
            code = input("The wizard says that a password is required to get in. Type password to get the code or exit to stop talking with the wizard > ")

# Hunger
def food():
    print("You find yourself feeling hungry.")
    time.sleep(2)
    print("You reach into your inventory to find something to eat > ")
    print("Your inventory: "+str(inventory))
    while True:
        eat = input("Select something to get rid of your hunger.")
        if eat in inventory:
            if eat == "Carrot" or eat == "Apple" or eat == "Cake":
                if luck > 33:
                    print("You eat a "+eat+" and your hungry feelings go away.")
                    inventory.remove(eat)
                    dragon()
                else:
                    you_died("You died of starvation.")
            else:
                print("You cannot eat that.")
                eat = input("Select something to get rid of your hunger > ")
        else:
            print("You don't have that item.")
            eat = input("Select something to get rid of your hunger > ")
    
# Traps
def boulder():
    print("You hear a clicking sound as you walk towards the exit of the room you are standing in. ")
    time.sleep(2)
    print("Soon you see a huge boulder rolling towards your direction!")
    print("You can either go left or right to dodge the boulder.")

    while True:
        escape = input("Which direction do you go? Type left/right > ").lower()
        if escape == "left" and luck > 50:
            print("CRASH!")
            print("You manage to get out of the boulder's path in time by jumping to the left.")
            time.sleep(2)
            food()
        elif escape == "left" and luck < 50:
            you_died("You were crushed by the boulder...")
        elif escape == "right" and luck > 50:
            print("CRASH!")
            print("You manage to get out of the boulder's path in time by jumping to the right.")
            time.sleep(2)
            dragon()
        elif escape == "right" and luck < 50:
            you_died("You were crushed by the boulder...")
        else:
            print("I don't understand.")
            escape = input("Which direction do you go? Type left/right > ").lower()

def treasure():
    global password
    global inventory
    treasure_chest = ["Diamonds", "Gold", "Sword", "Carrot", "Apple"]
    treasure_chest2 = ["Health potion", "Silver", "Bow and arrow", "Cake"]
    print("You continue to walk and find a lever on the wall.")
    time.sleep(2)
    print("You pull the lever down and a closed secret entrance with a key pad attached to it shows up.")
    while True:
        pin = input("Enter Password: ")
        if int(pin) == password:
            print("The password works and you make it inside the room!")
            time.sleep(2)
            print("Inside the room you see two treasure chests that may contain weapons, gems, and supplies.")
            chest = input("Press 1 to open the first chest, 2 to open the second, or 3 to leave it alone. > ").lower()
            while True:
                if chest == "1":
                    print("The chest creaks open.")
                    for treasure in treasure_chest:
                        inventory.append(treasure)
                    print("You collect all of this loot.")
                    time.sleep(2)
                    print("Your inventory: "+str(inventory))
                    boulder()
                elif chest == "2":
                    print("The chest creaks open.")
                    for treasure in treasure_chest2:
                        inventory.append(treasure)
                    print("You collect all of this loot.")
                    time.sleep(2)
                    print("Your inventory: "+str(inventory))
                    boulder()
                elif chest == "3":
                    dragon() 
                else:
                    print("That is not a valid answer")
                    chest = input("Press 1 to open the first chest, 2 to open the second, or 3 to leave it alone. > ").lower()
        else:
            print("Incorrect. Try again.")
    
def bridge():
    print("As you keep running away, you stop when a yellow bridge appears in front of you.")
    bridge = input("Do you want to go across? Type yes/no > ").lower()
    while True:
        if bridge == "yes" and luck > 66:
            print("You made it across!")
            boulder()
        elif bridge == "yes" and luck < 66:
            you_died("The bridge breaks all of a sudden and you fall down a bottemless pit.")
        elif bridge == "no":
            you_died("You go back and the slime finds you. Your vision suddenly goes black...")
        else:
            print("Type yes or no.")
            bridge = input("Do you want to go across?")

# Doors
def red_door():
    global inventory
    have_key = True
    print("You approach the door and find that it is locked.")
    if "key" not in inventory:
        have_key = False
    time.sleep(2)
    enter = input("Would you like to open it? Type yes/no > ").lower()
    while True:
        if have_key and enter == "yes":
            print("You sucessfully opened the door!")
            inventory.remove("key")
            print("Your inventory: "+str(inventory))
            slime()
        elif not have_key and enter == "yes":
            print("You don't have a key to enter the door and walk over to the blue one.")
            blue_door()
        elif enter == "no":
            print("You walk over to the blue door instead.")
            blue_door()
        else:
            print("That is not a valid answer.")
            enter = input("Would you like to open it? Type yes/no > ").lower()
    
def blue_door():
    global wizard
    print("You decide to go to the blue door.")
    print("When you walk inside, you discover that you are not alone.")
    time.sleep(2)
    choice = input("You see a wizard who seems just as lost as you are. Press 1 to talk and Press 2 to go to the red door. > ").lower()
    while True:
        if choice == "1":
            wizard()
        elif choice == "2":
            red_door()
        else:
            print("Invaild answer")
            wizard = input("You see a wizard who seems just as lost as you are. Press 1 to talk and Press 2 to go to the red door. > ").lower()
           
# Beginning
def start():
    global inventory
    name = input("What is your name? > ")
    print("Nice to meet you "+name+" :)")
    time.sleep(2)
    print("You are lost in the woods when you come across a dark cave. ")
    print("Your inventory: "+str(inventory))
    cave = input("Do you want to explore or ignore the cave? Type explore/ignore > ").lower()
    while True:
        if cave == "explore":
            time.sleep(2)
            print("You find a golden key on the floor.")
            key = input("Would you like to put it in your inventory? Type yes/no > ").lower()
            while True:
                if key == "yes":
                    inventory.append("Key")
                    print("Your inventory: "+str(inventory))
                    break
                elif key == "no":
                    print("You don't pick up the key.")
                    break
                else:
                    print("Please type yes or no.")
                    key = input("Would you like to put it in your inventory? Type yes/no > ").lower()
                
            print("You decide to walk inside and find a red and a blue door on opposite sides of the cave.")
            time.sleep(2)
            door = input("Which door do you want to enter? Type red/blue > ").lower()
            while True:
                if door == "red":
                    red_door()
                elif door == "blue":
                    blue_door()
                else:
                    print("I'm not sure if I understand.")
                    door = input("Which door do you want to enter? Type red/blue > ").lower()
        elif cave == "ignore":
            you_died(name+" ignores the cave and dies from starvation.")
        else:
            print("Sorry, that isn't a valid answer.")
            cave = input("Do you want to explore or ignore the cave? Type explore/ignore > ").lower()

if __name__ == '__main__':
    start()
