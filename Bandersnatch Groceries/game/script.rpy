# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("John Bandersnatch")

define w = Character("Allison the Cashier Witch")

define e = Character("Janitor")

# Code for running a timer

init python:
    class GroceryItem:
        def __init__(self, name, cost, image, classification):
            self.name = name
            self.cost = float(cost)
            self.image = "VN icons/" + image + ".png"
            self.classification = classification

        def display_item(self):
            return f"{self.name.lower()} (${self.cost:.2f})"

# Dairy 
default cow_milk = GroceryItem("Cow Milk", 3.50, "Cow Milk", ["milk"])
default soy_milk = GroceryItem("Soy Milk", 4.00, "Soy Milk", ["milk"])

# Produce
default corn_cob = GroceryItem("Corn on the cob", 4.50, "Corn", ["side"])
default corn_hair = GroceryItem("Corn hair", 0, "Corn Hair", ["coarse_thin", "long_yellow"])
default banana = GroceryItem("Banana", 1.00, "Bananas", ["long_yellow"])

# Only achievable if John has the corn cob and scissors
default corn_hairless = GroceryItem("Corn on the cob (hairless)", 5.50, "Corn Hairless", ["side"])

# In the "canned" aisle, but is a standin for when 
# I can take a new picture for the fish aisle
default salmon = GroceryItem("Cape-brand Salmon", 10.00, "Salmon", ["fishy", "side"])
default soy_fish = GroceryItem("Soy-based faux-fish", 8.00, "Faux Fish", ["fishy"])

# Clothing aisle (don't have a picture for this either)
default shirt = GroceryItem("Yellow sequin shirt", 20.00, "Shirt", ["clothing"])
default shoes = GroceryItem("Golden glittery shoes", 25.00, "Shoes", ["clothing"])

# Arts and crafts aisle
default thread = GroceryItem("Golden thread", 15.00, "Threads", ["coarse_thin", "long_yellow"])
default scissors = GroceryItem("Scissors", 5.00, "Scissors", ["needed_for_long_yellow"])

# define milk_$ item = ["cow_milk"]
# define side_$ item = ["corn_cob", "corn_hairless", "salmon"]
# define clothing_$ item = ["shoes", "shirt"]

# define long_yellow = ["thread", "banana", "corn_hair"]
# define coarse_thin = ["corn_hair", "thread"]
# define fishy = ["soy_fish", "salmon"]

default inventory = []
default unique_ids = set()
default john_wants = ["milk", "side", "clothing"]
default j_missing_wants = []
default witch_wants = ["long_yellow", "coarse_thin", "fishy"]
default w_missing_wants = []

default last_visited = ""
default john_script = ""
default end = ""
default witch_ending = ""

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

    play music "audio/Theme.mp3"

    # These display lines of dialogue.

    j "Ugh, I can't believe I have to go to the grocery store. I hate grocery shopping."

    j "But I guess I have to go in if I want to get the items I need for my project."

    j "I need to get some milk, something for a side dish, and something to wear. I hope I can find everything I need."

    j "So, this is the grocery store that my family told me never to enter...I guess it's only a few items though."

    j "Let's see what this store has in store for me tonight."

    scene bg cashier
    with Dissolve(0.5)

    jump witch_welcome

label witch_welcome:
    scene bg cashier
    pause 1

    play music "audio/Witch.mp3"

    show allison witch
    with Dissolve(0.5)

    w "Hehehe, hello my pretty! It is good to see you after all this time. Why have you come to my store?"

    j "I'm looking for some items of mine. I'm in a pinch, so I want to leave quickly."

    w "Not so fast! I want some items too! I want a long yellow item, a coarse and thin item, and a fishy item. If you can get those for me, I'll let you leave."

    j "Fine, but I'm only entering each aisle once, so if I can't find the item the first time I go through, I'm not going back."

    stop music 

    play music "audio/Theme.mp3"

    jump aisle_menu
    with Dissolve(0.5)

    # This ends the game.

    return

label witch_final:
    
    stop music
    pause 0.5
    play music "audio/Witch.mp3"
    scene bg cashier

    show allison witch
    with Dissolve(0.5)

    python:
        def format_missing_items(items, w_bool=False):
            noun = "You are" if w_bool else "I am"
            if not items:
                return f"{noun} not missing anything!"

            processed = [s.replace("_", " and ") + " item" for s in items]

            count = len(processed)

            str_start = f"{noun} missing a"
            if count == 1:
                return f"{str_start} {processed[0]}."
            elif count == 2:
                return f"{str_start} {processed[0]} and a {processed[1]}."
            else:
                commas = ", a ".join(processed[:-1])
                return f"{str_start} {commas}, and a {processed[-1]}."

        for item in inventory:
            for item_id in item.classification:
                unique_ids.add(item_id)

        w_missing_wants = [w for w in witch_wants if w not in unique_ids]
        j_missing_wants = [j for j in john_wants if j not in unique_ids]

        witch_dialgue = format_missing_items(w_missing_wants, w_bool=True)
        john_dialgue = format_missing_items(j_missing_wants)
    
    menu:
        w "Ugh, it's you again. Did you get the items I wanted?"

        "Yes, here you go." if len(w_missing_wants) == 0 and corn_hair in inventory:
            w "Wow. I'm actually impressed that you were able to find these. Wait, are these corn hairs? MY FAVORITE!"

            w "Thank you, John. See you later."

            $ witch_ending = "corn hairs"
        
        "Yes, here you go." if len(w_missing_wants) == 0 and corn_hair not in inventory:
            w "Wow. I'm actually impressed that you were able to find these."

            w "Good ridance with you now!"
            
            $ witch_ending = "all items"
        
        "No, because I frankly do not like you.":
            w "HOW RUDE!"

            w "Be gone, John Bandersnatch!!!"

            $ witch_ending = "mean"

        "I tried, but I couldn't get enough items." if len(inventory) < len(witch_wants):
            w "You come to MY counter with only [len(inventory)] items? Did you even try??"

            w "Be gone!!"

            $ witch_ending = "tried"

        "I only got my items." if len(j_missing_wants) == 0 and len(w_missing_wants) > 0:
            w "I can't say I'm surprised. Would it really kill you to just do some extra searching for me?"

            w "Whatever. Get out of here."

            $ witch_ending = "john items only"

        "Sorry, I wasn't able to find all your items." if len(w_missing_wants) > 0:
            w "It looks like you found [len(witch_wants) - len(w_missing_wants)] of my items."

            w "[witch_dialgue]"

            w "Okay. I'm done with you now."
            
            $ witch_ending = "apologetic"
    stop music
        
    jump end
    return

