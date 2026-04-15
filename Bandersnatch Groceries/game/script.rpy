# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("John Bandersnatch")

define w = Character("Allison the Cashier Witch")

init python:
    class GroceryItem:
        def __init__(self, name, cost, image):
            self.name = name
            self.cost = float(cost)
            self.image = image

default cow_milk = GroceryItem("Cow Milk", 3.50, "Cow Milk")
default corn_cob = GroceryItem("Corn on the cob", 4.50, "Corn")

define milk_item = ["cow_milk"]
define side_item = ["corn_cob", "corn_hairless", "salmon", "corn_hairless"]
define clothing_item = ["shoes", "shirt"]

define long_yellow = ["thread", "banana", "corn_hair"]
define coarse_thin = ["corn_hair", "thread"]
define fishy = ["soy_fish", "salmon"]

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
            $ inventory.append(soy_milk)

        "Get cow milk.":
            $ inventory.append(cow_milk)

    j "Guess I'm done shopping"
    jump aisle_menu
    

label produce_aisle:
    scene bg produce
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get banana.":
            $ inventory.append(banana)
        "Get corn on the cob.":
            $ inventory.append(corn_cob)
    j "Guess I'm done shopping"
    jump aisle_menu

label canned_aisle:
    scene bg canned
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get cape-brand salmon.":
            $ inventory.append(salmon)
        "Get soy-based faux-fish.":
            $ inventory.append(soy_fish)

    j "Guess I'm done shopping"
    jump aisle_menu

label arts_aisle:
    scene bg arts
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get scissors.":
            $ inventory.append(scissors)
        "Get golden thread.":
            $ inventory.append(thread)
    j "Guess I'm done shopping"
    jump aisle_menu

label clothing_aisle:
    scene bg aisle2
    with Dissolve(0.5)

    menu:
        "What should I get?"

        "Get yellow sequin shirt.":
            $ inventory.append(shirt)
        "Get golden glittery shoes.":
            $ inventory.append(shoes)

    j "Guess I'm done shopping"
    jump aisle_menu


