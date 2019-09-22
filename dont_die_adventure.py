# A text based adventure game.
# The game is built with functions, user input, while loops- 
# -if-else statements, and break. 
# The pattern of the text based adventure game is straightforward.
# User input limited to valid responses (while loop to ensure it), strings, -
# -nested functions.
# Import time module to allow sleep functions in between text.
# This will help to add effect and allow the user to read the lines of text.
import time

# The first function as a message this will be nested in later functions
def start():
    """Begin the Game"""
    print("Welcome to the Adventure!")

# The next 8 functions are exit/restart loops pending user input in the game.
# These allow for the user to lose the game and be able to start from the-
# -beginning without exiting the game or end the game and leave.
# These 8 are all patterned the same, except for the string (text and input)-
# -while True loop, if-else statements, break to exit the loop and ensure-
# there are no infinite loops.
# The user input is limited to 'valid' responses that are predetermined.
# Alternate 'invalid' responses receive a looped messsage for a valid response.
# Each of these are nested within the game play function which allows for an-
# -easy loop back to the start or to end the game.
def cont_or_end():
    """Alt Continue or End"""
    time.sleep(1)
    while True:
        try_try = input(
                    "\n\nGo to the start or leave weak: 'go' or 'weak'"
                    )
        if try_try not in ('go', 'weak'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'go' in try_try:
        return start(), play_game()
    if 'weak' in try_try:
        quit(
            "\nBetter luck next time.  Bidding you Adieu"
            )

def shield_shelter():
    """Alt Continue or End"""
    time.sleep(1)
    while True:    
        s_p = input(
                "\n\nA shield will protect you from enemies, not elements. "
                "The artic cold has numbed and made your brain dumb. "
                "Go to the start or leave weak: 'go' or 'weak'"
                    )
        if s_p not in ('go', 'weak'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'go' in s_p:
        return start(), play_game()
    if 'weak' in s_p:
        quit(
            "\nBetter luck next time.  Bidding you Adieu"
            )
            
def raft_boat():
    """Alt Continue or End"""
    time.sleep(1)
    while True:
        r_b = input(
                    "\n\nA raft is more flotation device than a boat. "
                    "Not a wise decision at all. "
                    "Go to the start or leave weak: 'go' or 'weak'"
                    )
        if r_b not in ('go', 'weak'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'go' in r_b:
        return start(), play_game()
    if 'weak' in r_b:
        quit(
            "\nBetter luck next time.  Bidding you Adieu"
            )
            
def victory():
    """Victory"""
    time.sleep(1)
    while True:
        vi_ct = input(
                    "\n\nPlay again: 'play' or 'bye'"
                    )
        if vi_ct not in ('play', 'bye'):
                print(
                    "A new adventure awaits."
                    )
        else:
            break
    if 'play' in vi_ct:
        return start(), play_game()
    if 'bye' in vi_ct:
        quit(
            "\nQueue the blues music to bid you Adieu"
            )
            
def co_ward():
    """Coward"""
    time.sleep(1)
    while True:
        coward = input(
                    "\n\nYou are a coward that does not take risks. "
                    "Go back to the start coward or leave weak: 'go' or 'weak'"
                    )
        if coward not in ('go', 'weak'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'go' in coward:
        return start(), play_game()
    if 'weak' in coward:
        quit(
            "\nBetter luck next time coward.  Bidding you Adieu"
            )
            
def friend():
    """New Friend"""
    time.sleep(1)
    while True:
        fri_e = input(
                "\nRuler of the seas, but not of the artic lands."
                "\nYou live a long life pillaging the ships of the sea. "
                "\nThe Leviathan a true ally to the end."
                "\nYou both grow old and die.\n"
                "\nGo for Victory in a new quest or End game: 'go' or 'end'"
                    )
        if fri_e not in ('go', 'end'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'go' in fri_e:
        return start(), play_game()
    if 'end' in fri_e:
        quit(
            "\nBetter luck next time.  Bidding you Adieu"
            )
            
def mighty():
    """Not so Mighty"""
    time.sleep(1)
    while True:
        mighty = input(
                "\nA mighty warrior would take his own path."
                "\nPirate Crazy Ears became jealous of your treasures."
                "\nYou died by assasination.  \nA hired mercenary paid for by "
                "none other than Pirate Crazy Ears. "
                "\n\nBe brave and try again or End game: 'brave' or 'end'"
                    )
        if mighty not in ('brave', 'end'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'brave' in mighty:
        return start(), play_game()
    if 'end' in mighty:
        quit(
            "\nBe brave next time.  Bidding you Adieu"
            )

def alien():
    """aliens oh my"""
    time.sleep(1)
    while True:
        al_en = input(
                "\nThe spaceship activates into a hostile alien robot."
                "\nMaybe you ran back into the blizzard and froze to death."
                "\nMaybe you battled the alien robot and died."
                "\nDeath overtakes you either way."
                "\nGo back to the beginning or leave the game?: 'go' or 'end'"
                    )
        if al_en not in ('go', 'end'):
               print(
                "Choose wisely.  Time is fleeting."
                    )
        else:
            break
    if 'go' in al_en:
        return start(), play_game()
    if 'end' in al_en:
        quit(
            "\nA tearful goodbye it is.  Bidding you Adieu"
            )
    
# This function is the actual game play
# While loop, if-else statement, user input, string, and the prior functions.
# The prior functions are nested in making it very easy to have the user- 
# -restart or end the game 
def play_game():
    """Playing the Game"""
    while True:
        player1 = input(
                    "\nEnter your name: "
                    )
        # limiting input to alpha only, non-numeric, non-special characters
        if not player1.isalpha():
            print(
                "\nUse your words mighty warrior.  Letters only."
                )
        else:
            break
            
    print(
            "\nBrave " + player1 + " has entered the game!"
            )

    while True:
        cloak = input(
                    "\nChoose a cloak @,$,%,& "
                    )
        if cloak not in ('@','$','%','&'):
            print(
                "You must choose a cloak mighty warrior."
                )
            time.sleep(1)
        else:
            break
            
    print(
            "\nThe mighty cloak of " + cloak + " has been chosen."
            "\nBe warned...the cloak of " + cloak + " is flammable."
            )
    
    print(
        "\n" + cloak + player1 + 
        " is almost ready to begin the Adventure!"
        )
    
    while True:
        shield = input(
                        "\n" + cloak + player1 + 
                        " choose your shield: #, ], }, | "
                        )
        if shield not in ('#', ']', '}', '|'):
            print(
                "A shield will protect you from enemies."
                )
        else:
            break
        
    print(
        "\n" + cloak + player1 + 
        " has chosen the honorable shield " + shield + " ."
        "\nBe warned...the honorable shield " + shield + 
        " can be used as a raft in dire circumstances."
        )

    print(
        "\n~~~~~~~~~~~~\___/,,,,,," 
        + cloak + player1 + shield + " shall begin the Epic Quest!"
        )

    while True:
        begin = input(
                "\nEnter the boat to sail the seas"
                " or burn the boat and remain in the artic land"
                " 'sail' or 'land' ?"
                )
        if begin not in ('sail', 'land'):
            print(
                "Your adventure awaits choose!"
                )
            time.sleep(1)
        else:
            break
    if 'sail' in begin:
        print(
            "\nSailing the seas \n"
            "\nSailing"
            "\nThe"
            "\nSeas"
            )
# The time module utilized to add effect, between strings for the user to read
        time.sleep(1.5)
        
        print(
            "\n~~~~~~~~~~~\__" + cloak + player1 + shield + "__/~~~~~~~~~~~\n"
            "\nThe winds are favorable. Pirate Crazy Ears is nearby."
            "\n~~~~<___>~~~~~~~~\__" + cloak + player1 + shield + "__/\n"
            )
            
        time.sleep(1.5)
        
        print(
            "\nCannons fire and you narrowly avoid the first cannonball!\n"
            )
            
        time.sleep(1.5)
        
        print(
            "\nCannons fire again and your boat is damaged."
            "\n~~~<___>*******~~~~___" + cloak + player1 + shield + "__/\n"
            )
            
        time.sleep(1.5)
         
        print(   
            "\nIt is Pirate Crazy Ears laughing at you!"
            "\n~~~<___>~~~~Ha~~~~Ha~~~~Ha~~~~"
                )
                
        time.sleep(1.5)
                
        while True:
            pir_pow = input(
                            "\nPirate Crazy Ears draws near."
                            "\nHe offers an alliance in exchange"
                            " for your cloak or to take you as a "
                            "prisoner of war and sell you at the next port."
                            "\nDire circumstances indeed, but the shield can"
                            " be used as a raft:"
                            "\n'ally' or 'pow' or 'raft'"
                            )
            if pir_pow not in ('ally', 'pow', 'raft'):
                time.sleep(1)
                print(
                    "\nPirate Crazy Ears does not take kindly to fools and "
                    "kills you."
                    "\nThrowing your body overboard and taking your cloak " + 
                    cloak + " and " + shield + " as treasure."
                    )
# The first of the 8 functions.  The user lost and can restart or end the game
# Calling this function in makes it very easy to maintain proper indentation-
# -and syntax.  
                cont_or_end()
        
            else:
                break    
            
        if 'ally' in pir_pow:
            print(
                "\nPirate Crazy Ears welcomes you to the crew!"
                "\n" + player1 + shield + " is now a pirate." 
                )
            time.sleep(2)
            print(
                "\nYears pass and you grow in wealth and reputation. "
                "\nPirate Crazy Ears has given you a ship and crew to command."
                "\nBoth of you rule the seven seas!"
                )
            time.sleep(2)
            while True:
                seven_seas = input(
                        "\nDo you continue to work for Pirate Crazy Ears?"
                        "\nOr do you want to pillage the seas on your own?:"
                        "\n 'work' or 'pillage'"
                                )
                if seven_seas not in ('work', 'pillage'):
                    print(
                        "\nAfter all this time being a pirate."
                        "\nYou are still a coward."
                        )
                        
                    co_ward() 
                                       
                else:
                    break
                    
            if 'work' in seven_seas:
                mighty()
                    
            if 'pillage' in seven_seas:
                time.sleep(2)
                print(
                        "\nPirate Crazy Ears mocks you one day."
                        "\n'I have this mighty cloak " + cloak + " I took "
                        "from a coward! Ha Hardy Har Ha'"
                        )
                time.sleep(2)
                print(
                    "\n" + player1 + shield + " immediately lights Pirate " 
                    "Crazy Ears on fire! \nYou are clever and remembered "
                    "the cloak is flammable!"
                    )
                time.sleep(1.5)
                print(
                    "\nMore years pass..."
                    )
                time.sleep(1)
                while True:
                    ruler = input(
                        "\nOne day a Leviathan interrupts your pillaging!"
                        "\nWage war on it or sail away from it: "
                        "\n'war' or 'flee'"
                                )
                    if ruler not in ('war', 'flee'):
                        co_ward()
                    else:
                        break
                            
            if 'war' in ruler:
                print(
                    "\nThe War begins!!!"
                    )
                time.sleep(1)
                print(
                    "\n|""_________________________________""|"
                    "\n|[<*>                          <*>|"
                    "\n\[vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv]/"
                    "\n    <___" + player1 + "___>        "
                    "\n[^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^]"  
                    )  
                time.sleep(1)
                print(
                        "\nUh Oh the Leviathan was not to be trifled with."
                        )
                print(
                    "\nCHOMP"
                    )
                time.sleep(1)
                print(
                    "\nCHOMP"
                    )
                time.sleep(1)
                print(
                "\nCHOMP"
                    )
                        
                time.sleep(1)
                print(
                    "\nThe Leviathian happily enjoyed the war."
                    "\n\nDeath by Leviathan for you, your crew, and treasures."
                        "\n|""_________________________________""|"
                        "\n|[<*>                          <*>|"
                        "\n\[===============================]/"
                        "\n[===============================]" 
                        )
            
                cont_or_end()
                    
            if 'flee' in ruler:
                print(
                    "\nYour crew loses trust in you for turning down a war."
                    )
                time.sleep(1)
                print(
                    "\nMUTINY!"
                    )
                time.sleep(1)
                print(
                    "\nTRAITOR!"
                    )
                time.sleep(1)
                print(
                    "\nCOWARD!"
                    )
                time.sleep(.5)
                print(
                    "\nYour crew hangs you until you are dead. Then throws "
                    "your cowardly corpse into the sea."
                    )
                co_ward()
                
        if 'pow' in pir_pow:
            print(
                "\nPirate Crazy Ears took your cloak " + cloak + " and " 
                "shield " + shield + " as treasure."
                "\nYet, he kept his word and sold you at the next port."  
                "\nLament for the lost cloak and shield." 
                "\nBroken and demoralized " + player1 + " works as a laborer."
                "\nDying of old age with bitter sadness."
                )
            
            cont_or_end()
            
        if 'raft' in pir_pow:
            time.sleep(2)
            print(
                "\nWith the sheild as a raft, your boat sinks and Pirate "
                "Crazy Ears draws near.  \nBUT a giant Leviathan emerges "
                "between you and the Pirate!\n"
                "\n~~~~~~~~~~~~~|""______________""|~~~~~~~~~~~~~~~~~~~~~~~~"
                "\n~~~<__>~~~~~ |[<*>       <*>|~~~~~~" + player1 + "~~~~~"
                "\n~~~~~~~~~~~~~~\[vvvvvvvvvvv]/~~~~~~" + shield + "~~~~~~"
                "\n~~~~~~~~~~~~~~~~[^^^^^^^^^]~~~~~~~~~~~~~~~~~~~~~~~~~~"
                )
            
            while True:
                spaghetti = input(
                            "\nPirate Crazy Ears flees from the Leviathan."
                            "\nWhile trying to paddle away, you find a pouch "
                            "of spaghetti in the shield. \nDo you eat the "
                            "spaghetti for energy or share with the sea "
                            "giant trying to eat you?!: 'energy' or 'share'"
                                )
                if spaghetti not in ('energy', 'share'):
                    print(
                        "\nTrifle with a Leviathan?! So STUPID!!"
                        "\n" + player1 + shield + " eaten by the Leviathan."
                        "\n|""_________________________________""|"
                        "\n|[<*>                          <*>|"
                        "\n\[vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv]/"
                        "\n    " + player1 + "        "
                        "\n[^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^]"    
                            )
                            
                    cont_or_end()
                
                else:
                    break
            if 'energy' in spaghetti:
                print(
                    "\nEating spaghetti in front of a Leviathan?! So STUPID!!"
                        "\n" + player1 + shield + " eaten by the Leviathan."
                        "\n|""_________________________________""|"
                        "\n|[<*>                          <*>|"
                        "\n\[vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv]/"
                        "\n    " + player1 + "        "
                        "\n[^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^]"    
                    )
                print(
                    "\nCHOMP"
                    ) 
                time.sleep(1)
                print(
                    "\nCHOMP" 
                    )
                time.sleep(1)
                print(
                    "\nChomp"
                    )
                time.sleep(1)
                print(
                    "\nThe Leviathian happily enjoyed you and your spaghetti."
                    "\nSTINGY JERK YOU WERE!  SHARE NEXT TIME!\n"
                        "\n|""_________________________________""|"
                        "\n|[<*>                          <*>|"
                        "\n\[===============================]/"
                        "\n[===============================]" 
                        )
            
                cont_or_end()
            
            if 'share' in spaghetti:
                print(
                    "\nWise move!  It is common knowledge that Leviathan's "
                    "enjoy spaghetti!  Who doesn't?!\n"
                    "\nThe Leviathan happily enjoys spaghetti with you."
                    "\n" + player1 + " has made a new friend."
                        "\n|""_________________________________""|"
                        "\n|[<*>                          <*>|"
                        "\n\[vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv]/"
                        "\n[^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^]" 
                        )
                        
                friend()

    if 'land' in begin:
        print(
            "\nThe ship is now in ashes " + player1 + shield + 
            " barely removed the flammable cloak " + cloak + " without" 
            " being burned."
            )
        print(
            "~~~~~~~~/::" + cloak + ":\,,,,,,,,," + player1 + shield + ""
            ) 
        while True:
            cold = input(
                        "\nUse shield for shelter, use shield as a boat, "
                        "or stare at the ashes with disdain?: "
                        "'shelter' or 'boat' or 'stare' "
                        ) 
            if cold not in ('shelter', 'boat', 'stare'):
                print(
                    "\n" + player1 + shield + "grows colder."
                    " Make a decision quickly."
                    )
                time.sleep(1)
            else:
                break
        if 'shelter' in cold:
            print(
                "\nFOOL! A shield is a shelter against pirates"
                " not for keeping warm in an artic land."
                "\n,,,,,,,,,,,,,,,,:::,,,,,,,::....." + player1 + 
                shield + "\n""\nIt is too cold to continue.\n"
                ",,,,,,,,,,,,,,,," + shield + ",,,,,,,,," + player1 + ""
                "\nSuch foolishness can only result in death"
                )

            shield_shelter()
            
        if 'boat' in cold:
            print(
                "\nA shield, 'can be used as a raft in dire circumstances' "
                "\n" + player1 + " has nothing to paddle the raft with."
                "\nThe raft washes back up on the artic shores repeatedly."
                "\nFatigued and cold " + player1 + " dies on the artic shores."
                )

            raft_boat()
    
        if 'stare' in cold:
            print(
                    "\nWhilst staring in disdain at the ashes..."
                    "\nApproaching footsteps"
                    "\nfrom behind"
                    "\nbefore you can turn"
                    )
            time.sleep(3)
            print(
                    "\nA penguin has happened upon you!"
                    )
            while True:
                penguin = input(
                            "\nThe penguin is now beside you."
                            "\nLet the penguin stare in disdain with you?"
                            "\nOr kill the penguin for standing nearby?: "
                            "\n'disdain' or 'kill'"
                            )
                if penguin not in ('disdain', 'kill'):
                    print(
                        "\n" + player1 + shield + "is indecisive."
                        "\nThe penguin laughs at you and kills you for food."
                        )
                    cont_or_end()
                    time.sleep(1)
                else:
                    break 
            
            if 'disdain' in penguin:
                print(
                    "\nThe penguin nudges " + player1 + shield + " waddling "
                    "into the approaching blizzard."
                    )
                while True:
                    blizzard = input(
                            "\nTo follow the penguin or remain with the ashes:"
                            "\n'follow' or 'ashes'"
                            )
                    if blizzard not in ('follow', 'ashes'):
                        print(
                        "\n" + player1 + shield + "is indecisive."
                        "\nThe approaching blizzard overpowers you"
                        " and you die."
                        )
                        co_ward()
                        time.sleep(1)
                    else:
                        break 
                        
                if 'follow' in blizzard:
                    print(
                        "\nThe penguin leads you deeper into the storm"
                        "\nAfter a grueling trek into the blizzard..."
                        )
                    time.sleep(3)
                    print(
                        "\nThe penguin has led you to a mountain shelter."
                        "\n.......\=========================================="
                        "\n........\========================================="
                        "\n.........\========================================"
                        "\n.........|________________________________________"
                        "\n..............." + player1 + shield + " ...|^|....."
                        )
                    
                    while True:
                        spaceship = input(
                            "\nThe penguin gives a head nod of respect and "
                            "returns to the blizzard. \nWhile resting in "
                            "the mountain, you find a spaceship. \nDo you"
                            " try to fly this spaceship: 'yes' or 'no' \n"
                                        )
                            
                        if spaceship not in ('yes', 'no'):
                            print(
                                "\n" + player1 + shield + "is indecisive."
                                )
                        
                            time.sleep(2)    
                            
                            print(
                                "\nThe spaceship activates into a hostile "
                                "alien robot and kills you!"
                                )
                            co_ward()
                        else:
                            break
                    if 'yes' in spaceship:
                        print(
                "\nA calculating warrior you have have become "
                + player1 + shield + " uses the spaceship to return home."
                "\nVictory is yours mighty warrior.  You are the winner!\n"
                "\nThe spaceship sets off for a far away galaxy\n"
                                )
                                
                        time.sleep(1.5)
                    
                        print(
                "\n * * * * * * * * * * * * * * * * * * * * |^|* * * *"
                "\n * * * * * * * * * * * * * |^| * * * * * *  * * * *"
                "\n * * * * * * * |^| * * * * * * * * * * * *  * * * *"
                "\n * |^| * * * * * * * * * * * * * * * * * *  * * * *"
                "\n * * * * * * * * * * * * * * * * * * * * *  * * * *"
                "\n * * * * * * * * * * * * * * * * * * * * *  * * * *"
                "\n * * * * * * * * * * * * * * * * * * * * *  * * * *"
                "\n * Produced by sweet dreams d(-__-)b * * *  * * * *"
                "\nPizza and Nap time, bye bye."
                                )
                                
                        victory()
                    
                    if 'no' in spaceship:
                        alien()
                
                if 'ashes' in blizzard:
                    print(
                        "\n" + player1 + shield + " really has poor social "
                        "skills."
                        "\nA cold wind passes by and the penguin is gone."  
                        )
                    
                    time.sleep(2)    
                    
                    print(
                        "\nThe approaching blizzard overpowers you"
                        " and you die."
                        )
                    
                    cont_or_end()
            
            if 'kill' in penguin:
                print(
                    "\nIt takes a big (WEAK) mighty (POOR) warrior to kill "
                    "a penguin."
                    )
                time.sleep(1)
                print(
                    "\nThe approaching blizzard overpowers you and you die."
                    )
                time.sleep(1)
                cont_or_end()
        
    return

start()
play_game()

