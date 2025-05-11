# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Detective = Character("Detective", color="#FFFFFF")
define Sailor = Character("Sailor", color="#33DAFF")
define Local = Character("Local", color="#5b1bd1")


# The game starts here.

label start:
    "..."
    play music "audio/bgm_ocean.mp3" fadein 1.0
    "{i}January 14th, 2004.{/i}"

    "I couldn't see much beyond the shoreline."

    "Fog drifted low over the water, blurring the line between sea and sky."
    
    "The boat shifted and swayed with the pull of the sea."

    "I’ve sailed this route more times than I can count."

    "It always felt routine, like a trip to the local market."

    "But this time, the water felt unfamiliar — like I was sailing into somewhere I shouldn’t be."

    "There was a cold feeling in my chest I hadn’t known before — not from the winter winds, but from something else."

    Sailor "We're almost there, mate."

    Detective "Good, sitting gets exhausting."

    Sailor "Would you rather stand in front of this wheel for 12 hours straight?"

    Detective "I’ll pass, the physical prowess required is not in my skill set, sadly."

    Sailor "Hehe."

    "Weirdly enough, despite the sailor’s veteran status in the business, I actually had only just met him on that fateful day."

    "I was used to the ironically calming nature of a packed shuttle boat on my previously regular visits. I always found it easier to focus on my own thoughts if everyone around me was already busy with theirs."

    "In a one-on-one scenario, though, people just… can’t really keep it to themselves."

    Sailor "How you feeling? Nervous?"

    Detective "How many times do you think I've done something like this?"

    Sailor "Not enough, clearly. You’re jitterin’, hehe."

    Detective "Hmph."

    "That comment hurt a little."

    "I'd always been able to separate my work from my emotions."

    "Apparently, I'd let some cracks slip through."

    Sailor "I’m just teasin’ ya mate. I’d rather take a leaky boat through a galestorm than follow in your footsteps."

    Sailor "I mean, imagine seeing a lifeless body in front of ya… aches my heart just thinkin’ about it."

    Detective "You get used to it, I suppose."

    Sailor "..."

    "A detective’s task is more than just solving puzzles. It’s more like making sure the dead aren’t left behind."

    "My deductions decide whether or not the poor soul’s peace of mind will be ensured for the rest of eternity."

    "Remaining objective is the only way I can guarantee my chances of success."

    Detective "Once you learn to absorb the shock, the impact is lost."

    "The sailor looked at me like I was a monster in a horror movie."

    Sailor "H-hehe… I can’t relate, fortunately."

    "We kept inching closer to our destination."

    "The island was finally taking shape through the fog."

    Detective "No lights this time?"

    Sailor "People are scared, mate. Shut everything after sundown, from what I heard."

    Sailor "Shame, really. I used to drop by now and then — good folks."

    Sailor "Actually, they said even during the day, folks barely leave their homes. Only when they need to."

    Detective "I see."

    "The one thing that hadn’t changed was the night sky."

    "It’s ethereal beauty washed over me, as violet and green blurred together, painting the night sky."

    "This dazzling sight breathed some much-needed life back into this island cloaked in darkness."

    "Not as I remembered it, but beautiful nonetheless."

    Sailor "If you don’t mind me askin’..."

    Detective "Hm?"

    Sailor "Aren’t you the detective who cleared that one person in ‘92?"

    Detective "..!"

    menu:
        "Yeah, that was me.":
            jump Choice_1

        "...":
            jump Choice_2

label Choice_1:
    Detective "Yeah, that was me."

    Sailor "Damn. You got some flack for it, didn't ya?"

    Detective "I suppose I did."

    Sailor "Think you were right?"

    Detective "Yeah."

    Sailor "No hesitatin', huh. Hey, for what it's worth, I believe ya."

    Detective "I appreciate that."

    Sailor "Ya know, savin’ someone that was basically six feet deep already… that’s not nothing."

    Sailor "In fact, I’d say it’s quite something!"

    Sailor "Hehe."

    Sailor "..."

    Sailor "S'cuse me, mate. You look uncomfortable."

    "His question wasn’t unexpected, nor did I care much about giving out that info."

    "I'd rather he kept his mouth shut, though."

    jump end

label Choice_2:
    Detective "..."

    Sailor "Mate?"

    Detective "You’re gonna have to be more specific. Plenty of ‘one guys’ in my line of work."

    Sailor "..."

    jump end

label end:
    "He struck a forced smile and aimed his attention back at sea."

    Sailor "Before we dock, let me just make one thing clear, mate."

    "The tide started to settle down as the port slowly came into view."

    Sailor "I’m not coming back unless I know you caught the bastard."

    Sailor "This place… it gets under your skin. Not like when a song gives you goosebumps."

    "His hands were shaking on the wheel as he spoke."

    Sailor "I mean it more like… I feel like I’m mournin’ my own death just being here."

    Detective "You can just say you’re terrified."

    Sailor "There ya go."

    Sailor "I’m not planning an early retirement."

    "After that little speech, we finally arrived at the island."   

    "I got up, grabbed my suitcase in one hand and pulled out some cash in the other."

    Sailor "Nah, mate. No need for that. The job feeds me plenty."

    Detective "A reward for facing your fear."

    Sailor "Tss..."

    "He grabbed the cash and shook my hand."

    Sailor "Thank you, mate. Watch your back out there. You’re gonna be a prime target the moment you’re on ground."

    Detective "I’ll be fine."

    "I stepped foot onto the port. Someone was approaching me from a distance."

    Sailor "Alright. See you on the other side, mate."

    "He turned and left before I could say another word."

    "Now that my thoughts had space to breathe, I took a moment to recollect myself as I counted down to the mysterious person’s footsteps."

    "Setting foot on the island whisked away any sense of wonder I had looking at it from the outside."

    "Everything was dark and gloomy."

    "The mountains cast a shadow over everything as far as the eye could see."

    "The buildings were reduced to outlines in the obscurity, husks now devoid of any life."

    "The bright white snow was the only thing guiding my vision."

    "The island that used to be my haven had now shown another face."

    "And it was about to show me its teeth."

    Local "Are you the detective?" 




















    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    return
