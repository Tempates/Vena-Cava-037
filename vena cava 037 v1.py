#imports
import time
import random
import math

#globals
global vena_cava
global hallway1
global liddle
global hallway2
global hasLighter
global hallway3
global hasBroom
global boysRoom
global janitors
global hallway4
global Detention
global Teachers
global homework
global question
global OsbornQuest
global SkeletonKey
global Juvenile
global hasPhone
global Exited
global FirstTime

FirstTime = bool(True)

pas1 = str(random.randint(0,9))
pas2 = str(random.randint(0,9)) 
pas3= str(random.randint(0,9))
pas4 = str(random.randint(0,9))
passcode = pas1+pas2+pas3+pas4

def Phone():
    if Exited == False:
        if liddle == True:
            print("Mr Liddle: Get off that phone!")
            time.sleep(1)
        else:
            if vena_cava == False:
                print("phone")
                print("--------------------------------------------------------")
                print("A - Call L. Cole")
                print("B - Look at timetable")
                print("C - Look at Photos")
                print("D - Look at Map")
                print("E - Enter Passcode...")
                print("--------------------------------------------------------")
                choice = input("").lower()
                if choice == "a":
                    onPhone = True
                    print("Ringing L.Cole...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("L.Cole: Hello?")
                    time.sleep(1)

                    while onPhone == True:
                        print("--------------------------------------------------------")
                        print("A - Ask him for hints")
                        print("B - Ask him what all the ending of the game are")
                        print("C - Ask him what the passcode is about")
                        print("D - Hang up")
                        print("--------------------------------------------------------")
                        choice = input("").lower()

                        if choice == "a":
                            print(name+": Hello, Can I get some hints for this game?")
                            time.sleep(1)
                            print("L. Cole: idk... can you???????????")
                            time.sleep(1)
                        elif choice == "b":
                            endingsQuery = True
                            print(name+": Hello, Can you tell me all the endings of this game?")
                            time.sleep(1)
                            print("L. Cole: Well, there are about 5 endings of this game, you should unlock them in the order I tell you")
                            time.sleep(3)
                            print("--------------------------------------------------------")
                            print("L. Cole: There is the NORMAL ending")
                            print("L. Cole: There is the JUVENILE ending")
                            print("L. Cole: There is the INSANITY ending")
                            print("L. Cole: There is PRESLEY'S ending")
                            print("L. Cole: The other ending I'm not allowed to tell you about")
                            print("--------------------------------------------------------")
                            time.sleep(5)
                            print()
                            while endingsQuery == True:
                                print("--------------------------------------------------------")
                                print("A - Tell me about the NORMAL ending")
                                print("B - Tell me about the JUVENILE ending")
                                print("C - Tell me about the INSANITY ending")
                                print("D - Tell me about PRESLEY'S ending")
                                print("E - Only five endings?")
                                print("--------------------------------------------------------")
                                choice = input("").lower()

                                if choice == "a":
                                    print("L. Cole: Well there isn't much to tell you about, just play through the game and you'll probably get it")
                                    time.sleep(5)
                                elif choice == "b":
                                    print("L. Cole: Juvenile prison is basically just a prison for kids, think about what you could get sent to juvenile prison for, and what character in this game would maybe try and send you there")
                                    time.sleep(8)
                                elif choice == "c":
                                    print("L. Cole: The INSANITY ending is a sub-ending of the juvenile ending, so if you know how to get the juvenile ending, which you should get before you try the insanity ending, you should be able to get the insanity ending by doing something new...")
                                    time.sleep(10)
                                elif choice == "e":
                                    print("L. Cole: Shut up")
                                    time.sleep(2)
                                    endingsQuery = False
                                elif choice == "d":
                                    print("L. Cole: Let's just say that Presley has been working on an interesting machine")
                                    time.sleep(5)
                        elif choice == "c":
                            print("L. Cole: I'm not allowed to tell you")
                            time.sleep(2)
                        elif choice == "d":
                            print("You hang up")
                            onPhone = False
                                
                elif choice == "b":
                    print("--------------------------------------------------------")
                    print("Monday - Computing, Computing, Computing, Lunch, Computng, Computing, Computing, Computing")
                    print("Tuesday - Computing, Computing, Computing, Lunch, Computng, Computing, Computing")
                    print("Wednesday - Computing, Computing, Computing, Lunch, Computng, Computing, Computing, Computing")
                    print("Thurday - Computing, Computing, Computing, Lunch, Computng, Computing, Computing")
                    print("Friday - Computing, Computing, Computing, Lunch, Computng, Computing, Computing")
                    print("--------------------------------------------------------")
                elif choice == "c":
                    print(str(name)+": Hey, there's a picture of me and Rehan Ali, things have been dull since he went missing")
                    time.sleep(3)
                elif choice == "d":
                    print("--------------------------------------------------------")
                    print("░Mr Liddle's░░░██████████░░░░░░░░░░░░░░░░░████████░░████████░░")
                    print("░░░░░██████░░░░█║║║║║║║║█░░░██████████░░░░█Teachs████Cooper█░░")
                    print("░░░░░█║║║║█░░░░█Nurse's █░░░█║║║║║║║║█░░░░█║║║║║║║──║║║║║║║█░░")
                    print("██░░░█║║║║█░░░░█║║║║║║║║█░░░█Boys WC║█░░░░█Lounge████Office█░█")
                    print("██░░░█║║║║█░░░░█║║║║║║║║█░░░█║║║║║║║║█░░░░█║║║║║║█░░█║║║║║║█░█")
                    print("███████││█████████││││█████████││││█████████│││███████████████")
                    print("██═══════════█═══════════█═════════════█═════════════════════█")
                    print("██═══════════█═══════════█═════════════█═════════════════════█")
                    print("██═Hallway 1═█═Hallway 2═█══Hallway 3══█══════Hallway 4══════█")
                    print("██═══════════█═══════════█═════════════█═════════════════════█")
                    print("██═══════════█═══════════█═════════════█═════════════════════█")
                    print("███████││███████════════███████││││█████████████│││││█████████")
                    print("██░░░█║║║║█░░░░█Vending █░░░█║║║║║║║║█░░░░█║║║║║║║║║║║║║║║█░░█")
                    print("██░░░█║║║║█░░░░██████████░░░█Girls WC█░░░░█║║║Detention║║║█░░█")
                    print("░░░░░██████░░░░░░░░░░░░░░░░░██████████░░░░█║║║║║║║║║║║║║║║█░░░")
                    print("░Janitors Closet░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████░░░")
                    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                    print("--------------------------------------------------------")

                elif choice == "e":
                    choice = input("Enter Passcode: ")
                    if choice == passcode:
                        global Abduction
                        Abduction = True
                        print("You enter the passcode...")
                        time.sleep(2)
                        print("..Your Phone shines green, you got it correct!")
                        time.sleep(2)
                        print("It did nothing")
                        
                    else:
                        print("You enter the passcode...")
                        time.sleep(2)
                        print("..Your Phone shines red, you got it wrong...")
            else:
                print(str(name)+": I shouldn't be on my phone right now, I need to get ethan to the nurse")
                time.sleep(1)
    else:
        if Abduction == True:
            # ABDUCTION ENDING
            print("You walk out of the school, somethings off...")
            time.sleep(3)
            print("You hear whirling in the distance, it's getting louder")
            time.sleep(3)
            print("You look up in the distance and see a helicopter Hovering over the school's car park")
            time.sleep(4)
            print("A familiar voice comes blaring out from the helicopter...")
            time.sleep(5)
            print("L. Cole: Cosignee "+name+"!")
            time.sleep(3)
            print("L. Cole: You have been located and are instructed to surrender")
            time.sleep(4)
            print("L. Cole: Remain in place and put your hands up")
            time.sleep(4)
            print("You grunt with frustration")
            time.sleep(3)
            print("L. Cole: Come on, "+name+".")
            time.sleep(3)
            print("L. Cole: It's like he told you, there's no escape for the students")
            time.sleep(4)
            print("You put your hands up, How could this have happened?")
            time.sleep(4)
            print("The helicopter lowers and you feel the breeze blowing your hair back")
            time.sleep(5)
            print("--------------------------------------------------------")
            print("What happened there? Who even is L. Cole? So many questions, such little answers!")
            print("You achieved the ABDUCTION ending!")
            print("")
            print("All Endings:")
            print("")
            print("Normal Ending")
            print("Juvenile Ending")
            print("Insanity Ending")
            print("Presley's Ending")
            print("[REDACTED] Ending")
            print("Abduction Ending")
            print("")
            print("Inventory: ", *inventory, sep=', ')
            print("--------------------------------------------------------")
            time.sleep(999)
            quit()
            
#start of game
name = input("What is your name? ")
while True:
    if FirstTime == True:
        #Variables
        vena_cava = bool(False)
        hasLighter = bool(False)
        hasBroom = bool(False)
        janitorMoney = bool(False)
        homework = bool(False)
        question = int(1)
        leosMoney = bool(False)
        OsbornQuest = bool(False)
        hasCoke = bool(False)
        SkeletonKey = bool(False)
        Juvenile = bool(False)
        hasPhone = bool(True)
        onPhone = bool(False)
        endingsQuery = bool(False)
        Exited = bool(False)
        Abduction = bool(False)
        PresleysMachine = bool(False)
        BrokenMachine = bool(False)

        #Areas
        liddle = bool(True)
        hallway1 = bool(False)
        hallway2 = bool(False)
        hallway3 = bool(False)
        hallway4 = bool(False)
        Nurse = bool(False)
        boysRoom = bool(False)
        janitors = bool(False)
        Detention = bool(False)
        Teachers = bool(False)


        global inventory
        inventory = []
        inventory.append("phone")

        print("You wake up in from a deep slumber, you are in class and you want to escape school")
        time.sleep(1)

        FirstTime = False

    #Runs in mr liddle's classroom
    while liddle == True:
        print("What do you do?")
        print("--------------------------------------------------------")
        print("Clock - look at the clock")
        print("Teacher - talk to the teacher")
        print("Ethan - Talk to ethan")
        print("Inventory - Check inventory")
        print("Phone - Look at your phone")
        print("--------------------------------------------------------")
        choice = input("").lower()
        if choice == "clock":
            print(name+": 11:99 AM, 3/5/23, wow, I wonder what the world will be like ten years from now")
            time.sleep(2)
        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif choice == "ethan":
            print("Ethan: Okay dude, what do you want now?")
            time.sleep(3)
            print("--------------------------------------------------------")
            print("A - I want to escape the school")
            print("B - *rips out vena cava*")
            print("C - Tell me all about the amazing game you played yesterday")
            print("D - You can't be pooin' yourself, Ethan")
            print("--------------------------------------------------------")
            choice = input("").lower()
            if choice == "a":
                print("Ethan: Okay, that might be a bit too far dude,you better lay off before I tell mr Liddle")
                Juvenile = True
                time.sleep(5)
            if choice == "b":
                if vena_cava == False:
                    print("Ethan: What the flip, that is mine, finders keepers! You are literally the filthy mcnasty")
                    print("You got: Ethan's Vena Cava!")
                    inventory.append("Ethan's Vena Cava")
                    vena_cava = True
                else:
                    print("Ethan: Broski, you already took that from me, what do you want now?")
                time.sleep(5)
            if choice == "c":
                print("Ethan: Deep Rock Galactic is a co-operative first-person shooter video game that is sure to get your adrenaline pumping. It is set in the future, where a group of dwarves has been hired to explore the depths of different planets. Players are tasked with mining resources and eliminating hostile alien creatures to keep themselves and their team safe. The game allows you to customize your character by selecting different classes, each with their own unique set of abilities and weapons")
                time.sleep(6)
            if choice == "d":
                print("Ethan: What...? Not very funny")
                time.sleep(1)

        elif choice == "teacher":
            print("Mr Liddle: Yes, "+str(name)+"?")
            time.sleep(1)

            print("--------------------------------------------------------")
            print("A - Uhhhh, mmmmm, idk")
            print("B - Can I go to the toilet?")
            print("C - Did ethan tell you about deep rock galactic?")
            if vena_cava == True:
                print("D - ETHAN DOES NOT HAVE A VENA CAVA I NEED TO GO TO THE NURSE WITH HIM!!!!")
            print("--------------------------------------------------------")
            
            choice = input("").lower()

            if choice == "a":
                print("Mr Liddle: Then don't waste my time")
            if choice == "b":
                print("Mr Liddle: Idk.. can you??????")
            if choice == "c":
                print("Mr Liddle: Deep Rock Galactic is a co-operative first-person shooter video game that is sure to get your adrenaline pumping. It is set in the future, where a group of dwarves has been hired to explore the depths of different planets. Players are tasked with mining resources and eliminating hostile alien creatures to keep themselves and their team safe. The game allows you to customize your character by selecting different classes, each with their own unique set of abilities and weapons")
            if vena_cava == True:
                if choice == "d":
                    print("Mr Liddle: Ok then, you may leave the classroom and take ethan here to the nurse, go!")
                    liddle = False
                    hallway1 = True

        elif choice == "phone":
            Phone()
            
    #Runs in Hallway 1
    while hallway1 == True:
        time.sleep(1)
        print("Area - Hallway 1")
        print("--------------------------------------------------------")
        print("North - Mr Liddles Classroom")
        print("East - Hallway 2")
        print("South - Janitors Closet")
        print("West - School Exit")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "north":
            print(str(name)+": I don't want to go in there again")
            if vena_cava == True:
                print(str(name)+": I probably shouldn't go anywhere except the nurse, this could be my key to escape")
        if choice == "west":
            if SkeletonKey == False:
                print(str(name)+": It's locked, I need a key to escape")
                time.sleep(1)
            else:
                Exited = True
                Phone()
                    
                if Juvenile == False and hasLighter == False:
                    # NORMAL ENDING #
                    time.sleep(1)
                    print("You open up the pearly gates and the sun is shining on your face")
                    time.sleep(3)
                    print("You walk out the school with pride, then go home to play some Taran Fighting Simulator")
                    time.sleep(4)
                    print("--------------------------------------------------------")
                    print("You successfully escaped the school!")
                    print("You achieved: The NORMAL Ending")
                    print("")
                    print("All Endings:")
                    print("")
                    print("Normal Ending")
                    print("Juvenile Ending")
                    print("Insanity Ending")
                    print("Presley's Ending")
                    print("[REDACTED] Ending")
                    print("✌♌♎◆♍⧫♓□■ Ending")
                    print("")
                    print("Inventory: ", *inventory, sep=', ')
                    print("--------------------------------------------------------")
                    print("Replay?")
                    print("--------------------------------------------------------")
                    print("A - Yes")
                    print("B - No")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        print("Replaying...")
                        time.sleep(2)
                        hallway1 = False
                        FirstTime = True
                    else:
                        hallway1 = False
                        break
                        
                elif Juvenile == True and hasLighter == False:
                    # JUVENILE ENDING #
                    time.sleep(1)
                    print("You open up the pearly gates and the sun is shining on your face")
                    time.sleep(3)
                    print("You walk out the school with pride, then go home to play some Taran Fighting Simulator")
                    time.sleep(4)
                    print("But wait...")
                    time.sleep(2)
                    print(".. You hear a voice behind you")
                    time.sleep(3)
                    print("You turn around and..")
                    time.sleep(2)
                    print("You see Ethan McLean, Mr Cooper, Mrs McCloy, Mr Stevenson and Mr Liddle!")
                    time.sleep(4)
                    print("Ethan: I told you to lay off")
                    time.sleep(2)
                    print("You try to run away but then you get tased by Mr Stevenson")
                    time.sleep(3)
                    print("Mr Stevenson: You're going to juvenile prison for a long long time")
                    time.sleep(4)
                    print("--------------------------------------------------------")
                    print("Uh Oh! Ethan McLean caught you escaping school, he did warn you to lay off, bad idea telling him you wanted to escape school")
                    print("You achieved: The JUVENILE Ending")
                    print("")
                    print("All Endings:")
                    print("")
                    print("Normal Ending")
                    print("Juvenile Ending")
                    print("Insanity Ending")
                    print("Presley's Ending")
                    print("[REDACTED] Ending")
                    print("✌♌♎◆♍⧫♓□■ Ending")
                    print("")
                    print("Inventory: ",*inventory, sep=', ')
                    print("--------------------------------------------------------")
                    print("Replay?")
                    print("--------------------------------------------------------")
                    print("A - Yes")
                    print("B - No")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        print("Replaying...")
                        time.sleep(2)
                        hallway1 = False
                        FirstTime = True
                    else:
                        hallway1 = False
                        break
                elif Juvenile == True and hasLighter == True:
                    # INSANITY ENDING #
                    time.sleep(1)
                    print("You Open up the pearly gates and the sun is shining on your face")
                    time.sleep(3)
                    print("You walk out the school with pride, then go home to play some Taran Fighting Simulator")
                    time.sleep(4)
                    print("But wait...")
                    time.sleep(2)
                    print(".. You hear a voice behind you")
                    time.sleep(3)
                    print("You turn around and..")
                    time.sleep(2)
                    print("You see Ethan Mclean, Mr Cooper, Mrs McCloy, Mr Stevenson and Mr Liddle!")
                    time.sleep(4)
                    print("Ethan: I told you to lay o-")
                    time.sleep(2)
                    print("Ethan gets shot in the side of his chest!")
                    time.sleep(2)
                    print("Mr Stevenson, Mr Liddle, Mrs McCloy and Mr Cooper get gunned down!")
                    time.sleep(4)
                    print("Before you can get a look at who the shooter was, you get shot yourself!")
                    inventory.append("Shot lighter")
                    inventory.remove("Lighter")
                    time.sleep(4)
                    print("You're on the floor and your vision blurs")
                    time.sleep(3)
                    print("A familiar face walks up to you.")
                    time.sleep(2)
                    print("...")
                    time.sleep(2)
                    print("Daniel: Have I ever told you the definition of insanity?")
                    time.sleep(4)
                    print("Your eyes begin to shut.")
                    time.sleep(4)
                    print("You quickly get off the floor and you suddenly realise that you are unscaved")
                    time.sleep(4)
                    print("You take the lighter out of your pocket...")
                    time.sleep(3)
                    print("... and you realise there is a bullet wedged inside it!")
                    time.sleep(3)
                    print("Daniel is nowhere to be seen, so you walk home, and play Taran Fighting Simulator")
                    time.sleep(4)
                    print("--------------------------------------------------------")
                    print("That was crazy wasn't it! Daniel Fyfe to the rescue! Ethan McLean is surely the biggest threat of this school... Right?")
                    print("You achieved: The INSANITY Ending")
                    print("")
                    print("All Endings:")
                    print("")
                    print("Normal Ending")
                    print("Juvenile Ending")
                    print("Insanity Ending")
                    print("Presley's Ending")
                    print("[REDACTED] Ending")
                    print("✌♌♎◆♍⧫♓□■ Ending")
                    print("")
                    print("Inventory: ",*inventory, sep=', ')
                    print("--------------------------------------------------------")
                    print("Replay?")
                    print("--------------------------------------------------------")
                    print("A - Yes")
                    print("B - No")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        print("Replaying...")
                        time.sleep(2)
                        hallway1 = False
                        FirstTime = True
                    else:
                        hallway1 = False
                        break

                elif Juvenile == False and hasLighter == True:
                    # NORMAL ENDING #
                    time.sleep(1)
                    print("You open up the pearly gates and the sun is shining on your face")
                    time.sleep(3)
                    print("You walk out the school with pride, then go home to play some Taran Fighting Simulator")
                    time.sleep(4)
                    print("--------------------------------------------------------")
                    print("You successfully escaped the school!")
                    print("You achieved: The NORMAL Ending")
                    print("")
                    print("All Endings:")
                    print("")
                    print("Normal Ending")
                    print("Juvenile Ending")
                    print("Insanity Ending")
                    print("Presley's Ending")
                    print("[REDACTED] Ending")
                    print("✌♌♎◆♍⧫♓□■ Ending")
                    print("")
                    print("Inventory: ",*inventory, sep=', ')
                    print("--------------------------------------------------------")
                    print("Replay?")
                    print("--------------------------------------------------------")
                    print("A - Yes")
                    print("B - No")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        print("Replaying...")
                        time.sleep(2)
                        hallway1 = False
                        FirstTime = True
                    else:
                        hallway1 = False
                        break
                
        if choice == "south":
            if vena_cava == True:
                print(str(name)+": I probably shouldn't go anywhere except the nurse, this could be my key to escape")
            else:
                hallway1 = False
                janitors = True
        if choice == "east":
            hallway1 = False
            hallway2 = True
        if choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        if hasPhone == True:
            if choice == "phone":
                Phone()

    #Runs in Hallway 2
    while hallway2 == True:
        time.sleep(1)
        print("Area - Hallway 2")
        print("--------------------------------------------------------")
        print("North - Nurses office")
        print("East - Hallway 3")
        print("South - Vending Machine")
        print("West - Hallway 1")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "north":
            hallway2 = False
            Nurse = True
        elif choice == "east":
            if vena_cava == False:
                hallway2 = False
                hallway3 = True
            else:
                print(str(name)+": I probably shouldn't go anywhere except the nurse, this could be my key to escape")
        elif choice == "south":
            if vena_cava == False:
                print("There is cokes in the vending machine")
                time.sleep(1)
                print("'Cokes for £1.00 each'")
                if janitorMoney == True and leosMoney == True and hasCoke == False:
                    time.sleep(1)
                    print("--------------------------------------------------------")
                    print("A - Purchase a coke")
                    print("B - Don't buy a coke")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        inventory.append("Coke")
                        inventory.remove("50p")
                        inventory.remove("50p")
                        print("You got Coke for £1.00")
                        hasCoke = True
                        time.sleep(1)
                else:
                    time.sleep(1)
                    print("--------------------------------------------------------")
                    print("A - Purchase a coke")
                    print("B - Don't buy a coke")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        print(str(name)+": I don't have enough money")
                        time.sleep(1)
                    elif choice == "b":
                        print("You leave")
                        time.sleep(1)
            else:
                print(str(name)+": I probably shouldn't go anywhere except the nurse, this could be my key to escape")
        elif choice == "west":
            if vena_cava == False:
                hallway2 = False
                hallway1 = True
            else:
                print(str(name)+": I probably shouldn't go anywhere except the nurse, this could be my key to escape")
        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif hasPhone == True:
            if choice == "phone":
                Phone()

    #Runs in Nurse's office
    while Nurse == True:
        time.sleep(1)
        print("Area - Nurses Office")
        print("--------------------------------------------------------")
        print("A - Talk to Andrew")
        print("B - Talk to Daniel")
        print("C - Talk to nurse")
        print("South - Hallway 2")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "south":
            if vena_cava == True:
                print("I cant go back now, I need to save ethan, it will be my only chance to get out the school")
            else:
                Nurse = False
                hallway2 = True
        elif choice == "a":
            print("Andrew: Play the Farm Diner on scratch! Farm diner 2 releasing on the 11/5/23 (not confirmed)")
        elif choice == "b":
            if vena_cava == True:
                print("Daniel: I saw you with ethan over there, I was going to rip out his vena cava but you already did...")
                time.sleep(3)
                print(str(name)+": Good going lad, ill talk to you later, I need to sort out this ethan situation")
                time.sleep(2)
            else:
                print("Daniel: Have I ever told you the definition of insanity")
                time.sleep(1)
                print("--------------------------------------------------------")
                print("A - No")
                print("B - I don't care")
                print("C - ...")
                print("--------------------------------------------------------")
                choice = input("").lower()
                
                if choice == "a":
                    print("Daniel: Insanity is doing the exact... same thing... over and over again expecting... things to change... That. Is. Crazy. The first time somebody told me that, I dunno, I thought they were kidding me on, so, I shot him. The thing is... He was right. And then I started seeing, everywhere I looked, everywhere I looked all these absolute NPCs, everywhere I looked, doing the exact same thing... over and over and over and over again thinking 'this time is gonna be different' no, no, no please... This time is gonna be different!")
                    time.sleep(5)
                elif choice == "b":
                    if hasLighter == False:
                        print("*Daniel steals your phone* I like this phone, this is a nice phone, this phone looks very expensive, that's good because I like expensive things, *puts lighter in your pocket*")
                        time.sleep(4)
                        inventory.append("Lighter")
                        hasLighter = True
                        inventory.remove("phone")
                        hasPhone = False
                    else:
                        print("What is it now? You want your phone back? Thats not gonna happen, that things gonna get you killed, or worse. Always remember: There's no escape for the students")
                        hasPhone = False
                        time.sleep(4)
                elif choice == "c":
                    print("I am sorry, I don't like the way... you are looking at me! Okay? Do you have a problem in your head? Do you think im kidding you? Do you think that I am lying? SCREW YOU!")
                    time.sleep(4)
                        
        elif choice == "c":
            if vena_cava == True:
                print("Nurse: Hello it's me, the nurse!")
                time.sleep(1)
                print(str(name)+": This boy is missing the largest vein in his body! you must help!")
                time.sleep(2)
                print("Nurse: Okay, we must get some ice on this boy immedietly, I will take him away!")
                inventory.remove("Ethan's Vena Cava")
                vena_cava = False
                time.sleep(3)
            else:
                print("Nurse: Just a second, I'm still working on ethan")
                time.sleep(2)

        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)

        elif hasPhone == True:
            if choice == "phone":
                Phone()

    #Runs in hallway 3
    while hallway3 == True:
        time.sleep(1)
        print("Area - Hallway 3")
        print("--------------------------------------------------------")
        print("North - Boys Bathroom")
        print("East - Hallway 4")
        print("South - Girls Bathroom")
        print("West - Hallway 2")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "north":
            hallway3 = False
            boysRoom = True
        elif choice == "east":
            hallway3 = False
            hallway4 = True
        elif choice == "south":
            if SkeletonKey == False:
                print("It's locked")
            else:
                # MCINTYRE'S ENDING #

                print(str(name)+": Wait a minute, I've got a skeleton key, so do you think I'll be able to enter?")
                time.sleep(3)
                print("To your surprise, it works! you are greeted with a dark staircase going down, you decide to go down")
                time.sleep(4)
                print("You're at the end of the staircase and a dark basement is presented to you")
                time.sleep(4)
                print("You find the light switch")
                time.sleep(2)
                print("And the lights closest to you go on with a boom, then the next light, then the next, until the whole hallway is illuminated")
                time.sleep(6)
                print("Incubators on the walls, there are people in them?!")
                time.sleep(3)
                print("They have labels.")
                time.sleep(2)
                print("'Kerr Flaherty'")
                time.sleep(1)
                print("'Rehan Ali'")
                time.sleep(1)
                print("'Cameron Hamilton'")
                time.sleep(1)
                print("'Ruairaidh Doherty'")
                time.sleep(1)
                print("'Angus Rizzburt'")
                time.sleep(1)
                print(passcode)
                time.sleep(2)
                print("And that's only a few of them..")
                time.sleep(3)
                print("Before you can even process this whole thing, you hear footsteps from behind you...")
                time.sleep(5)
                print("...")
                time.sleep(2)
                print("Mr McIntyre: You're next...")
                time.sleep(5)

                print("--------------------------------------------------------")
                print("Who would have guessed, Mr McIntyre has been participating in some devious shenanigans. Will the mystery of The Cavacademy ever be solved?")
                print("You achieved: MCINTYRE'S Ending")
                print("")
                print("All Endings:")
                print("")
                print("Normal Ending")
                print("Juvenile Ending")
                print("Insanity Ending")
                print("Presley's Ending")
                print("McIntyre's Ending")
                print("✌♌♎◆♍⧫♓□■ Ending")
                print("")
                print("Inventory: ",*inventory, sep=', ')
                print("--------------------------------------------------------")
                print("Replay?")
                print("--------------------------------------------------------")
                print("A - Yes")
                print("B - No")
                print("--------------------------------------------------------")
                choice = input("").lower()
                if choice == "a":
                    print("Replaying...")
                    time.sleep(2)
                    hallway3 = False
                    FirstTime = True
                else:
                    hallway3 = False
                    break
                
        elif choice == "west":
            hallway3 = False
            hallway2 = True
        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif hasPhone == True:
            if choice == "phone":
                Phone()

    #runs in the boys room
    while boysRoom == True:
        time.sleep(1)
        print("Area - Boys Room")
        print("--------------------------------------------------------")
        print("A - Knock on the cubicle")
        if hasBroom == False:
            print("B - Take the broomstick which is under the sink")
        print("South - Hallway 3")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "a":
            print("You knock on the cubicle...")
            time.sleep(1)
            print("???: Sorry, I'll be just a second! I'm recording a music monday!")
            time.sleep(3)
        elif choice == "b":
            if hasBroom == False:
                print("You got the broomstick!")
                inventory.append("Broomstick")
                time.sleep(2)
                hasBroom = True
        elif choice == "south":
            boysRoom = False
            hallway3 = True
        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif hasPhone == True:
            if choice == "phone":
                Phone()
    #Runs in Janitor's Closet
    while janitors == True:
        time.sleep(1)
        if hasBroom == False:
            print("Area - Janitor's Closet")
            print("--------------------------------------------------------")
            print("A - Talk to Presley")
            print("North - Hallway 1")
            print("Inventory - Check inventory")
            if hasPhone == True:
                print("Phone - Check Phone")
            print("--------------------------------------------------------")
            choice = input("").lower()
            if choice == "a":
                print("Presley: My Guy, I'm sorry but you have to leave here")
                janitors = False
                hallway1 = True
            elif choice == "north":
                janitors = False
                hallway1 = True
            elif choice == "inventory":
                print(*inventory, sep=', ')
                time.sleep(3)
            elif hasPhone == True:
                if choice == "phone":
                    Phone()
        else:
            print("Area - Janitor's Closet")
            print("--------------------------------------------------------")
            print("A - Talk to Presley")
            print("North - Hallway 1")
            print("Inventory - Check inventory")
            if hasPhone == True:
                print("Phone - Check Phone")
            print("--------------------------------------------------------")
            choice = input("").lower()
            if choice == "a":
                if janitorMoney == False:
                    print("Presley: My Guy, I'm sorry but you have to leave here")
                    time.sleep(1.5)
                    print(str(name)+": I think I have your broomstick")
                    time.sleep(1)
                    print("Presley: Woohoo! My guy thank you for bringing this to me, I will reward you with 50p")
                    inventory.append("50p")
                    inventory.remove("Broomstick")
                    print("You got 50p!")
                    time.sleep(3)
                    janitorMoney = True
                else:
                    print("Presley: Thank you for returning my broomstick, you are welcome here anytime")
                    time.sleep(1)
                    print("--------------------------------------------------------")
                    print("A - Hey presley, do you have any kids?")
                    print("B - Tell me an epic fact about you.")
                    if BrokenMachine == False:
                        print("C - Can I get another 50p?")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    
                    if choice == "a":
                        print("Presley: Yes, I have a son, his name is Duane, we always say that if there is ever an apocalypse, then we will hideout in the school.")
                        time.sleep(1)
                    elif BrokenMachine == False:
                        if choice == "c":
                            print("Presley: I would if I could, but all my savings are going into this dusty old machine, do you want to test it out?")
                            time.sleep(3)
                            PresleysMachine = True
                            while PresleysMachine == True:
                                print("--------------------------------------------------------")
                                print("A - Yes")
                                print("B - No")
                                print("--------------------------------------------------------")
                                choice = input("").lower()
                                if choice == "a":
                                    print("You walk to the corner of the closet and you pick up the dusty helmet")
                                    time.sleep(2)
                                    print("You blow off the dust and stick it on your head")
                                    time.sleep(2)
                                    print("It's like a VR headset! The visuals open with the words 'Presley Inc.' and as the branding fades away, it asks you for a date")
                                    time.sleep(3)
                                    print("--------------------------------------------------------")
                                    Day = input("Enter Day: ")
                                    Month = input("Enter Month: ")
                                    Year = input("Enter Year (must be full year e.g: 2001): ")
                                    print("--------------------------------------------------------")
                                    Date = str(Day)+str(Month)+str(Year)
                                    if Date == "352033":
                                        PresleysMachine = False
                                        #MY GUY ENDING
                                        print("The machine starts to rumble, and you feel the ground beneath you fade away")
                                        time.sleep(4)
                                        print("The screen on the machine turns white, and you wake up on the ground")
                                        time.sleep(4)
                                        print("You take off the helmet, and you're in the janitors closet, there's empty tins of soup all over the floor, what happened here?")
                                        time.sleep(5)
                                        print("you exit the janitors closet and you see that the whole school is in ruin, there are fungal spores growing all over the walls, and the sky is green?")
                                        time.sleep(6)
                                        print("You are walking around and you hear a something burst open the door to exit the school")
                                        time.sleep(5)
                                        print("You hide in Mr Liddle's classroom, and you can hear a voice you know speaking as he walks through the hallways")
                                        time.sleep(6)
                                        print("Presley: This is where I lived with Duane before he died...")
                                        time.sleep(3)
                                        print(name+": Presley?")
                                        time.sleep(2)
                                        print("Presley: Who are you???")
                                        time.sleep(2)
                                        print(name+": Presley, it's me, "+name+", you know me!")
                                        time.sleep(3)
                                        print("Presley: W-Wait a minute, I know.. who you are..")
                                        time.sleep(3)
                                        print("Presley: I always wondered where you went off to with that machine of mine")
                                        time.sleep(4)
                                        print(name+": What is even going on, what does this machine even d-")
                                        time.sleep(4)
                                        print("A plant tangles your feet and drags you into a fungus, the fungus is devouring you, but you grab the machine")
                                        time.sleep(6)
                                        print("The you stick the machine on, and press the red button at the side of it")
                                        time.sleep(5)
                                        print("The screen turns white, and your reality starts to fade.")
                                        time.sleep(3)
                                        print("...")
                                        time.sleep(2)
                                        print("You wake up outside the school gates with a helmet on, and you take it off")
                                        time.sleep(3)
                                        print("The school seems empty, you look at your watch and it's sunday!")
                                        time.sleep(3)
                                        print("You walk home to play Taran's fighting simulator and act like nothing happened")
                                        inventory.append("Presley's Time Machine")
                                        time.sleep(4)
                                        print("--------------------------------------------------------")
                                        print("What happened there? What happened to the school, was that a time machine? Who cares you escaped school, and that's all that matters")
                                        print("You achieved: PRESLEY'S Ending")
                                        print("")
                                        print("All Endings:")
                                        print("")
                                        print("Normal Ending")
                                        print("Juvenile Ending")
                                        print("Insanity Ending")
                                        print("Presley's Ending")
                                        print("[REDACTED] Ending")
                                        print("✌♌♎◆♍⧫♓□■ Ending")
                                        print("")
                                        print("Inventory: ",*inventory, sep=', ')
                                        print("--------------------------------------------------------")
                                        print("Replay?")
                                        print("--------------------------------------------------------")
                                        print("A - Yes")
                                        print("B - No")
                                        print("--------------------------------------------------------")
                                        choice = input("").lower()
                                        if choice == "a":
                                            print("Replaying...")
                                            time.sleep(2)
                                            janitors = False
                                            FirstTime = True
                                        else:
                                            janitors = False
                                            break
                                    else:
                                        print("The machine starts to break and the screen displays the words: 'INVALID DATE'")
                                        time.sleep(2)
                                        print("Presley: My machine must be broken, hopefully one day it'll work...")
                                        time.sleep(2)
                                        PresleysMachine = False
                                        BrokenMachine = True
                                elif choice == "b":
                                    time.sleep(1)
                                    print("Ok")
                                    time.sleep(1)
                                    PresleysMachine = False
                    elif choice == "b":   
                        print("Presley: Did you know that I am a grandmaster in akido?")
                        time.sleep(1)
                        
            elif choice == "north":
                janitors = False
                hallway1 = True
            elif choice == "inventory":
                print(*inventory, sep=', ')
                time.sleep(3)
            elif hasPhone == True:
                if choice == "phone":
                    Phone()

    #Runs in hallway 4
    while hallway4 == True:
        time.sleep(1)
        print("Area - Hallway 4")
        print("--------------------------------------------------------")
        print("North - Teacher's Lounge")
        print("East - Entrance")
        print("South - Detention")
        print("West - Hallway 3")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "north":
            hallway4 = False
            Teachers = True
        elif choice == "east":
            print("its locked from the inside, the only way to open it is from the outside")
        elif choice == "south":
            hallway4 = False
            Detention = True
        elif choice == "west":
            hallway4 = False
            hallway3 = True
        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif hasPhone == True:
            if choice == "phone":
                Phone()

    #Runs in detention
    while Detention == True:
        time.sleep(1)
        print("Area - Detention")
        print("--------------------------------------------------------")
        print("A - Talk to Mr Stevenson")
        print("B - Talk to Scott Harding")
        print("C - Talk to Leo Tartaglia")
        print("North - Hallway 4")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "a":
            print("Mr Stevenson: You can't be in here, get out!")
            Detention = False
            hallway4 = True
        elif choice == "b":
            print("--------------------------------------------------------")
            print("A - Why are you in detention?")
            print("B - When is your dance battle with kate bunten")
            print("--------------------------------------------------------")
            choice = input("").lower()

            if choice == "a":
                time.sleep(1)
                print("Scott: NEVER threaten Scott Harding with a good time..")
            elif choice == "b":
                time.sleep(1)
                print("Scott: 11/5/2023")

        elif choice == "c":
            if leosMoney == False:
                print("Hello I am leo tartaglia, can you help me with my homework?")
                time.sleep(1)
                print("--------------------------------------------------------")
                print("A - Yes")
                print("B - I dont help catfishers")
                print("--------------------------------------------------------")
                choice = input("").lower()

                if choice == "b":
                    time.sleep(1)
                    print("Leo T: I guess I'll get scott harding to help me, at least he can make me laugh and giggle")
                elif choice == "a":
                    homework = True
                    while homework == True:
                        while question == 1:
                            time.sleep(1)
                            print("Leo: Okay, question 1 is: 'What is the biggest vein in the body?'")
                            time.sleep(1)
                            print("--------------------------------------------------------")
                            print("A - Aorta")
                            print("B - Pulmonary Vein")
                            print("C - Vena Cava")
                            print("D - Leo Cole")
                            print("--------------------------------------------------------")
                            choice = input("").lower()

                            if choice == "c":
                                print("Leo T: Correct!")
                                question = question +1
                            else:
                                print("Wrong!")

                        while question == 2:
                            time.sleep(1)
                            print("Leo: (x + 4)(x - 6) the answer has no spaces (squared written as ^2)")
                            choice = input("")

                            if choice == "x^2-2x-24":
                                print("Leo T: Correct!")
                                question = question +1
                            else:
                                print("Wrong!")

                        while question == 3:
                            time.sleep(1)
                            print("Leo: Why didn't the skeleton go to the prom?")
                            time.sleep(1)
                            print("--------------------------------------------------------")
                            print("A - He had no body to go with")
                            print("B - He is fat, ugly and no one loves him")
                            print("C - Leo Cole")
                            print("--------------------------------------------------------")
                            choice = input("").lower()

                            if choice == "b":
                                time.sleep(1)
                                print("Correct! That's all of the questions, thank you for helping me, dont ask me why I already know the answers")
                                time.sleep(1)
                                print("As a reward, I will give you 50p!")
                                inventory.append("50p")
                                time.sleep(1)
                                question = 0
                                homework = False
                                leosMoney = True
                            else:
                                print("Wrong!")
                                
            else:
                print("Leo: Back for seconds? wowee you must be desperate for money!")

        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif choice == "north":
            Detention = False
            hallway4 = True
        elif hasPhone == True:
            if choice == "phone":
                Phone()

            
    # Runs in Teachers Lounge
    while Teachers == True:
        time.sleep(1)
        print("Area - Teacher's Lounge")
        print("--------------------------------------------------------")
        print("A - Talk to Mrs McCloy")
        print("B - Talk to Mr Osborn")
        print("C - Look out the window")
        print("South - Hallway 4")
        print("Inventory - Check inventory")
        if hasPhone == True:
            print("Phone - Check Phone")
        print("--------------------------------------------------------")
        choice = input("").lower()

        if choice == "a":
            print("Mrs McCloy: Why are you here?")
            time.sleep(1)
            print("--------------------------------------------------------")
            print("A - uhhhh mmm idk...")
            print("B - Leo Cole")
            print("C - Why are YOU here?")
            print("D - Can I get in mr coopers office?")
            print("--------------------------------------------------------")
            choice = input("").lower()

            if choice == "a":
                print("Mrs McCloy: Not good enough, get out.")
                time.sleep(1)
                Teachers = False
                hallway4 = True
            elif choice == "b":
                print("Mrs McCloy: That boy is a champion, now get out.")
                time.sleep(1)
                Teachers = False
                hallway4 = True
            elif choice == "c":
                print("Mrs McCloy: Fair enough, you may stay here")
                time.sleep(1)
            elif choice == "d":
                print("Mrs McCloy: Why?")
                time.sleep(1)
                print("--------------------------------------------------------")
                print("A - im not too sure")
                print("B - I have a doctors appointment")
                print("--------------------------------------------------------")
                choice = input("").lower()

                if choice == "a":
                    print("Well get out then")
                    Teachers = False
                    hallway4 = True
                elif choice == "b":
                    print("Then why are you in the teachers lounge and not the doctors? get out")
                    time.sleep(1)
                    Teachers = False
                    hallway4 = True

        elif choice == "b":
            if OsbornQuest == False:
                print("Mr Osborn: What are you doing here?")
                time.sleep(1)
                print("--------------------------------------------------------")
                print("A - Can I get into mr coopers office")
                print("B - im not sure")
                print("C - What are YOU doing here")
                print("--------------------------------------------------------")
                choice = input("").lower()

                if choice == "a":
                    print("Mr Osborn: Why?")
                    time.sleep(1)
                    print("--------------------------------------------------------")
                    print("A - Cause I'm cool")
                    print("B - I have a doctors appointment")
                    print("--------------------------------------------------------")
                    choice = input("").lower()

                    if choice == "a":
                        print("Mr Osborn: To be fair, you are quite cool, but I'm not just going to let you in, I need something for doing this for you, how about you buy me a can of coke from the vending machine and come back here when you have it. Deal?")
                        time.sleep(7)
                        print(str(name)+": Deal.")
                        OsbornQuest = True
                        time.sleep(1)
                        print("Mr Osborn: Now skedaddle.")
                        time.sleep(1)
                        Teachers = False
                        hallway4 = True
                    elif choice == "b":
                        print("Mr Osborn: Then go to the doctors not the teachers lounge")
                        time.sleep(1)
                        Teachers = False
                        hallway4 = True

                elif choice == "b":
                    print("Get out then")
                    Teachers = False
                    hallway4 = True
                elif choice == "c":
                    print("Mr Osborn: Okay then wise guy, stay here")
                    time.sleep(1)
            else:
                if SkeletonKey == False:
                    print("Mr Osborn: Do you have my coke?")
                    time.sleep(1)
                    print("--------------------------------------------------------")
                    print("A - Not yet")
                    if hasCoke == True:
                        print("B - Yes")
                    print("--------------------------------------------------------")
                    choice = input("").lower()
                    if choice == "a":
                        print("Mr Osborn: Then go get it then")
                        Teachers = False
                        hallway4 = True
                    if hasCoke == True:
                        if choice == "b":
                            print("Mr Osborn: Go right ahead then.")
                            inventory.remove("Coke")

                            #Start of the end
                            time.sleep(3)
                            print("The door the mr coopers office opens, this is it, you can't mess up now")
                            time.sleep(7)
                            print("You creep in his room, and osborn closes it shut, you spot a skeleton key on a desk")
                            time.sleep(7)
                            print("Mr Cooper is playing the hit game 'Taran's Fighting Simulator' and he can't hear you and his computer is facing the opposite way of the wall")
                            time.sleep(9)
                            print("You grab the key, turn around and as you're walking out...")
                            inventory.append("Skeleton Key")
                            SkeletonKey = True
                            time.sleep(6)
                            print("... you hear mr cooper speaking")
                            time.sleep(4)
                            print("Mr Cooper: Hey!")
                            time.sleep(3)
                            print("You slowly turn around..")
                            time.sleep(4)
                            print("..Mr Cooper: Get that jacket off!")
                            time.sleep(4)
                            print(str(name)+": Right, yeah, sorry sir.")
                            time.sleep(3)
                            print("You run out the room and back in the hallway")

                            Teachers = False
                            hallway4 = True
                else:
                    print("Mr Osborn: You think I'm gonna let you in again? The coke doesn't taste THAT good, "+name)
                    time.sleep(2)
                            
        elif choice == "c":
            print("You look out the window, and you see Mr McIntyre dragging a human shaped bag into a vault, strange.")
            time.sleep(5)
        elif choice == "south":
            Teachers = False
            hallway4 = True
        elif choice == "inventory":
            print(*inventory, sep=', ')
            time.sleep(3)
        elif hasPhone == True:
            if choice == "phone":
                Phone()


