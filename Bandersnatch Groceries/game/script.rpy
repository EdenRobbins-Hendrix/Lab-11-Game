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

    # This ends the game.

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

    return

label aisle_menu:
    menu:
        set visited_aisles
        j "Which aisle should I go to first?"

        "Go to dairy aisle":
            jump dairy_aisle

        "Go to produce aisle":
            jump produce_aisle

        "Go to canned vegetables aisle":
            jump vegetables_aisle

        "Go to arts and crafts aisle":
            jump arts_aisle

        "Go to clothing aisle":
            jump clothing_aisle

label dairy_aisle:
    j "Guess I'm done shopping"
    jump aisle_menu
    

label produce_aisle:
    j "Guess I'm done shopping"
    jump aisle_menu

label vegetables_aisle:
    j "Guess I'm done shopping"
    jump aisle_menu

label arts_aisle:
    j "Guess I'm done shopping"
    jump aisle_menu

label clothing_aisle:
    j "Guess I'm done shopping"
    jump aisle_menu


