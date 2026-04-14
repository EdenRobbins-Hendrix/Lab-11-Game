# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("John Bandersnatch")

define w = Character("Allison the Cashier Witch")


define milk_item = [cow_milk]
define side_item = [corn_cob, corn_hairless, salmon]
define clothing_item = [shoes, shirt]

define long_yellow = [thread, banana, corn_hair]
define coarse_thin = [corn_hair, thread]
define fishy = [soy_fix, salmon]

define john_wants = [milk_item, side_item, clothing_item]
define witch_wants = [long_yellow, coarse_thin, fishy]

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

    return