label end:
    python:
        j_inventory_base = "Looks like I had "
        j_lower_inv = [item.name.lower() for item in inventory]
        if len(j_lower_inv) == 1:
            j_inv_append = j_lower_inv[0]
        elif len(j_lower_inv) == 2:
            j_inv_append = f"{j_lower_inv[0]} and {j_lower_inv[1]}"
        else:
            commas = ", ".join(j_lower_inv[:-1])
            j_inv_append = f"{commas}, and {j_lower_inv[-1]}"
        j_inv_string = j_inventory_base + j_inv_append + "."

    scene bg enter
    with Dissolve(0.5)

    show jon bander
    play music "audio/Theme.mp3"

    $ another_shot = "Maybe if I ever end up back here again, I'll give it another shot."

    j "Well, that was an adventure I hope to never take on again."

    if witch_ending == "corn hairs":
        j "I can't believe that I knew to cut the hairs off the corn to give to the witch."

        j "I guess her riddles weren't so tricky after all."

    elif witch_ending == "all items":
        j "I got all of the witches items, but I can't help but feel like she was really wanting another long and yellow item."

        j "[another_shot]"

    elif witch_ending == "mean":
        j "I probably shouldn't have said that I didn't like her, but she was really rude."

    elif witch_ending == "tried":
        j "I probably should have looked more for her items, but I just couldn't find them."

        j "[another_shot]"

    elif witch_ending == "john items only":
        j "I probably should have looked more for her items, rather than just my own."

        j "[another_shot]"

    elif witch_ending == "apologetic":
        j "I'm glad the witch was kind enough to tell me which items I was missing."

        j "[another_shot]"

    j "Lets go over what all I had in my inventory."

    j "[j_inv_string]"

    if len(w_missing_wants) == 0:
        if len(j_missing_wants) == 0:
            j "I can't believe that I found all of my items too!"

            j "I suppose I've earned the badge of an efficient shopper."

            j "But that's all I can take for tonight."
        
        elif len(j_missing_wants) > 0:
            j "I got all her items, but I didn't all of mine."

            j "I guess that shows how much of a good person I am, even though she was rude."

            j "I'll have to come back another night to get my things."
    
    elif len(w_missing_wants) > 0:
        if len(j_missing_wants) == 0:
            j "Looks like I got all of my items, but I was missing [len(w_missing_wants)] of the witch's."

            j "Oh well. I only came here for mine anyways."
        
        elif len(w_missing_wants) > 0:
            j "Dang, I wasn't able to get any of my items, nor hers."

            j "I'll have come back again to actually do some shopping."

            j "At least I did get some items, so I have that to cherish."

    j "Goodnight!"

    return

label aisle_menu:

    python:
        if last_visited == "":
            john_script = "I guess I should start shopping. Where should I head to first?"
        else:
            john_script = f"I hope I got the right item from the {last_visited} aisle. Now, where should I head to next?"
        if len(visited_aisles) == 5:
            leave = True

    if leave:
        jump witch_final
        with Dissolve(0.5)
    
    scene bg aisle1
    with Dissolve(0.5)
    menu:
        set visited_aisles
        j "[john_script]"

        "Go to the dairy aisle.":
            $ last_visited = "dairy"
            call shopping_aisle("bg dairy", soy_milk, cow_milk)

        "Go to the produce aisle.":
            $ last_visited = "produce"
            call shopping_aisle("bg produce", banana, corn_cob)

        "Go to the canned vegetables aisle.":
            $ last_visited = "canned vegetables"
            call shopping_aisle("bg canned", salmon, soy_fish)

        "Go to the arts and crafts aisle.":
            $ last_visited = "arts and crafts"
            call shopping_aisle("bg arts", scissors, thread)

        "Go to the clothing aisle.":
            $ last_visited = "clothing"
            call shopping_aisle("bg aisle2", shirt, shoes)

        "Leave the aisles." if len(visited_aisles) > 0:
            $ leave = True
            jump witch_final
            with Dissolve(0.5)
    
    return



label shopping_aisle(bg, item1, item2):
    # Start janitor timer if len(visited_aisles) > 2
    scene expression bg
    with Dissolve(0.5)

    menu:
        j "What should I get?"
        "Get [item1.display_item()].":
            $ item = item1
        "Get [item2.display_item()].":
            $ item = item2
    $ inventory.append(item)
    show expression item.image as shopping_item
    j "That'll come in handy."
    hide shopping_item
    if len(visited_aisles) == 1:
        e "Hey, you shouldn't be here!'"
    elif len(visited_aisles) == 2:
        e "I warned you..."
        jump janitor_interaction
    
    # Reset janitor timer

    jump aisle_menu

label janitor_interaction:
    scene bg aisle1
    with Dissolve(0.5)

    show joe janitor
    with Dissolve(0.5)

    e "I see you've been here for a while. You should leave soon, or else..."

    jump aisle_menu
