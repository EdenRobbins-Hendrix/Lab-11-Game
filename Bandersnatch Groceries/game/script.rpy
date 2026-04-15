# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("John Bandersnatch")

define w = Character("Allison the Cashier Witch")

define e = Character("Janitor")

init python:
    class GroceryItem:
        def __init__(self, name, cost, image, classification):
            self.name = name
            self.cost = float(cost)
            self.image = image
            self.classification = classification

# Dairy 
default cow_milk = GroceryItem("Cow Milk", 3.50, "Cow Milk", ["milk_item"])
default soy_milk = GroceryItem("Soy Milk", 4.00, "Soy Milk", ["milk_item"])

# Produce
default corn_cob = GroceryItem("Corn on the cob", 4.50, "Corn", ["side_item"])
default corn_hair = GroceryItem("Corn hair", 0, "Corn Hair", ["coarse_thin", "long_yellow"])
default banana = GroceryItem("Banana", 1.00, "Banana", ["long_yellow"])

# Only achievable if John has the corn cob and scissors
default corn_hairless = GroceryItem("Corn on the cob (hairless)", 5.50, "Corn Hairless", ["side_item"])

# In the "canned" aisle, but is a standin for when 
# I can take a new picture for the fish aisle
default salmon = GroceryItem("Cape-brand Salmon", 10.00, "Salmon", ["fishy", "side_item"])
default soy_fish = GroceryItem("Soy-based faux-fish", 8.00, "Soy Fish", ["fishy"])

# Clothing aisle (don't have a picture for this either)
default shirt = GroceryItem("Yellow sequin shirt", 20.00, "Shirt", ["clothing_item"])
default shoes = GroceryItem("Golden glittery shoes", 25.00, "Shoes", ["clothing_item"])

# Arts and crafts aisle
default thread = GroceryItem("Golden thread", 15.00, "Thread", ["coarse_thin", "long_yellow"])
default scissors = GroceryItem("Scissors", 5.00, "Scissors", ["needed_for_long_yellow"])

# define milk_item = ["cow_milk"]
# define side_item = ["corn_cob", "corn_hairless", "salmon"]
# define clothing_item = ["shoes", "shirt"]

# define long_yellow = ["thread", "banana", "corn_hair"]
# define coarse_thin = ["corn_hair", "thread"]
# define fishy = ["soy_fish", "salmon"]

define john_wants = ["milk_item", "side_item", "clothing_item"]
define witch_wants = ["long_yellow", "coarse_thin", "fishy"]

default inventory = []
default last_visited = ""
default john_script = ""

default leave = False

default visited_aisles = set()

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg enter

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jon bander

    # These display lines of dialogue.

    j "So, this is the grocery store that my family told me never to enter...I guess it's only a few items though."

    j "Let's see what this store has in store for me tonight."

    scene bg cashier
    with Dissolve(0.5)

    pause 0.5

    show allison witch
    with Dissolve(0.5)

    w "Hehehe, hello my pretty! It is good to see you after all this time. Why have you come to my store?"

    j "I'm looking for some items of mine. I'm in a pinch, so I want to leave quickly."

    w "Not so fast! I want some items too! They are ..."

    j "Fine, but I'm only entering each aisle once, so if I can't find the item the first time I go through, I'm not going back."


    jump aisle_menu
    with Dissolve(0.5)

    # This ends the game.

    return

label aisle_menu:
    python:
        if last_visited == "":
            john_script = "I guess I should start shopping. Where should I head to first?"
        else:
            john_script = f"I hope I got everything from the {last_visited} aisle. Now, where should I head to next?"
        if len(visited_aisles) == 5:
            leave = True
    
    if leave:
        jump completed
        with Dissolve(0.5)

    scene bg aisle1
    with Dissolve(0.5)
    menu:
        set visited_aisles
        j "[john_script]"

        "Go to the dairy aisle.":
            $ last_visited = "dairy"
            jump dairy_aisle

        "Go to the produce aisle.":
            $ last_visited = "produce"
            jump produce_aisle

        "Go to the canned vegetables aisle.":
            $ last_visited = "canned vegetables"
            jump canned_aisle

        "Go to the arts and crafts aisle.":
            $ last_visited = "arts and crafts"
            jump arts_aisle

        "Go to the clothing aisle.":
            $ last_visited = "clothing"
            jump clothing_aisle

        "Leave the store." if len(visited_aisles) > 0:
            $ leave = True
            jump completed

label completed:
    scene bg cashier
    j "I got your items. Now go!"

    return

label dairy_aisle:
    scene bg dairy
    with Dissolve(0.5)

    menu:
        "What should I get?"
        "Get soy milk.":
            item = soy_milk
            $ inventory.append(soy_milk)
            
        "Get cow milk.":
            item = cow_milk
            $ inventory.append(cow_milk)
    show item.image
    j "Guess I'm done shopping"
    hide item.image
    if len(visited_aisles) == 1:
        e "Hey, you shouldn't be here!'"
    elif len(visited_aisles) == 2:
        e "I warned you..."
    jump aisle_menu
    

label produce_aisle:
    scene bg produce
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get banana.":
            item = banana
            $ inventory.append(banana)
        "Get corn on the cob.":
            item = corn_cob
            $ inventory.append(corn_cob)
    show item.image
    j "Guess I'm done shopping"
    hide item.image
    if len(visited_aisles) == 1:
        e "Hey, you shouldn't be here!'"
    elif len(visited_aisles) == 2:
        e "I warned you..."
    jump aisle_menu

label canned_aisle:
    scene bg canned
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get cape-brand salmon.":
            item = salmon
            $ inventory.append(salmon)
        "Get soy-based faux-fish.":
            item = soy_fish
            $ inventory.append(soy_fish)
    show item.image
    j "Guess I'm done shopping"
    hide item.image
    if len(visited_aisles) == 1:
        e "Hey, you shouldn't be here!'"
    elif len(visited_aisles) == 2:
        e "I warned you..."
    jump aisle_menu

label arts_aisle:
    scene bg arts
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get scissors.":
            item = scissors
            $ inventory.append(scissors)
        "Get golden thread.":
            item = thread
            $ inventory.append(thread)
    show item.image
    j "Guess I'm done shopping"
    hide item.image
    if len(visited_aisles) == 1:
        e "Hey, you shouldn't be here!'"
    elif len(visited_aisles) == 2:
        e "I warned you..."
    jump aisle_menu

label clothing_aisle:
    scene bg aisle2
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get yellow sequin shirt.":
            item = shirt
            $ inventory.append(shirt)
        "Get golden glittery shoes.":
            item = shoes
            $ inventory.append(shoes)
    show item.image
    j "Guess I'm done shopping"
    hide item.image
    if len(visited_aisles) == 1:
        e "Hey, you shouldn't be here!'"
    elif len(visited_aisles) == 2:
        e "I warned you..."
    jump aisle_menu


