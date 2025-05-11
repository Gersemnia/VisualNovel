# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Detective = Character("Detective", color="#FFFFFF")
define Sailor = Character("Sailor", color="#33DAFF")


# The game starts here.

label start:
    "..."
    play music "audio/bgm_ocean.mp3" fadein 1.0
    "June 14th, 2004."

    "I couldn't see anything beyond the shoreline, but with every second passing..."

    "I felt like I was ever closer to touching the horizon."

    Sailor "We're almost there, mate."

    Detective "Good, sitting still gets exhausting."

    Sailor "Hehe."

    "I got up and walked next to the sailor."

    "The sky started to look almost purple, and lights were shining in the distance."

    "It looked almost like a painting. It was beautiful."

    Sailor "Mate, if you don't mind me asking..."

    Detective "..?"

    Sailor "Aren't you the one who cleared that one guy in '92?"

    Detective "..."

    Detective "Yeah."

    Sailor "Wow. Congrats, mate."

    Detective "Thanks."

    Sailor "Ya know, saving a reputation like that... that's not nothing."

    Sailor "I'd even say it's quite something!"

    Sailor "Hehe."

    Sailor "..."

    Sailor "S'cuse me, mate, you look uncomfortable."

    "His question wasn't unexpected, but it's not one I enjoyed answering."

    Detective "You're fine."

    "He struck a forced smile and aimed his attention back at sea."

    Sailor "..."

    Sailor "Before we get there, let me just make sure you understand something, mate."

    "The tide started to settle down as the port slowly came into view."

    Sailor "I'm not coming back unless I know you caught the bastard."

    Sailor "This place makes my body hair stick out."

    Sailor "Not the way it happens when you hear someone sing beautifully, or you're watching a hella good movie."

    "His hands were shaking on the wheel as he spoke."

    Sailor "I mean it as in..."

    Sailor "I feel like I'm mourning my own death just being here."

    Detective "You can just say you're terrified."

    Sailor "There ya go."

    Sailor "I got a life I give half a rat's ass about."

    "After that little speech, we finally arrived at the island."

    "I grabbed my suitcase in one hand and pulled out some cash in the other."

    Sailor "Nah, mate. No need for that. The job keeps me plenty fed."

    Detective "A reward for facing your fear."

    Sailor "Tss..."

    "He grabbed the cash and shook my hand."

    Sailor "Thank you, mate. Watch your back out there. You're gonna be a prime target the moment you're on ground."

    Detective "I'll be fine."

    "I stepped foot onto the port. Someone else was approaching me in the distance."

    Sailor "Oh, and if you want to quit..."

    Sailor "Find another way."

    Detective "Got it."

    Sailor "Alright. See you on the other side, mate."
    
    Detective "Take care."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    return
