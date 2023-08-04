# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ak = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    ak "uurgh.. -uhgh.. -tf"
    ak "uuh.. ne-. ne oldu bana.. bruh"
    ak "neredeyim ben?.."
    
    menu:
        "Kimse var mı?!!":  # Kullanıcının seçeceği seçenekler
            ak "Kimse yokmu!! HEEY!!"       
        "Kapı aralığından bak":  # Kullanıcının seçeceği diğer seçenek
            "" "..."

    

    return
