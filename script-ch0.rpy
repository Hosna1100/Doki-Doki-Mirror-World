label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "Sayori catches up to me, breathing heavily."
    show sayori 4p zorder 2 at t11
    s "Huff... huff... Hey, [player]! Wait up!"
    "I slow down, pretending to be caught off guard."
    mc "Oh, hey, Sayori! What's up?"
    show sayori zorder 2 at t11
    "She grins, her eyes sparkling with excitement."
    s 1a "I found something amazing! You won't believe it!"
    "Sayori pulls out an old, ornate hand mirror from her bag."
    s "Look at this! It's like something out of a fairy tale!"
    "I take the mirror from her. The glass is pristine, but the frame is ancient."
    mc "It's beautiful, Sayori. Where did you find it?"
    s "In the attic of my grandma's house. She said it's been in our family for generations."
    s 1g "But that's not the best part! When I looked into it, I saw..."
    "She hesitates, her expression shifting from excitement to unease."
    mc "Saw what?"
    s "My reflection, but different. Like an alternate version of me."
    s 1h "And then I heard a voice. It said, 'Cross the mirror, find your other self.'"
    "Sayori's eyes widen, and I feel a chill run down my spine."
    s "What do you think it means, [player]?"
    mc "I don't know, Sayori. But this mirror... it feels powerful."
    mc "We should be careful. Maybe we shouldn't mess with it."
    s 1r "Aw, come on! It's an adventure! Let's see what's on the other side!"
    "And so, we decide to explore the mirror together."
    "We step closer to the mirror, our reflections merging."
    "Suddenly, the world shifts. Colors blur, and I feel disoriented."
    hide sayori
    show bg black
    "When I open my eyes, I'm no longer in there..."
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music m1
    "I'm standing in a twisted version of our school, eerie place."
    show sayori 3z zorder 2 at t11
    "Sayori is beside me, her eyes wide with wonder and fear."
    "The air smells of decay, and the walls pulse as if alive."
    s "Is this... the other side?"
    "I nod." 
    mc "It must be. But where are the others?"
    scene bg corridor
    show Sayori zorder 2 at t44
    show yuri 2y1 zorder 2 at t43
    "We explore the mirror world, finding Yuri—an aggressive, knife-wielding version of herself."
    show natsuki exe zorder 2 at f42
    "Natsuki is there too, her sweet facade replaced by a sinister grin. she looks like Sonic.exe"
    "And Monika..."
    show monika err zorder 2 at t41
    "Monika stands at the left side, her code visible, glitching."
    "She turns to us, her eyes hollow."
    m "Welcome to my nightmare."
    "We learn that Monika, aware of both worlds, tried to merge them."
    "But something went wrong. The mirror world feeds on our fears."
    "As we confront our darker selves, we risk losing our sanity."
    "And Monika? She's fading, her existence unraveling."
    "Our choices matter. We can save her—or doom both worlds."

    menu:
        "Save Monika":
            "I reach out to Monika, my hand passing through her glitched form."
            m "Find the mirror's core. Reverse the merge. Save us all."
            jump ch0_save_monika

        "Confront Yuri":
            y "Knowledge is a double-edged sword, [player]. Choose wisely."
            jump ch0_confront_yuri

        "Face Natsuki":
            n "Sweetness hides darkness. Embrace it, [player]."
            jump ch0_face_natsuki

label ch0_save_monika:
    # Save Monika path
    "I delve deeper into the mirror world, seeking its core."
    hide sayori
    hide yuri
    hide natsuki
    show monika err zorder 2 at t11
    "Monika's whispers guide me"
    m "Remember, reality bends to your choices."
    "As I approach the mirror's heart, I glimpse glimpses of forgotten memories."
    "The merge can be undone, but at a cost. Sacrifice awaits."
    "what should I do??"

    menu:
        "Rewrite the code":
            "I touch the mirror, lines of code flowing through my fingertips."
            "The world shudders, and Monika fades, her smile grateful."
            hide monika
            
            scene bg club_day_e
            with wipeleft_scene

            "Reality shifts, and I wake up in the literature club room."
            "The mirror is gone, but Monika's poem remains: 'In fractured worlds, we find salvation.'"
            return

        "Refuse":
            m "I understand. But remember, choices echo across dimensions."
            return

label ch0_confront_yuri:
    # Confront Yuri path
    hide sayori
    hide natsuki
    hide monika

    scene bg yroom
    with wipeleft_scene

    show yuri 2y1 zorder 2 at t11
    "Yuri's library holds forbidden tomes. Each book whispers secrets."
    "She offers me a choice: ancient knowledge or oblivion."
    "Will you read the forbidden grimoire?"

    menu:
        "Read the grimoire":
            "The words sear into my mind. I gain insight, but darkness consumes me."
            y "Power comes with a price, [player]."
            return

        "Resist":
            y "You're stronger than I thought."
            "She steps aside, allowing me to continue my quest."
            return

label ch0_face_natsuki:
    # Face Natsuki path
    hide sayori
    hide yuri
    hide monika
    
    scene bg kitchen
    with wipeleft_scene

    show natsuki exe zorder 2 at t11
    "Natsuki's kitchen smells of decay. Cupcakes lie on a blood-streaked table."
    n "Taste the truth, [player]"
    "Will you eat the corrupted cupcake?"

    menu:
        "Eat the cupcake":
            "Visions flood your mind—Natsuki's pain, her hidden past."
            "I gain resolve but lose a piece of myself."
            n "Sweetness has consequences."
            return

        "Reject":
            n "You're different. Keep that strength."
            n "Find answers, [player]."
            return



