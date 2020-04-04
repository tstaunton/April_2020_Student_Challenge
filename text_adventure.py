import time

print("\n" * 200)
print(">>>>>>>>> Text Adventure Game <<<<<<<<<<")
print("\n" * 3)
time.sleep(3)
print("\nA long time ago in a galaxy far far away, a warrior was born.")
time.sleep(1)
print("Does this warrior have a name?")
name=raw_input("> ")
print(name, "blaster in hand and looking for adventure!")
time.sleep(1)
print("As always, when a brave warrior looks for adventure, evil is nearby...")
time.sleep(1)
print("From the shadows, icy grey eyes fix on the hero...")
time.sleep(1)
print("Will", name, "be victorious, and save the galaxy...?")
time.sleep(1)
print("Or perish at the hands of the unknown evil?")
time.sleep(1)
print("\n" * 3)
print("Time will tell...")
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(5)
print("\n" * 200)

print("You find yourself in a small, run down bar. You have a small amount of money and your blaster."  + "\nYou're ready for your next adventure. In the bar with you are three others. An old man, and two dangerous looking soliders.")

def start():
    print("\n ----------")
    print("Do you approach the...")
    print("\n")
    print("1. The old man")
    print("2. The two dangerous looking soliders")

    cmdlist=["1", "2"]
    cmd=getcmd(cmdlist)
    if cmd == "1":
        old()
    elif cmd == "2":
        soliders()

def old():
    print("\n" * 200)
    print("You get up off of your bar stool, and walk up to the old man and greet him.\n")
    print("He smiles a tootless smile at you. He knows you seek adventure.")
    print("He mumbles, 'Buy me a cup of spirits and I'll tell you a story...' ")
    time.sleep(2)

def soliders():
    print("\n" * 200)
    print("You get up off of your bar stool, and walk over to the two soliders. Hand on your blaster.\n")
    print("The soliders are not happy that you have disturbed them. One grunts 'Yes boy...'")
    print("You can tell the grunting guard has a blaster, ready, under the table.")
    time.sleep(2)

def getcmd(cmdlist):
    cmd = raw_input(name + ">")
    if cmd in cmdlist:
        return cmd
    elif cmd == "help":
        print("\nEnter your choice...")
        print("or enter 'quit' to leave the game")
        return getcmd(cmdlist)
    elif cmd == "quit":
        print("\n ----------")
        time.sleep(1)
        print("You have chosen to return to your barstool...")
        time.sleep(5)
        exit()

if __name__ == "__main__":
    start()
