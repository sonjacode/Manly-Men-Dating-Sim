# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up a default schedule.
init python:
    register_stat("Strength", "strength", 10, 100)
    register_stat("Intelligence", "intelligence", 10, 100)

# This is the entry point into the game.
label start:

    # Initialize the default values of some of the variables used in
    # the game.
    # Show a default background.
    scene black

    # The script here is run before any event.
    scene bg sandy ground
    with Dissolve(4.0)

    play sound "holyshit.mp3"
    "Holy shit."
    "I have a bomb inside my body, and the bastards wired it so if my heart rate goes below a number it blows."
    "Do I know that number? No. Do {i}they{/i} know that number? Of course not."
    "Holy."
    "Fucking."
    "Shit."
    "I've never been this pissed off, ever. All my life I, Joseph Joestar, was meant to be a suicide bomber, and now I'm not even going to be able to set myself off at the right place or time." 
    "Why are my kin so incompetent? Can't even wire a fucking bomb properly..."
    "*breathes*"
    "As long as my heart rate stays up, I'll be good. For now, I'm angry as hell so that should keep me going for a good bit. But it won't last forever, as I get happy too easily..."
    "I need something more permanent. Hmm..."
    "Walking on pins? nah, I don't want it to be that painful."
    "Running? I've never been much of a runner..."
    "Flying a plane without having a license? Sounds great, but I won't ever get to my precise location that way."
    "I need something that always keeps my heart racing, and is small enough to take with me to bombing targets."
    "Wait, I've got it!"
    "I'll fall in love."

    # We jump to day to start the first day.
    jump intro


# This is the label that is jumped to at the start of a day.
label intro:

    $ day = 0
    $ t_jeff = False
    $ t_horse = False
    $ t_conner = False
    $ t_ted = False
    $ t_max = False
    $ t_greg = False
    $ t_john = False
    $ t_lest = False
    $ t_dunk = False

    $ period = "introdutcion"
    $ act = "intro"

    call events_run_period

    jump city

label city: # future plans: have the Trap Map get darker as it turns night.

    if day < 40:
        $day = day
        call screen city_map
    elif day == 40:
        jump evening_visit

#label apothecary: # this scene may not be needed as there is a mandatory event where JoJo goes to meet so'jei for advice. 
#    
#    # Increment the day it is.
#    $ day += 10
#
#    "I decide to pay Sonja a visit."
#
#    jump city
#
#    return

label school:

    $ day += 10

    scene bg school
    "I go to the school. I recognize a few students here and there."
    "Looking around, there seem to be a few places to go to."

    $ period = "schoolyard"

    menu:
        "I decide to..."
        "...walk around the classrooms." if t_greg == False:
            $ t_greg = True
            $ act = "classroom"
        "...go to the library." if t_ted == False:
            $ t_ted = True
            $ act = "lib"
        "...climb up to the roof."if t_max == False:
            $ t_max = True
            $ act =  "roof"

    call events_run_period

    jump city

    return

label playground:

    $ day += 10

    scene bg playground
    "The playground is where I'm headed."
    "On the way I look more closely at the Trap Map to see that there are a few more places I can head to."
    $ period = "playground"

    menu:
        "Do I:"
        "Stay at the playground" if t_john == False:
            $ t_john = True
            $ act = "play"
        "Go to the nearby gym" if t_dunk == False:
            $ t_dunk = True
            $ act = "gym"
        "Sneak into a music studio" if t_lest == False:
            $ t_lest = True
            $ act = "studio"

    call events_run_period

    jump city

    return

label zoo:

    $ day += 10

    scene bg zoo
    "As I walk toward the zoo, I wonder what animalistic things I will see there."
    $ period = "zooppl"

    menu:
        "I reach the directory and ponder for a bit before going to the..."
        "...aquarium." if t_jeff == False:
            $ t_jeff = True
            $ act = "aquar"
        "...stables."if t_horse == False:
            $ t_horse = True
            $ act = "stabl"
        "...the rest of the zoo." if t_conner == False:
            $ t_conner = True
            $ act =  "rest_o"

    call events_run_period

    jump city

label evening_visit:

    $ period = "dark"
    $ act = "advice"

    call events_run_period

    jump sonja_advice

label sonja_advice:

    menu:
        "Greg" if t_greg == True:
            son "Ah, Greg... he's an odd one. Really hates jews, really doesn't like himself. Really likes Awesomenauts though... and Jesus's crucifixion."
            jump sonja_advice
        "Teddy" if t_ted == True:
            son "NO! I mean just go as yourself, he already loves you."
            jump sonja_advice
        "Max" if t_max == True:
            son "Max... uh... you know, I don't know. You might have a chance with him. I hear he likes Warframe a lot, so hey, you can give it a shot."
            jump sonja_advice
        "John" if t_john == True:
            son "For John, all you need is penguins. Trust me."
            son "You'll still regret it later."
            jump sonja_advice
        "Lester" if t_lest == True:
            son "Let me tell you a story. Lester was once playing top lane against this Riven, and they flirted all game."
            son "Nothing would be more humiliating than to dress up as his one and only love!"
            jump sonja_advice
        "Dunk" if t_dunk == True:
            son "Dunk really loves Dunkmaster Darius and having his ego stroked. I know he'll be dressed as Papyrus even though that's completely irrelevant to this story because we wrote this before everybody's obsession with Undertale."
            jump sonja_advice
        "Jeff" if t_jeff == True:
            son "I would tell you not to get involved with Jeff, but... if you must... you know his love of Pepes."
            son "If  you choose Jeff, I will make you the rarest Pepe of them all!"
            jump sonja_advice
        "Conner" if t_conner == True:
            son "Conner is the sweetest and most non-violent emu-man you will ever meet in your life."
            son "I would suggest dressing as his favorite: Team Spirit Anivia!"
            jump sonja_advice
        "Horse" if t_horse == True:
            son "Horse is a bit trickier. You need to dress like-"
            jojo "Don't worry about Horse. I have a costume he gave me that he wants me to wear."
            jump sonja_advice
        "That's all I visited today.":
            jump costume_pick

label costume_pick:
    
    scene bg cellar with dissolve
    "After this, Sonja takes me back down to her cellar. A bunch of fabrics are strewn across a small table."
    show sonja regular with easeinright
    son "Alright, JoJo. Now's the time for you to choose who you want to impress."
    son "So, knowing all of this, tell me- which costume would you like for me to make?"

    menu:
        "Dead Jesus" if t_greg == True:
            $ cos = "Dead Jesus"
        "No Costume" if t_ted == True:
            $ cos = "no_cos"
        "Warframe-themed" if t_max == True:
            $ cos = "Warframe-themed"
        "Penguin" if t_john == True:
            $ cos = "Penguin"
        "Riven" if t_lest == True:
            $ cos = "Riven"
        "Dunkmaster Darius" if t_dunk == True:
            $ cos = "Dunky"
        "The Rarest Pepe" if t_jeff == True:
            $ cos = "Pepe"
        "Anivia" if t_conner == True:
            $ cos = "Anivia"
        "Hatsune Miku" if t_horse == True:
            $ cos = "hatsu"
    
    if cos == "hatsu":
        "I show her the costume Horse has given me."
        son "Oh, wow. That'll work magic at the party."
        jojo "It sure will. I'll see you there."
        "The next night..."
    elif cos == "no_cos":
        son "You will look dashing as yourself. See you there JoJo!"
        "I tidy myself up and turn to leave."
        "The next night..."
    else:
        "She bustles off to gather materials for the [cos] costume."
        hide sonja with easeoutleft
        "A while passes, and soon she's done."
        show sonja regular with easeinleft
        son "It looks great on you! You'll be sure to seduce your chosen."
        jojo "Hopefully this works. See you there, Sonja."
        "The next night..."

    jump halloween

label halloween:

    scene mansion with dissolve
    "I walk up the steps of Lester's mansion."
    "I have a feeling it was the drug trade that paid for it, not his musical efforts."

    scene inside mansion with dissolve
    show lester hregular with zoomin
    "Lester appears."
    if cos == "Riven":
        jump HalloweenLester

    le "Welcome to the Halloween Party!"
    le "I like your originality! Enjoy yourself and have a good time with the others."

    hide lester with easeoutleft

    "Like that's even possible. Great."
    "I walk around a bit until I spot the trap I'm supposed to impress."

    if cos == "Froggy G":
        jump HalloweenGreg
    elif cos == "no_cos":
        jump HalloweenTed
    elif cos == "Warframe-themed":
        jump HalloweenMax
    elif cos == "Garen":
        jump HalloweenJohn
    elif cos == "Dunky":
        jump HalloweenDunk
    elif cos == "Pepe":
        jump HalloweenJeff
    elif cos == "Anivia":
        jump HalloweenConner
    elif cos == "hatsu":
        jump HalloweenHorse


label HalloweenDunk:

    $ period = "halldunk"

    show dunk hregular with easeinright
    du "Joseph...Dunkmaster Darius? Really?"
    jojo "I thought it would fit you well."
    show dunk hangry with dissolve
    du "Man you know Darius is 'balanced'!"
    du "Because you know, having more damage than a fed ADC is fair because he is also tanky..."
    jojo "Do you want me to go change?"
    show dunk hregular with dissolve
    du "No. I know it might be confusing, but..."
    show dunk hblush with dissolve
    du "I love unbalanced things."
    show dunk hregular with dissolve
    du "As a child, my father left me alone on a seesaw with a sack of potatoes on the other end."
    show dunk hsad with dissolve
    du "I was so afraid of heights, I stayed up there for a full 7 hours."
    du "The sack of potatoes... reduced in mass as my hunger increased."
    du "Balance nearly made me starve to death."
    jojo "Okay listen, I understand you need serious therapy,"
    jojo "but aren't seesaws like a foot off the ground?"
    du "Once we start imagining some horror..."
    du "It's not easy to realize it's illogical."
    jojo "Right..."
    jojo "Do you need a hug?"
    du "I have needed one for 17 years JoJo."
    du "But I must stay strong..."
    show dunk hregular with dissolve
    du "My pokemon need me!"
    jojo "It appears the need is mutual."
    show dunk hangry with dissolve
    du "Shut up! There are water pokemon. I am just trying to catch them in my tears."
    du "So how is the whole Regi thing going?"
    jojo "I tried to kidnap him but he said he didn't have the power to change pokemon."
    jojo "I guess that makes sense, TSM never really did pokemon."
    show dunk hregular with dissolve
    du "Wait, what?"
    jojo "You know, he used to be the mid laner for that League team."
    du "No... Joseph... no. Wrong Regi."
    jojo "Huh. So..."
    du "Please, release him. How else am I supposed to ironically cheer for TSM at worlds?"
    jojo "CLG beat them. Cheer for them."
    du "Where is the irony in that?"
    jojo "Come on. They are CLG."
    jojo "You know they will only win their first game in every series."
    jojo "Give the fans hope."
    du "Fair point."
    show dunk hseductive with dissolve
    du "Now get to work on getting the right Regi!"
    hide dunk with easeoutright  

    scene bg apothecary
    with fade
    "I feel confused. I need someone's advice. I'll visit Sonja."
    scene bg apothecary counter
    with CropMove(3.0, "slideawayleft")
    show sonja regular with easeinbottom
    son "Hey JoJo, what's wrong? You look down."
    jojo "I may have gotten myself involved with a psychopath."
    son "John?"
    jojo "Huh? Why does everyone think that?"
    jojo "No, Dunk. He wants me to help him kidnap someone."
    son "You have experience with that stuff. What's the problem?"
    jojo "I'm not getting paid to do it."
    son "Listen, you need to do this to complete your mission, don't you?"
    jojo "Yea, but he's starting to creep me out."
    son "Joseph... I have the blood of at least 40 on my hands."
    son "You look at me casually as a friend."
    son "Even though you have seen me murder infront of you,"
    son "you have no fear of me. Do not fear the Dunk."
    jojo "Hmm, that's a good point. Alright, I'll give it a try."
    jojo "Thanks Sonja, cya!"
    son "Goodbye JoJo!"
    hide sonja easeoutleft

    scene bg jojohome with fade
    "I can hear a knock on my door."
    show dunk regular with dissolve
    jojo "Dunk! I wasn't expecting you to come here. How did you get my address?"
    du "My pokedex tells me where everything spawns."
    du "Listen, I found a way to capture Regi!"
    jojo "Really? Thank god. I was out of ideas."
    du "There is a pokemon tournament coming into town."
    du "Regi and other Nintendo employees are there giving out legendary pokemon."
    du "I will go as myself with my Steel Team Six to dominate the competition!"
    du "You will crossdress as my lovely assistant, Maryl. I will build a pokemon team for you and..."
    jojo "Crossdress? Absolutely not. Joseph Joestar never does that!"
    du "Have you never googled {a=https://www.youtube.com/watch?v=SgWcSuxyvT8}\"JoJo Tequila\"{/a}?"
    jojo "I try to forget such moments."
    jojo "Still, I am going as myself. Lets do this."
    du "Fine...Deal."
    hide dunk with zoomout
    scene dunkscar with fade
    "I realize immediately after hopping into Dunk's car that I should have brought my own music to listen to."
    du "Gotta catch em all! Gotta catch em all! Pokemon!"
    scene black with fade
    "3 hours later..."
    scene dunkmatch with fade
    show dunk regular with easeinright
    jojo "Okay Daniel. It's time for your first match."
    show dunk sad with dissolve
    du "...yeah..."
    jojo "What's wrong?"
    du "You know how hearthstone now-a-days is just people playing the same 5 decks?"
    jojo "Sure?"
    du "What happens if my party is so good that people just copy it?"
    jojo "Is it really that good?"
    du "I am nearly undefeated."
    jojo "Well, keep that record going. No one could ever match your skill!"
    show dunk blush with dissolve
    du "You really think so?"
    jojo "Would you believe me if I said yes?"
    du "Less so after you say that, but if you pander to my ego enough, sure."
    jojo "Okay then yes."
    "A new challenger approaches!"
    show dunk regular at left with dissolve
    du "The name is Dunksexuality. I am ready to battle!"
    show dunk regular with dissolve
    "We begin whispering."
    jojo "I thought you were Daniel!"
    du "Huh? Oh, Dunk is just a screen name."
    jojo "Oh...Wait so you are sexually attracted to slam dunks?"
    du "Are you telling me that you don't get off to Space Jam?"
    jojo "Gotta be honest, never watched it."
    show dunk angry with dissolve
    du "WHAT!? But... It's Space Jam?"
    jojo "Wait... There he is. Regi!"
    show dunk blush with dissolve
    du "Oh my god... Is this what it feels like to be starstruck?"
    jojo "Focus on your game. I'll go do the deed."
    hide dunk with easeoutright
    show regi regular with easeinleft
    jojo "Hey Regi. The name is Joseph Joestar, but you can call me JoJo."
    jojo "Mind if I kidnap you?"
    regi "A little?"
    jojo "That's a shame. I have some political brainwashing to subject you to."
    "The fight goes on for a full 5 seconds before I win."
    show regi scared
    hide regi scared with moveoutright
    "Because I always win."
    show dunk regular with easeinright
    jojo "Okay Dunk, I got the goods."
    jojo "You ready to split?"
    show dunk angry
    du "Hang on. Just a second... This idiot thinks Hyper beam is a good move."
    jojo "He's 12, Dunk."
    du "Childhood is the time in life where the adults are supposed to tell you why your life choices are stupid."
    du "This idiot just happens to make it easy."
    jojo "Okay I might be a terrorist, but somehow I am judgemental of your morality."
    jojo "Lets get out of here."
    scene dunkhouse with fade
    show regi bound at left with easeinleft
    "We capture the Reginald and bring him to Dunk's house."
    show dunk regular at right with easeinright
    du "Okay Joseph, we got him. What now?"
    jojo "I thought you had that part planned out!"
    du "I must admit, this is my first kidnapping."
    jojo "I thought pokemon would have taught you to make kidnapped creatures fall in love with you!"
    du "This is Regi Joseph. He's no creature, he's a god."
    jojo "That seems a bit dramatic. Okay... Let's see what I can do."
    hide dunk with moveoutright
    show regi bound at center with moveinleft
    jojo "Listen, Regi, I need you to do me a favor."
    regi "I will never break! The pride of Nintendo is with me in all my actions."
    jojo "Never break?"
    regi "You can torture me all you want! Nothing will change!"
    jojo "Torture? That's... not a bad idea."
    "But how do I go about that?"
    menu:
        "Explain the ending of Bioshock Infinite":
            $ end = "bad_dunk"
            $ act = "dunkA"
        "Develop a love for Digimon":
            $ end = "bad_dunk"
            $ act = "dunkA"
        "Show him John's images for this game":
            $ end = "bad_dunk"
            $ act = "dunkA"
        "Jumper cables to the nipples":
            $ end = "good_dunk"
            $ act = "dunkB"
    
    call events_run_period

    jump end_credits

label HalloweenHorse:
    show horse hangry with easeinright
    ho "Damn it. I knew you'd come here like that, but it still pisses me off!"
    jojo "This is where all of the targets are."
    show horse hregular with dissolve
    ho "You make a valid point. Here, take a drink."
    jojo "Oh thank god. I was waiting all day for something to drink."
    show horse hangry
    ho "What? No. Don't drink that!"
    ho "That drink is poisoned."
    jojo "Normally someone would warn me of that BEFORE giving me the drink!"
    show horse hregular with dissolve
    ho "True, but do I seem like a normal person to you?"
    jojo "Fair point. So what do I do with this?"
    ho "Everyone wants a gift from their crush."
    ho "When one of the weeaboos comes to flirt with you, give them that."
    hide horse with easeoutleft
    "Wait, wasn't my goal to find love? Why am I killing the people flirting with me?"
    show john hblush with easeinright
    john "Miku? Is that you? Am I... just seeing things?"
    john "Can I please have a lock of your hair?"
    "Actually, I really want to kill them."
    jojo "Sorry, I need this hair for my next concert."
    jojo "Want my drink though? I put my lips on it."
    john "Is that even a question?!?!?"
    show john hregular
    john "Wait a second... This doesn't taste like a drink."
    john "This tastes like me dying."
    jojo "What does that even mean?"
    show john dead with dissolve
    "The entire party breaks into a panic when it is clear John is dead."
    "I barely survive the stampede to get outside."
    scene mansion with slideawayleft
    "Lester's house is forever ruined by the event."
    "But you know, he probably deserves it."
    show horse hregular with easeinright
    ho "Hahaha! Well done friend."
    jojo "Dear god. I have never met someone who is less creepy dead than alive."
    ho "Such is the life of a weeaboo..."
    show horse hsad with dissolve
    ho "It's a horrible disease. The people don't even know they are sick."
    jojo "I suppose so. So, that's 1 down."
    ho "Just 3 to go."
    jojo "I thought there were only 2 left."
    show horse hregular with dissolve
    ho "Right...2..."
    ho "I keep forgetting I crossed you off the list."
    jojo "That seems like an important thing to remember."
    ho "Anyways, lets talk about the next plan..."
    ho "Lester is hosting a concert soon."
    ho "Dunk is going to be there. Probably."
    jojo "Probably?"
    ho "I'm not his mother."
    ho "Anyways, here is a drill."
    ho "It's painted to look like one from Gurren Laggan."
    ho "He will beg you to kill him with it!"
    jojo "Those we worship rarely worship us back."
    jojo "Okay, I can do it. But what's with the trend of messing up Lester's events?"
    ho "He just happens to attract weeaboos."
    jojo "Is he one?"
    ho "Nah. Can't be. He watches Teen Titans."
    jojo "Fair point."

    scene concerthall with fade
    "I approach the concert. It's clear Lester went all out with this one."
    "Conner is helping him out by doing the lights."
    scene upper rows with dissolve
    "I can see Dunk sitting on the upper row, playing pokemon on his DS."
    jojo "*under my breath* This doesn't seem difficult."
    "But while climbing the stairs, I find Teddy."
    "He's watching crunchyroll on his tablet, completely distracted."
    "Oh how lucky... I get to kill 2 birds with one stone."
    "However, I know that Teddy is the truest of all weeaboos."
    "He's even trained in martial arts."
    "This is no easy fight. This is a boss battle."
    "I have to strike in a way that would kill Teddy for sure without giving him a chance to react."
    scene upper dunkonly with dissolve
    jump HorseTedKill
    return

label HorseTedKill:
    menu:
        "Spoil the end of Madoka Magicka":
            show teddy regular with fade
            jojo "Turns out at the end of Madoka Magicka..."
            te "Oh? That show? I already saw it. The ending was awesome huh? Remember when..."
            jojo "Wait, you already watched it?"
            te "Yea man. That was one of the most popular animes. Everyone's seen it."
            jojo "Damn it!"
            jump HorseTedKill
        "Challenge him to an Osu battle with a broken tablet":
            show teddy regular with fade
            jojo "Hey Teddy, fight me in Osu!"
            jojo "Queen - Having a good time"
            jojo "Easy mode..."
            te "Easy mode? Oh... You sure know my weak spot."
            "I hand Teddy the Tablet..."
            "He accepts it, filled with trust."
            "Weeaboos tend to be emotional, but they will trust anyone who shows interest in their hobby."
            "And so the battle begins."
            "Even with the trick I pull, it is a hard fought battle."
            "Actually, it isn't."
            "Teddy has 10 times my score."
            "And I thought that I was doing well."
            te "Thanks for the game man! It was fun. Anyways, I'm going back to my anime."
            jojo "Damn it!"
            jump HorseTedKill
        "Explain why RWBY is the best anime":
            show teddy regular with fade
            jojo "Okay but real talk here:"
            jojo "RWBY has 4 different main characters from the get go!"
            jojo "Then they add more as they go."
            jojo "What other anime can do that? Hunter x Hunter? Didn't think so."
            te "Yea actually I agree with you. I like RWBY."
            te "I don't know if I'd call it the best, but definately top 5."
            te "Plus, since it's American, the subs are more accurately translated."
            jojo "Subs? But... It's literally dubbed English!"
            te "The English dubs always suck. They censor out what the artists originally intended."
            jojo "The artists {i}wrote{/i} it in English!"
            show teddy angry
            te "Pfft. You call those people {i}artists{/i}?"
            te "The true artists are the fans who dub it into Korean!"
            te "Followed by the lengthy negotiations with a group of bank robbers to convert it to Spanish."
            te "Then, a group of rebel programmers try to convert it to binary."
            show teddy regular with dissolve
            te "The engineers then make it hexidecimal..."
            te "And then God himself decends to translate it into Japanese."
            te "And that gets subbed by a group of monkeys who learned the human language after years of research."
            te "Those are the true artists mankind needs."
            te "Not the 'Creators'."
            "Okay he lost me half way through his monologue. I need another approach..."
            jump HorseTedKill
        "Just fucking stab him with a gun.":
            show teddy regular with fade
            jojo "Hey Teddy!"
            te "JoJo! What's up with you?"
            "I pistol whip the weeaboo in the face."
            "It's fully loaded. I just really like hitting people."
            "Feels more personal."
            show teddy dead with dissolve
            "Within hours, the Ted is Ded."
            "Now, all that stands in my way is Dunk."
            hide teddy with zoomout
            scene empty seats with dissolve
            show dunk regular with dissolve
            jojo "Hey Dank Dan!"
            du "Hey JoJo? Wait... What's that in your hand?"
            jojo "It's a powerdrill."
            du "That hardly seems like the right attire for a concert..."
            jojo "You came here dressed as a pokemon trainer."
            du "That is true."
            du "Wait... Something is different about that drill."
            jojo "I may have painted it a bit special."
            show dunk blush with dissolve
            du "Oh my god!"
            du "Is that... Is that what I think it is?"
            jojo "It's the first piece in my cosplay set."
            du "You like Gurren Lagann? Oh my god man! Me too!"
            jojo "Hey want to pose for an image?"
            du "Absolutely!"
            jojo "Okay, let me just pretend I am going to stab you in the head with this drill"
            du "Your drill is the drill that shall piece my heavens!"
            show dunk dead with dissolve
            "I kill Dunk with little resistance."
            "His team of pokemon was never heard from again."
            "Mostly because he bled all over the DS and no one wanted it."
            hide dunk with dissolve
            "Well that's everything. I better return to Horse."
    
            jump HorseFinale
    
label HorseFinale:

    $ period = "horseydorsey"

    scene bg pastures with fade
    show horse regular with easeinleft
    jojo "I did it. They are all dead."
    ho "I can tell. The skype group chat is finally free of anime images."
    jojo "So what do we do now?"
    "I saw Horse removing a pistol from his belt."
    "Yeah, horses wear belts. What's it to you anyways?"
    show gun at center with dissolve
    ho "There is only one weeaboo left now."
    jojo "What? No! I helped you!"
    ho "Sure you did. But only to save yourself."
    ho "You killed all your friends just to survive."
    jojo "No, it was just fun."
    ho "That kind of mindset seems even more psychopathic."
    ho "Tell you what, I'll give you a chance."
    ho "Convince me to let you live."
    ho "If you weeaboos are bad at anything, it's persuasion."
    ho "Prove you aren't one of them. Otherwise..."
    "I hear Horse turning off the safety."
    jojo "Okay... Just give me a moment to think."
    "My heart's sure beating fast... This is good. Let's finish this."

    menu:
        "Convince him the animes he watched just weren't good ones":
            $ end = "horse_bad"
            $ act = "horseA2"
        "Pick Nunu":
            $ end = "horse_bad"
            $ act = "horseA2"
        "Pick Bard":
            $ end = "horse_good"
            $ act = "horseB2"
        "Confess your love":
            $ end = "horse_bad"
            $ act = "horseA2"

    call events_run_period

    jump end_credits

label HalloweenConner:
    show conner regular with easeinright
    co "Joseph! What are you doing here?"
    jojo "Lester invited me. Do you like my costume?"
    co "It's great, but it seems like a bad idea to come here when you have a bomb in your chest."
    jojo "Hmm, fair point..."
    jojo "But I am not a personality that can just be locked away!"
    jojo "Social events like these...People deserve to see the JoJo in his full glory!"
    co "Okay fine. But what can I do to help keep your heartrate up?"
    jojo "Hmm, Sonja recommended finding love. Maybe you could flirt with me?"
    show conner blush with dissolve
    co "...Flirt with you?"
    jojo "Yea. Boost my ego a bit."
    co "Huh...Okay lets see what I can do."
    co "Wow, you sure are good at AD Ekko JoJo. Where did you learn to play him that well?"
    jojo "Oh you know, Back to the Future, Bioshock Infinite, Life is Strange..."
    jojo "Time travel is just something I grew up with."
    show conner regular with dissolve
    co "Did that help at all?"
    jojo "Sure did."
    co "Okay good..."
    co "Um..."
    show conner blush with dissolve
    co "I really like your Zilean jungle? It pushes the meta to new heights."
    jojo "Why, thank you! I get told often that it pushes it to new depths, so hearing the opposite is great."
    jojo "It really is a jungler with a high skill cap."
    co "I just played Life is Strange and I loved it. Do you have any recommendations for good games?"
    jojo "You should buy God Will Be Watching."
    show conner regular with dissolve
    co "Oh, that one's good?"
    jojo "No! But you can refund it for Hatred."
    co "Hatred? Huh..."
    jojo "It's pretty good. You know, until you get to the tank level..."
    jojo "But then later you can buy Postal!"
    co "Okay, it looks like the party is coming to a close. We can get out of here now."
    jojo "What? You aren't going to pander to my ego anymore?"
    co "Relax. I can do that more later. Anyways, lets get going."
    co "I like Lester, I want to keep his house un-exploded."
    jojo "Fair point. Alright, lets go."
    hide conner with easeoutleft
    scene bg apothecary
    with CropMove(3.0, "slideawayleft")
    "I should get more advice from Sonja before I move on."
    scene bg apothecary counter
    with CropMove(2.0, "slideawayleft")
    show sonja regular with easeinbottom
    son "How did the Halloween party go?"
    jojo "Pretty well... I think. It was a bit odd."
    son "How so?"
    jojo "I convinced a man to flirt with me."
    jojo "Surprisingly, I like anyone who can boost my ego."
    son "So you found love?"
    jojo "He doesn't seem too interested in love."
    jojo "More so fixing the bomb problem."
    son "Fixing it?"
    jojo "Yea, changing the heart rate so that it won't set off without warning."
    son "Hmm... That sounds like something Conner would do."
    jojo "How'd you know who it was?"
    son "His personality is pretty unique."
    show sonja blush with dissolve
    son "Treat him carefully Joseph."
    son "He's a bit fragile."
    jojo "I'm always a careful man!"
    show sonja regular with dissolve
    "She shrugs."
    son "The planes you have flown would disagree."
    jojo "Fair point. Well, time for me to go."
    son "Good luck JoJo!"

    scene warehouse with fade
    "I meet Conner in an abandoned warehouse."
    "Normally this is where a drug deal would go down."
    "Of course, I already know that."
    "I didn't get this far in life being nice to punks!"
    "No... I'm a thug at heart."
    show conner regular with easeinright
    co "Oh, thank the Emu Gods you met me here Joseph."
    jojo "What is all of this about?"
    co "I've prepared this location to fix your... heart problems."
    jojo "Oh good. See, it gets really hard to sleep while making sure you keep your heart rate up."
    jojo "And the cocaine just doesn't feel the same anymore..."
    show conner angry with dissolve
    co "Wait what?"
    jojo "Nothing!"
    jojo "So, fixing the bomb..."
    show conner regular with dissolve
    co "Right. That problem..."
    co "It's alright Joseph, I can fix the bomb..."
    co "Using..."
    co "MY EMU POWERS!"
    co "You can have your life, your love, and your destiny!"
    jojo "Emu powers? I have never heard of these before."
    co "All I have to do is channel my energy into your heart."
    jojo "And how will you do that?"
    co "Like this!"
    "A full 15 seconds go by."
    jojo "You... You did nothing."
    show conner sad with dissolve
    co "I kinda hoped the situation would solve itself."
    show conner regular with dissolve
    co "Okay, here I go, this time for real..."
    "I can feel Conner focus all his energy into my heart."
    scene black with fade
    "I always was able to tell what people were thinking."
    "I know everyone's next line, next thought, next plan, next hope."
    "I know exactly what is going through Conner's head."
    scene australia with fade
    "He envisions his homeland, Australia..."
    "He remembers very clearly the day he became an Emu."
    scene ice cream with fade
    "It was a difficult case. The Ice Cream bomber."
    "He was famous for... You know, bombing ice cream trucks? The name kinda says it all."
    "He was on his way home from work. He had just caught the perp."
    "But then... He heard the jingle."
    scene kids with fade
    "At first, he thought he was just imagining it, but then he heard the kids scream \"Ice Cream\"!"
    "Quickly, he shouted for them to take cover."
    "None of them were hurt."
    scene bomb with fade
    show conner sad with dissolve
    "But it was far too late for him..."
    "I could see the horror on his face as he recalled the explosion."
    "It turned him into the emu he is today."
    scene office with fade
    show conner sad with dissolve
    "His boss fired him. His wife left him. His dog ran away. That's unrelated, but still sad."
    "The discrimination an emu faces in a modern world... How horrifying."
    scene black with fade
    show conner regular with dissolve
    "But finally... He finds me. The first person to accept him for who he is."
    "I can never betray that trust."
    scene warehouse with dissolve
    show conner regular with dissolve
    co "Okay... I think I did it."
    jojo "Really?"
    co "I'm not sure you want to test it, but it looks like it worked."
    co "I must admit, this is my first time using my emu powers for good."
    jojo "You use them for evil?"
    co "No... more just to get the TV remote."
    co "So for neutral."
    jojo "Conner... You saved me, man."
    jojo "But how do I set the bomb off when I need it now?"
    co "Well... You just have to stop your heart."
    jojo "Only my grandchild can do that!"
    jojo "Well... I mean, I guess I could always kill myself, but that's suicide!"
    jojo "No Joestar would do that!"
    co "Aren't you a suicide bomber?"
    jojo "Yea but... hmm... Actually, how was I planning to survive the explosion?"
    jojo "I mean, the bomb {i}is{/i} in my heart."
    jojo "Now I just feel robbed."
    jojo "I feel like I need to go. Goodbye Conner."
    co "Goodbye Joseph. I hope I can see you again."

    scene bg jojohome with fade
    "The bomb problem is solved... but I feel so empty."
    "I haven't even seduced anyone!" with hpunch
    "I know I don't need to anymore but..."
    "I'm not one to back down from a challenge!" with vpunch
    "I'll ask Conner to go with me to the carnival."
    "And while he's there, I'll confess my feelings to him!"
    scene carnival with fade
    show conner regular with easeinright
    co "Joseph... Thank you for inviting me out here."
    jojo "Absolutely! I like spending time with you."
    show conner blush with dissolve
    co "Joseph..."
    jojo "So, what would you like to do while we are here?"
    show conner regular with dissolve
    co "Hmm... How about some games?"
    jojo "Do you want me to win you a prize?"
    show conner blush with dissolve
    co "A gift from you Joseph? Oh, please! I'd love one!"
    scene corkshooter with dissolve
    show conner regular with dissolve
    jojo "How about this cork-shooting game?"
    "All the targets here are Evelynns?"
    "I like this place..."
    show crowd behind conner with dissolve
    s1 "What? An Emu? At a carnival?"
    s2 "Oh god. I hate Emus..."
    s1 "I know right? And this is the ugliest one of them all!"
    s2 "It looks like he is crossed with a human!"
    s2 "Quick, cover the childrens' eyes. They don't deserve to see this horror."
    show conner sad with dissolve
    "Its clear to see Conner is depressed now..."
    jojo "Hey, leave him alone! He just came here to have fun!"
    s1 "An Emu? Having fun at a carnival? Ha!"
    s2 "Don't they have those in Australia? Go back home! You aren't welcome here."
    co "Joseph... It's alright, I can just go."
    jojo "No."
    co "Huh?"
    jojo "A Joestar never backs down when someone threatens his friend."
    co "Joseph...You don't have to fight for me."
    jojo "I know I don't need to. That doesn't change the fact that I want to."
    co "Joseph..."
    "But how do I go about taking them out without ruining the date?"
    hide conner with easeoutright

    $period = "emu"

    menu:
        "Break some knees":
            $ end = "conner_bad"
            $ act = "ConnerA"
        "Point the cork-gun at them":
            $ end = "conner_good"
            $ act = "ConnerB"
        "Stop heart and make the noble sacrifice":
            $ end = "conner_bad"
            $ act = "ConnerC"
        "Leave with Conner and don't start a conflict":
            $ end = "conner_bad"
            $ act = "ConnerD"

    call events_run_period

    jump end_credits

label HalloweenJeff:
    jeff "Joseph, to come here dressed as a pepe..."
    jeff "I didn't expect you to be a work of art!"
    jeff "But boy... I sure don't want to trade you away."
    jojo "It is concerningly easy to find costumes of any meme."
    jeff "Pepe is more than just a meme! It is a way of life. It is a religion."
    jojo "You are concerningly devoted to pepes."
    jeff "I was down in a dark place a few years ago. I found myself at the same bar every night and the same alley every day."
    jeff "Pepes picked me up. They took me to a higher place."
    jeff "To not show my appreciation would be nothing short of deicide."
    john "Jeff! What are you doing here, idiot?"
    jeff "JOHN! OH GOD!"
    john "JoJo, is that you? Why are you dressed as pepe?"
    jeff "JOHN, I PROMISE I WASN'T CHEATING ON YOU!"
    jojo "Cheating on him?"
    jeff "Me and John have been dating for about 5 years."
    jojo "Oh god. I'm so sorry John, I thought he was single."
    john "It's okay. I wasn't very committed to the idiot anyways."
    jojo "Wait... what?"
    jeff "WHAT THE HELL DO YOU MEAN BY THAT?"
    john "Well, I didn't think you took the relationship that seriously, idiot."
    jeff "SERIOUSLY? WE WERE TOGETHER FOR 5 YEARS!"
    john "True, but if you think about it, we've been apart for longer."
    john "Anyways, cya. I'm going to go fake happiness and cry myself to sleep."
    jojo "That was..."
    jeff "Well it appears I am now single."
    jojo "Guess so... Maybe we can fix that."
    jeff "I guess we will just have to see, huh?"
    jump War
    return

label WarJeff:
    jojo "Jeff? What the hell is with you man?"
    jeff "Plenty. I am firing guns at my friends."
    jojo "No, well, yes, but what I meant was that you don't even code. Why are you in this war?"
    jeff "I just like rubies."
    jojo "Any reason why?"
    jeff "It pisses Teddy off."
    jojo "Okay that is actually a very valid reason."
    jojo "But can't you just photoshop his face?"
    jeff "That's cold JoJo. You know damn well I can't."
    jojo "You run an underground pepe dealership. I think you can trade other 'art' too."
    jeff "I didn't say that was something that was out of the question."
    jeff "But how can you piss Teddy off if you can't even show him the images?"
    jojo "That was a surprisingly valid point."
    jojo "Anyways, how can I help?"
    jeff "Well... You know how I said I was shooting my friends?"
    jojo "On which occasion again?"
    jeff "Well, my gun is jammed...Actually it'd be more correct to say I never coded it."
    jeff "I thought that coding would be easy to understand, but it's just... not."
    jojo "Sounds like you need Lua."
    jeff "I can't betray my Ruby gods now Joseph!"
    jojo "Fair point. I'll see if I can't fix this up."
    "I pull out my laptop."
    jeff "What are you doing?"
    jojo "Copy pasting code online."
    jeff "Isn't that plagerism?"
    jojo "Nah it's fine. I changed the header to include my name."
    jeff "I think the morals here are a bit shaky."
    jojo "Such is the world of a Comp Sci major."
    jojo "Anyways, here you go. I fixed your gun."
    john "Hey Jeff... I've been thinking-"
    john "We have been friends for quite some time. I noticed you haven't been shooting."
    john "What do you say we call it a truce, idiot?"
    jeff "RUBY IS GOD!"
    "The bullets call the end() function on John's life."
    jojo "... wow."
    jeff "Holy shit. I just killed my own friend."
    jojo "Do... do you need to talk about it?"
    jeff "Nah man lets celebrate!"
    "Jeff runs off into the horizon."
    john "JoJo... revenge me..."
    jojo "Sorry man. A captain doesn't follow his crew, the crew follows the captain."
    john "Okay well can you at least stop the bleeding?"
    john "Joseph... Why are you leaving?"
    john "COME BACK DAMN IT!"

    "I go back to the aquarium with Jeff."
    jeff "Joseph... You have yet to give me my pepe art."
    jojo "Okay, seriously? I just walk in here and you are already asking me for something?"
    jeff "Formalities seem unnecessary. Now give me my pepes or I'll give you some painpe."
    jojo "Alright, fine. Let me just..."
    "I didn't prepare one. Crap... Okay we can solve this."

    jump JeffChoice

label JeffChoice:

    menu:
        "Draw one for Jeff":
            jojo "There, I made one. What do you think?"
            jeff "Joseph... This is..."
            jeff "Horrible. Literally the worst thing I have ever seen."
            jojo "No need to be a dick. Let me try something else."
            jump JeffChoice
        "Google, save me again!":
            jojo "Look, isn't this amazing?"
            jeff "This is the first response on the second page of Google."
            jojo "Yea... But isn't it still great?"
            jeff "Joseph... You know I am addicted to pepes."
            jeff "Do you {i}really{/i} think I never did a google search for them?"
            jeff "What kind of idiot do you take me for? HUH?"
            jojo "Okay plagerism isn't going to work here. Let's try something else."
            jump JeffChoice
        "Use your Ekko ult to go back and get one":
            "I go back in time to reinvent the meme."
            "I convince all the famous artists to make their pepe art."
            "Picasso, Michelangelo, Dunksexuality, Kanye..."
            "They all pour their hearts out to make the best art they can."
            "Then I rewind again, claiming the art as my own."
            jojo "Will this do Jeff?"
            jeff "My god... JoJo... This is beautiful!"
            jojo "Just like you."
            jojo "You see, I have always loved you Jeff."
            jeff "Mhmm. That's nice and all. When are you planning on marrying him?"
            jeff "Wait... I'm me."
            jojo "Ye...Yes? Yes you are."
            jeff "Joseph... I love you too."
            jojo "Jeff..."
            jeff "Me..."
            jojo "Sorry if this is a little forward, but what would I do to get in your pants?"
            jeff "Well, hopefully you'd take them off me first."
            jojo "Not quite what I..."
            jojo "Okay whatever. I got the {a=http://www.insolitology.com/guides/fuckdolphin.htm}dolphin sex link{/a} from Sonja."
            
            $ end = "jeff_good"

            jump end_credits

        "Secret Joestar Technique": 
            "This hardly seems like the right time to run."
            jump JeffChoice

label HalloweenJohn:
    john "...I have consumed all the JoJo with my eyes, and he tasted delicious."
    john "But I have yet to appreciate said taste with my mouth, may I have a little nibble?"
    jojo "Is this you flirting?"
    john "No. I just like to open myself to new perspectives."
    john "And though cannibalism is a common perspective of mine, a refresher course is always handy."
    john "I sure do need myself a study guide..."
    jojo "Could you please stop devouring my fingers in the middle of conversation? It makes it really hard to understand you."
    john "Sorry about that."
    john "...Could you text me a picture of your hand later?"
    "Jeff enters the room."
    john "Jeff... I swear, it's not what it looks like... idiot!"
    jeff "HUH? JOHN, THERE IS LITERALLY NOTHING SUSPICIOUS GOING ON RIGHT NOW!"
    john "I know. But it's not what it looks like. I was cheating on you. For JoJo. You missed it, idiot!"
    john "JoJo, tell the idiot about the time I stuck your entire hand in my mouth just to express my love."
    jeff "JoJo... Is this true?"
    jojo "I really wish it wasn't. I'm trying to forget it myself."
    jeff "JoJo... I trusted you!"
    jojo "I am still confused what I did wrong. He walked up to me, stuck my hand in his mouth, then you came."
    jojo "I don't have much control over this stuff."
    jeff "That is it, I challenge you to a duel!"
    john "No, Jeff, you aren't challenging him to... that, are you, idiot?"
    jeff "YOU BET I AM!"
    jeff "Joseph...Are you prepared to do battle?"
    jojo "A Joestar is always ready."
    jeff "Okay... uh... well."
    john "What's wrong idiot? Tell him the duel rules!"
    jeff "Uh... um..."
    jeff "Okay I've gotta be honest, I didn't think you'd say yes."
    john "Idiot... Did you prepare nothing?"
    jeff "I WAS JUST GOING ALONG WITH WHAT YOU WERE SAYING!"
    john "But I was also just going along with what I was saying idiot!"
    jeff "Wait, I've got a solution!"
    jeff "My Problem-Solver Revolver!"
    "Jeff points a gun at me."
    jojo "Oh god!"
    jeff "Give me a reason not to pull the trigger."
    jojo "I have a bomb wired to my heart that will blow this entire mansion up if my heart even begins stopping!"
    jojo "Though blowing up expensive buildings is my mission, do you really think I would throw my life away just to hurt Lester?"
    john "Yea, you would."
    jeff "I'm going to have to agree with John here."
    le "That kind of does sound like something you'd do."
    jojo "Okay, you all make a valid point."
    jojo "Pull the trigger. I'll dodge the bullet."
    "Dear god... I really hope he falls for that bluff."
    jeff "Will do!"
    "SHIT!"
    menu:
        "Dodge left":
            "The bullet hits me. I am bleeding everywhere!"
            john "Jeff, no, you idiot! He was my love..."
            jeff "YOU MET HIM UNDER AN HOUR AGO!"
            john "But that was the best hour of my life... If you shift your metrics to support my conclusion... idiot."
            jojo "I... huh. I'm not dead yet."
            john "Were you sleeping?"
            jojo "Greg isn't even in this conversation!"
            gr "You'd be surprised how many people start paying attention to conversations after a gunshot and a pool of blood."
            jojo "Fair point."
            john "But Joseph... I feel betrayed."
            jojo "You know, I really would love to listen to your abandonment issues, but I am seconds away from bleeding out!"
            john "I thought your love for me made you strong enough to not fear death."
            john "But instead, you tried to dodge."
            john "What do I mean to you?"
            jojo "Once again, bleeding to death right now."
            john "So both of our hearts are working overtime..."
            jojo "Okay, at least you are listening to me."
            john "I'm sorry JoJo. I have to go."
            jojo "Literally bleeding to death here!"
            john "Bye!"
            jojo "Damn it."

            $ end = "john_bad"

            jump end_credits

        "Stay still":
            jojo "OH JESUS CHRIST!"
            jojo "Oh... I'm still alive."
            john "Did you just miss a man who stood still, idiot?"
            jeff "NO!... A LITTLE."
            john "Maybe this is a sign... Joseph was willing to take a bullet for me."
            john "He really does love me doesn't he..."
            jojo "I have never said those words in my lifetime and that has served me well. Lets continue that trend."
            jeff "It is clear. You deserve John more than I do."
            jojo "Okay, but does John deserve me? This appears to be a question no one asks themselves here."
            jeff "I... I'll just leave now."
            jojo "Before you go, I have one question."
            jojo "Male or female?"
            jeff "Same as John."
            jojo "You know, I am beginning to see how you two fell in love."

            jump War

        "Dodge right":
            "The bullet hits me. I am bleeding everywhere!"
            john "Jeff, no, you idiot! He was my love..."
            jeff "YOU MET HIM UNDER AN HOUR AGO!"
            john "But that was the best hour of my life... If you shift your metrics to support my conclusion... idiot."
            jojo "I... huh. I'm not dead yet."
            john "Were you sleeping?"
            jojo "Greg isn't even in this conversation!"
            gr "You'd be surprised how many people start paying attention to conversations after a gunshot and a pool of blood."
            jojo "Fair point."
            john "But Joseph... I feel betrayed."
            jojo "You know, I really would love to listen to your abandonment issues, but I am seconds away from bleeding out!"
            john "I thought your love for me made you strong enough to not fear death."
            john "But instead, you tried to dodge."
            john "What do I mean to you?"
            jojo "Once again, bleeding to death right now."
            john "So both of our hearts are working overtime..."
            jojo "Okay, at least you are listening to me."
            john "I'm sorry JoJo. I have to go."
            jojo "Literally bleeding to death here!"
            john "Bye!"
            jojo "Damn it."

            $ end = "john_bad"

            jump end_credits


label WarJohn:
    jojo "Finally I found you John. You know this is the C++ combat camp, right?"
    john "Sure I do. But this is the point I chose to hold down."
    jojo "I see your positioning skills haven't changed."
    john "Okay now is a bad time to make jokes. There are people dying all around us."
    jojo "I am a suicide bomber. You are aware of this, right?"
    jojo "Not only do I kill as many people as possible."
    jojo "But you have done nothing but crack jokes about the situation."
    john "No need to blow your top."
    jojo "Okay fuck you for that one."
    jojo "Anyways, how can I help?"
    john "I need you to take this break statement grenade and throw it into Teddy's hut."
    jojo "This is just a regular grenade that you wrote 'Break' on."
    john "Sure. You always have to use some imagination when larping."
    john "But I want to make sure I'm not imagining that stupid motherblubber dying."
    jojo "Okay this is seriously creeping me out now."
    john "You are a man of many explosions. What is one more to you?"
    jojo "Okay... I'll do it."
    "I go on a 3 meter trek to Teddy's place."
    jojo "Yo Ted."
    te "JoJo, don't scare me like that. You need to warn me when you come in here."
    jojo "Sorry man. Hey, I'm practicing my Captain Gangplank cosplay. Want an orange?"
    te "Sure. I'm getting a bit hungry."
    jojo "Sorry, all out. Have a grenade instead!"
    te "This isn't an orange, this is a grenade!"
    te "DAMN YOU JOHN!"
    "3 more meters later."
    jojo "Okay problem solved."
    john "That sure was fast!"
    jojo "You know, everyone trusts a lua user."
    jojo "But we are the people most likely to kill you."
    john "That sounds psychopathic. But not wrong."
    jojo "So when is he going to wake up from that stun grenade?"
    john "Soon. Hey, don't look at the back of your shirt."
    jojo "Huh? Wait... Why is it coated red?"
    john "Oh it's probably paint. Some stun grenades are like that. Anyways, lets get out of here."
    jojo "What about Jeff?"
    john "He's a ruby user. I'd be impressed if his program hasn't crashed yet."
    jojo "Fair point."  

    "We return to the park together."
    jojo "John... I have a confession for you."
    john "I promise to make eye contact and pretend to listen until I get bored."
    jojo "John... I..."
    john "Already bored. Too many dramatic pauses."
    jojo "Fine. I love you."
    john "No you don't."
    jojo "I really hope you'll accept my feelings... Wait what do you mean I don't?"
    john "You didn't even fix the roundabout!"
    jojo "...You know you can be a real dick sometimes."
    john "That is my primary goal in life."
    jojo "Okay... fine. I'll fix it now. What... What do I have to do to fix it?"
    john "How the hell am I supposed to know? I only break things, not fix!"
    jojo "I thought you said Jeff broke it?"
    john "I thought you learned not to believe a word I say."
    jojo "Fair point. Okay... Let's see here..." 

    jump JohnOption

    return

label JohnOption:

    menu:
        "Bash it with a hammer":
            "The roundabout begins bleeding."
            jojo "OKAY WHAT THE HELL!"
            john "Yay! You fixed it!"
            jojo "John there is blood everywhere. What... What have I done?"
            john "You fixed it."
            jojo "What was with this roundabout John? There is something you aren't telling me."
            john "Hmm? Sorry, am I acting a bit suspicious?"
            john "See, normally, the person covered in blood would be considered the suspicious one."
            john "But by all means, call the police. I'm sure they will believe you."
            "Well... It certainly wasn't the first time I killed someone. If I'm going to be a good suicide bomber, I can't let this bother me."
            jojo "So it's fixed?"
            john "Sure is. Don't mind if I just hop on it and take it on a test drive..."
            john "Actually..."
            jojo "Hmm?"
            john "Every ship needs a captain, don't you think?"
            jojo "It sure does Johno, it sure does..."
            "And so we spun for hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "And hours and hours."
            "This is getting old."
            "Can we move on?"
            john "Joseph... You really do love me don't you?"
            jojo "I begin to have my doubts from time to time, but sure."
            john "Joseph..."
            jojo "Johnny boi..."
            "The words were in each of our heads, but neither of us had the courage to say anything."
            john "Want to have sex?"
            jojo "Just one question, what gender are you?"
            john "The world is not in booleans JoJo." #Faking Sonja 
            jojo "That... Okay, screw it."
            john "Screw it... Good word choice."

            $ end = "john_good"

            jump end_credits

        "Sing the Space Jam theme with the hopes of pleasing the gods":
            "I put my pride on the line for this song. The gods listen, appreciatively. But god is a dick and doesn't return the favor."
            john "JoJo, your voice is pretty seducing, but there is still the issue of the roundabout..."
            jojo "We can't all be perfect. You have to cherish yourself when you are."
            jump JohnOption
        "Give it a motivational speech":
            "Listen, I know you wanted a \"Just do it\" meme, but you ain't getting it."
            jojo "Just do it!"
            john "That meme kinda got done to death."
            jojo "True..."
            jump JohnOption
        "Hope it fixes itself":
            jojo "I don't know what I was expecting."
            john "Oh hey Joseph it looks like it's working now!"
            jojo "Wait, really?"
            john "NO. You literally sat there for 20 minutes doing fuck all!"
            jojo "But you sat with me doing fuck all too!"
            john "Yea but who is woo-ing who over here?"
            jojo "Fair point."
            jump JohnOption

label HalloweenLester:
    le "Dear god! Who is the man within this gift from god?"
    le "If you are even a tenth as beautiful, take me now! You have earned my heart."
    jojo "Lester. Seriously. I wanted to flatter you, but shut the hell up."
    le "Sorry man. I just get really excited about Rivens."
    jojo "I know. Okay man? I know. You are a le epic memer. This is a meme. You must fight your addictions."
    le "You are right...You are so right. But god... You are also so beautiful."
    jojo "Would it help if I dressed as something else, like DJ Sona?"
    le "DJ Lessy-Les shall never be outdone by a pathetic DJ like Sona."
    jojo "You take everything way too seriously. Have you been hanging out with John too much?"
    le "I try to avoid him."
    jojo "Yea, me too."
    john "*as a voice* Hey you assholes, knock that off. I'm writing your scripts!"
    le "Anyways, can I give you some lyrics to sing?"
    jojo "In the middle of this party?"
    le "You will be singing for an album that will be bought by over 20 people!"
    le "If you can't sing infront of a measly 40, you won't stand a chance."
    jojo "Is your ego blinding your math skills?"
    le "No. My ego died long ago. I just like to hope that if I pretend to be famous, I will be famous."
    jojo "It works for most celebrities..."
    jojo "Okay. I'll give it a try."
    le "Excellent! Here is the script."
    "As I read the script, at first I am amused. Then inspired."
    "Then I leave the party for a bit to throw up."
    jojo "Oh god that was horrible. Still, I just want to keep reading it."
    le "Art isn't meant to make you feel like a god."
    le "Art takes you through the full array of emotions. Starting at index 0."
    jojo "Coding jokes?"
    le "I told you, 20 people buy my albums. I need something to keep the lights on."
    le "But anyways..."
    le "Art is a work that can make you feel the full human experience."
    le "When you find yourself in a field of roses, then find yourself crying seconds later when you realize..."
    le "The petals aren't red because they are roses. They are red because they suffered discrimination for being purple..."
    le "That's what art is. What you just read is art."
    jojo "Sorry. I threw up again. What were you saying?"
    le "Oh nevermind. Just get up on stage on sing it."
    "Fuck no. Let's hope the audience doesn't get as {i}invested{/i} in this song as I did."
    "My hopes are utterly worthless. Without hesitation, the audience begins throwing up."
    crowd "Encore! Encore!"
    le "Bravo! Bravo! The crowd of 10 is just begging for more!"
    jojo "Okay, did you manage to find a crowd of masochists?"
    le "No... kinda. Absolutely, actually. Sonja's one of them..."
    jojo "Also, didn't you say there were 40 people here?"
    le "Not all people enjoy art JoJo. Success means controversy."
    jojo "Uh huh..."
    le "Will you sing another for the crowd?"
    jojo "Listen, I really appreciate all of the nothing you do for me,"
    jojo "but I think I should get out of here while there is still a path on the ground that is clean."
    le "Fair point... wait a second..."
    le "THIS IS MY MANSION!"
    le "Oh crap... Who is going to clean this all up?"
    jojo "That would be you."
    le "Damn it! Joseph come back!"
    jojo "I would love to, but actually, I would hate to. I lied entirely."
    le "JOJO!!!!!" 
    jump LesterThree
    return  

label LesterThree:
    "Lester had invited me to his studio to record."
    "I'm prepared for everything and anything. No matter what the lyrics are, I can do it."
    "I learned to appreciate the value of Lester's art..."
    "I'm ready to love Lesters's work, sing my heart out, and succeed in my mission."
    le "Hey Joseph. Right this way."
    jojo "Lester! Finally. I have been looking forward to this all day!"
    jojo "Can I see the lyrics?"
    le "About that... I actually only wrote every other line."
    jojo "Wait what? How the hell do you even do that?"
    le "Who knows. Anyways, you can improv the rest!"
    jojo "But this is your masterpiece Lester! How can I capture the value of your song if you didn't even write it all?"
    le "It's okay. I will still take all the credit for it if it's good."
    jojo "That... somehow does seem like something you'd do."
    le "Sure does. Anyways, what I have will run on the teleprompt. Ready?"
    jojo "Wait what? No! I need some time to prepare."
    le "Okay." 
    le "3!"
    le "2!"
    le "1!"
    le "Go!"
    jojo "Goddammit."
   

    $ l1_Flag = False
    $ L2_Flag = False
    $ L3_Flag = False
    $ L4_Flag = False
    $ L5_Flag = False

    tp "A new day, a new hope"
    menu:
        "I really hope Senpai will notice me":
            $L1_Flag = False
        "I really want to blow up a building":
            $L1_Flag = True
        "There is a bomb in my chest":
            $L1_Flag = False
        "I am really bad at improv":
            $L1_Flag = False

    tp "Though society may beat me down"
    menu: 
        "They are bullies. No one likes a bully.":
            $L2_Flag = False
        "I am sexually thrilled by their pain":
            $L2_Flag = False
        "I can just kill them":
            $L2_Flag = True
        "Want to hear some cool bird facts?":
            $L2_Flag = False

    tp "My internal organs feel amiss"
    menu:
        "Because there is a fucking bomb in my chest":
            $L3_Flag = True
        "I really shouldn't have swallowed that kitchen knife":
            $L3_Flag = False
        "I sold too many on the blackmarket":
            $L3_Flag = False
        "The mitochondria is the powerhouse of the cell":
            $L3_Flag = False

    tp "Maybe it's time"
    menu:
        "For me to buy Hatred":
            $L4_Flag = False
        "For Riot to release more Ekko skins":
            $L4_Flag = False
        "For me to die, proud and without regrets ":
            $L4_Flag = True
        "This song is as edgy as the Mirrors Edge":
            $L4_Flag = False

    tp "They will remember me"
    menu:
        "As the man who died for his cause":
            $L5_Flag = True
        "Actually they won't. Fuck them.":
            $L5_Flag = False
        "As the man who was really awkward during that one fieldtrip":
            $L5_Flag = False
        "Yorick Morri.":
            $L5_Flag = False

    $SuccessCounter = 0
    if L1_Flag:
        $SuccessCounter += 1
    if L2_Flag:
        $SuccessCounter += 1
    if L3_Flag:
        $SuccessCounter += 1
    if L4_Flag:
        $SuccessCounter += 1
    if L5_Flag:
        $SuccessCounter += 1
    if SuccessCounter >= 3:
        jump LesterSuccess
    else:
        jump LesterFail


label LesterSuccess:
    le "Joseph that was... brilliant!"
    jojo "Thanks man. I really sung my heart out there."
    le "Finally, people will respect me as an artist."
    jojo "Your song sucked. I saved it."
    le "Yea, but the audience doesn't know that."
    le "Though your singing could have been better Joseph. You really should work harder."
    jojo "Okay seriously? They say everyone has a hard shell, but once you get under that..."
    jojo "I get the feeling that if I start finding out who you truly are on the inside, I will envy those who know you as a stranger."
    le "Dark, horrible things happen at band camp Joseph. Things you wouldn't believe."
    le "I went in a boy. I came out..."
    jojo "A man?"
    le "A trap."
    jojo "That comment really should make me hesitate to say this next bit, but it doesn't..."
    jojo "About my reward..."
    le "Oh right. Hang on. You wait right here and I will be back with that reward of yours."
    "I wait for 17 hours."
    jojo "Damn it Lester!"

    "I finally find him."
    jojo "Lester! What the hell do you think you are doing! You owe me a reward and you... Why are you crying?"
    le "I called my mother to tell her about how my album sold."
    jojo "And...?"
    le "She told me that 50 sales was still pathetic."
    jojo "Aww... I'm sorry."
    le "No. I am crying because that is the nicest thing I have ever heard about my art..."
    jojo "Is your life just based around being bullied?"
    le "I'm used to it."
    le "We're in the big bucks Joseph! We're rich!"
    le "And it's all thanks to you."
    jojo "Yep. Finally you realize."
    le "Joseph... I don't know how to say this."
    jojo "Then sing it."
    le "But you know I can't sing!"
    jojo "Those who say they can't never know their limitations."
    jojo "They only know their fears."
    jojo "You are not limited by your fears Lester."
    jojo "You are an artist. A man! Someone I can respect!"
    le "Joseph...."
    le "Okay, here I go!"
    "I immediately realize why Lester isn't a singer."
    le "When I get that feeling..."
    le "I need... sexual healing..."
    jojo "Oh dear god stop singing and take me."

    $ end = "lester_good"

    jump end_credits

    return

label LesterFail:
    le "Joseph, that was absolutely horrible."
    jojo "When you are taking credit for the success, it's difficult to get motivated."
    le "You can take credit for the failure!"
    le "I am publishing this entire thing under your name!"
    le "You will be the laughing stock of the century!"
    jojo "That really doesn't bother me."
    le "Oh yea? Well let's see how well it sells!"
    "3 weeks later."
    jojo "So Lester..."
    le "Shut up."
    jojo "I sold 100 copies."
    le "SHUT UP!"
    jojo "Remind me, you sell... 20, right?"
    le "The world is filled with unappreciative garbage who don't know true art!"
    jojo "That isn't wrong, but who sold more albums to that garbage? Me!"
    le "Yea? Well who has a bomb in their chest that explodes if they don't find love? HUH?!"
    jojo "Me!" 
    jojo "Oh... fuck."

    $ end = "lester_bad"

    jump end_credits

    return   

label HalloweenMax:

    $ period = "HallMax"

    ma "Joseph! You are here at last! Thank god."
    ma "I was beginning to get lonely."
    ma "And would you look at you! I didn't even know you played Warframe."
    ma "Anyways, I brought the package. Are we ready to... blow this joint?"
    jojo "What? No!"
    ma "Then... Why did you invite me here?"
    jojo "I need someone to date. I was hoping to find someone here."
    jojo "I need a wingman."
    jojo "But it sure does seem like a sausage-fest."
    jojo "All the girls seem taken."
    ma "...I'm still available."
    jojo "By the way, why would I bring you here with a bomb if I was going to blow this up?"
    jojo "Do you know of the property of diminishing returns?"
    jojo "Putting double the people on a task doesn't mean you get double the rewards."
    jojo "Two suicide bombers do just the same thing as one:"
    jojo "Blow up and die."
    ma "Okay, you make a good point. I just... I just am so excited, you know?"
    ma "I want to be on the news."
    ma "Imagine how proud my mother will be."
    jojo "Probably not very."
    ma "Yea, but she sure will be horrified, huh?"
    jojo "Oh look, a girl! Quick, back me up."
    jojo "Hey. You sure are looking single."
    jojo "Wanna fix that?"
    "I immediately get mace sprayed in my eyes."
    jojo "JESUS CHRIST!"
    ma "I thought you were converting to Islam."
    jojo "Oh... uh... Muhammed Christ?"
    ma "...better."
    ma "Do you want me to take her down?"
    jojo "What? Killing someone just because they rejected me?"
    ma "Is that a no?"
    jojo "I didn't say that. I just wanted to make sure that was why you were killing her."
    jojo "Go get her tiger!"
    ma "*STABBY STABBY*"
    "The party is quickly evacuated by the police."
    "{s}Oddly enough{/s} Being police, they can't find enough evidence to convict anyone."
    "The crime goes cold." 
    
    "I invite Max out to a hidden area, far away from on-lookers."
    ma "Okay Joseph, I'm ready for my training."
    jojo "Hold onto this box."
    ma "Sure...?"
    jojo "And keep this walkie-talkie on at all times."
    jojo "Now, wait here."
    "I run off into the distance."
    "Then, talking over the walkie-talkie..."
    jojo "Max, can you hear me?"
    ma "Uh... Yea... I can hear you."
    jojo "The box you are holding... I will now explain what it is."
    jojo "Within that box are 10 pounds of concentrated explosives."
    ma "OH DEAR GOD!"
    jojo "Stay calm. They are rigged to explode if you move too much."
    ma "Stay calm? STAY CALM?!?!?!"
    ma "I could die if I even shake too much!"
    jojo "Well you better not shake then."
    ma "..."
    ma "Okay, you're right. Deep breaths."
    jojo "Good. Now I want you to find somewhere you feel safe."
    ma "I found it. My ship in Warframe."
    ma "Just sitting in the cockpit, awaiting my exploration of the galaxy..."
    ma "Ah... I feel so relaxed."
    jojo "Good. Now imagine that someone is taking that place away from you."
    ma "What? NO! That is my home! That is the only place I have ever felt like I belonged..."
    ma "What do I have to do to get it back?"
    jojo "You can't get it back."
    jojo "They took it from you. It's out of your life forever."
    jojo "But you can get revenge."
    jojo "You can let your children enjoy the glory of the cockpit."
    jojo "All you have to do is kill them."
    ma "For the next generation..."
    ma "The message I will send will Ekko throughout time...."
    jojo "You mispelled echo."
    ma "No, I didn't."
    jojo "Good... I like you."
    jojo "Okay, are you committed to killing them?"
    ma "Absolutely. I will do anything to kill them."
    jojo "Anything?"
    ma "Anything!"
    jojo "Would you give your life?"
    ma "Yes."
    jojo "Without hesitation?"
    ma "Absolutely no hesitation."
    jojo "Good."
    jojo "Drop the box."
    "With only a second of delay, Max drops the box."
    "I can see through my binoculars..."
    "Max is crying..."
    "But he's also smiling."
    ma "Remember me for what I did, Joseph, not for who I became."
    "The box shatters into pieces."
    "Wooden pieces."
    "Max gets a splinter, but nothing more."
    ma "Joseph, I thought you said this was loaded with explosives!"
    jojo "I told you, if you trust me, you will learn to regret it."
    jojo "But it is clear now... You are ready."
    jojo "Within a single hour, you have accomplished what others have done in 15 minutes."
    jojo "Will you join me in my mission?"
    ma "Absolutely."
    ma "But... Joseph, I must tell you one thing."
    ma "I love you."
    jojo "Sorry. I don't swing that way."
    ma "What? But you did in all the other routes!"
    jojo "Sure, but you are different."
    jojo "You kept me focused on my mission."
    jojo "And now I am ready to destroy my objective, with your help."
    ma "Whatever happened to diminishing returns?"
    jojo "The engineers miscalculated more than just my heartrate. {s}fucking engineers man they screw everything up for everyone{/s}"
    jojo "This explosive isn't nearly strong enough to take out the whole building."
    jojo "I need your help."
    jojo "Will you assist me?"
    ma "Of course!" 
    
    "Max and I approach the building."
    "Silently, we give each other a nod."
    "Max is to go to the 2nd floor and set up explosives after securing the room."
    "My position is further down in the basement."
    "Each of us are armed well, both in firearms and pyrotechnics."
    "We are ready for our fate."
    "As I approach the lower levels, I found myself ambushed."
    po "Those engineers... can we really trust them to give us the right information?"
    pc "If they give us the wrong info, they die."
    po "They are suicide bombers. They fear not death." # pretentious bastards!
    pc "We can fix that."
    "Those engineers... is there anything they can't fuck up?"
    "It's okay. I can still make this work."
    "I just need some way to take these guys out..."
    menu:
        "Kill self, blowing up on the spot.":
            $ end = "max_good"
            $ act = "MaxA"
        "Use rifle to take them out":
            $ end = "max_bad"
            $ act = "MaxB"
        "Take a spirit photograph":
            $ end = "max_bad"
            $ act = "MaxC"
        "Garen Taric Bot lane: Stun and Spin":
            $ end = "max_bad"
            $ act = "MaxD"

    call events_run_period

    jump end_credits

label HalloweenTed:
    te "Joseph! I didn't even think you knew that anime character!"
    jojo "I don't. I just asked for the most anime costume they had."
    te "Sorry. I couldn't hear that. I was too busy falling in love..."
    te "Resist Teddy... resist..."
    te "He is only an anime fan in disguise."
    te "He didn't even read the manga."
    jojo "Right... moving along."
    jojo "What animes do you recommend?"
    "Teddy pulls out a 14 pound book."
    te "Here is the first volume. Tell me when you finish with this."
    jojo "But... there are nearly a thousand titles in here..."
    jojo "Even if I just watch one episode of each, that's still..."
    jojo "500 hours!?!?"
    te "I expect you to be done by Friday."
    jojo "This is legitimately impossible."
    te "You have an Ekko ult, don't you?"
    jojo "Sure, but this seems like a misuse of my power!"
    jojo "I mean, the timeline is fragile."
    jojo "If I mess it up..."
    jojo "Lester might not even be throwing this party! He might be dead!"
    jojo "Actually that feels inspiring."
    jojo "REWIND!"
    "I waste way too much time watching anime."
    "I can feel myself grow wise with knowledge."
    "Not any useful knowledge, just, you know..."
    "Knowing the names of all the characters in Madoka Magika."
    "Knowing which animes are best sober or high."
    jojo "Okay. I did it. What a world I have seen."
    te "Hmm?"
    jojo "Oh, right... I rewinded. You have no idea what I am talking about."
    jojo "Okay, lets see..."
    jojo "I really liked the part in Gurren Lagann where he put the other guy on his head."
    te "I know right? That was the best part!"
    jojo "And suddenly... I want every Ahri skin."
    te "Less so that but I guess so?"
    jojo "I really liked the ending of Hatred. You get to kill off millions of people for no reason!"
    te "That... that isn't an anime, Joseph."
    jojo "Sorry. I enjoyed my world of infinite time a bit too much."
    jojo "I meant to say that I really loved the part in Fate/Stay Night when they shot the guy."
    te "I know right? It was such a great scene."
    te "Notably, it was a politcal commentary."
    jojo "Really?"
    te "Yea. It was commenting on the fact that bullets kill people."
    te "And in war, it's for politic{s}al{/s} reasons."
    te "What a deep scene..."
    jojo "... yeah, sure."
    jojo "Okay. I am a bit lightheaded after... well, you know, after rewinding for 100 years."
    jojo "I'm going to go lie down."
    te "Goodbye Joseph!"
    te "God... I finally have someone to talk anime to!" 
    jump War
    return   

label WarTeddy:

    $ period = "tedders"

    jojo "Hey Teddy."
    te "Joseph! Put your hands up!"
    jojo "Woah, relax man."
    te "Sorry, this war is making me paranoid of all my friends."
    te "Notably, they aren't really my \"friends\"."
    te "Jeff uses Ruby..."
    te "RUBY!"
    jojo "It sure seems like this war has been going on for a..."
    te "Don't say it."
    jojo "A WHILE!"
    te "Notably, this is why I hate my friends."
    jojo "Forgive me. I've been hanging out with John too much."
    te "Makes sense."
    te "Notably, Jeff seems to be having trouble."
    te "He isn't a real coder, so this war has been hard on him."
    jojo "So he isn't a real threat then?"
    te "Yep."
    te "Notably, I like killing underdogs."
    te "So if you want to help me out here..."
    te "Maybe you could sabotage his code?"
    te "Notably, I don't think he would notice."
    jojo "Sounds good."
    "I travel a note-worthy distance."
    "Notably, it is only about 20 feet."
    "But I found a ton of notes on the ground as I walked."
    "It's worth noting that I read all the notes, that way I keep note of the situation."
    "Notably, they are all anime recommendations from Teddy."
    "He said that Death Note was pretty good."
    "Note to self, watch that later."
    "Finally, I reach Jeff."
    "He's humming to himself, but his pitch is a bit off."
    "So I try to help him correct his note."
    jojo "Okay, now that I solved that, do you have any other issues?"
    jeff "Yea... um... This is a bit odd to say, but..."
    jeff "My rifle wasn't coded right."
    jeff "Is there any chance you could help me repair it?"
    jojo "Sure. Do you have the source code?"
    jeff "Source code?"
    jeff "No. I didn't code this in Halflife."
    jojo "That's source engine."
    jojo "Here, give it to me."
    "Immediately, I plug Teddy's \"File Reader\" code into the gun."
    jojo "Okay, test it out now."
    jeff "It says it wants me to select a file to read. What do I do?"
    jojo "Oh, just select yourself. It needs to know who the owner of the gun is."
    jeff "Oh, okay. That makes sense."
    jeff "But now, JoJo..."
    jeff "I know you are working for Teddy."
    "Jeff points the gun at me."
    jojo "Woah, relax. I promise, I have done nothing to help him."
    jeff "No. You are trying to gain my trust so that you can betray me for him."
    jeff "I am not taking that risk."
    jeff "And now that you repaired my gun..."
    "Jeff prepares to pull the trigger."
    jeff "I can kill you so easily."
    jojo "Jeff! Don't pull the trigger! We can talk this through!"
    jeff "Too late."
    "Jeff pulls the trigger, completely ignoring me! What a dick."
    "But immediately, he is transformed"
    "All of his internal organs disappear. Along with his external organs. Whatever those are."
    "All that is left of him..."
    "Is a single number \"1\"."
    "I'm not if I should be horrified, but my job is done."
    "I return to Teddy to tell him of the good news."
    "But Teddy was already gone."
    "His while loop throws an infinite loop exception."

    "I leave to search for where Teddy was now."
    jojo "Finally! I found you Teddy!"
    te "JoJo! Dang it! I had been trying to hide from you!"
    jojo "Hide from me? Why? We seemed like we were really hitting it off."
    te "Joseph... I don't know how to say this to you..."
    te "You aren't a real anime watcher."
    jojo "What? I watched 500 hours of anime for you!"
    te "Sure... but I've seen you in your freetime."
    jojo "You watch me in my freetime?"
    te "I get lonely, okay?"
    te "You don't watch any anime by choice."
    te "Only by force..."
    jojo "Isn't it a sign that I love you more if I am doing something for you even if I don't like it?"
    te "Sure, you might like me."
    te "But I can only date a true anime watcher."
    te "Now... I bet you just fell asleep through most of the episodes!"
    jojo "What can I do to prove myself to you?"
    te "Tell me something only a true anime viewer would say."
    jojo "Something only a true viewer would say?"
    jojo "Hmm...."
    menu:
        "Explain why Teen Titan breaks down the cutural boundaries of anime":
            $ end = "ted_bad"
            $ act = "TedA"
        "Tell him why Yuno from Future Diary was as awesome as she is.":
            $ end = "ted_bad"
            $ act = "TedB"
        "Complain about Angel Beat's ending.":
            $ end = "ted_good"
            $ act = "TedC"
        "Blush and call him a baka.":
            $ end = "ted_bad"
            $ act = "TedD"

    call events_run_period

    jump end_credits

label War:
    "I find myself being dragged to a political summit."
    "I barely manage to get by without having to go through the metal detectors."
    "I have made no effort to conceal the fact that I am a living bomb. Why does everyone trust me so much?"
    "Across the room, I notice Sonja in a fight with some of her traps."
    son "Don't get me started on bounds checking."
    te "You break your entire program with just one off-by-one error!"
    john "And don't forget about \"Write once run anywhere\"!"
    son "John, do you know what a Mac is?"
    john "I only recently learned what a PC was."
    jeff "Okay, but hear me out here."
    jeff "What is worth more? A cup of coffee, a mediocre grade, or a fucking ruby?"
    son "Your coding language has nothing going for it. Nada. Zilch."
    jeff "Sure, but it has a cool name."
    te "Jeff, you don't even code."
    jeff "Cool name!"
    john "Okay even C++ is better than Ruby, idiot."
    te "Agreed."
    son "But at least all the loops carry over between the languages."
    john "I know right?"
    te "I would hate to have to use for loops. They are the bane of programming!"
    john "Don't you mean while loops?"
    te "No. While loops are the least understandable things in coding!"
    john "You write 3 lines of code to run the same thing I do in one."
    te "It's still the same amount of processing run by the computer though."
    john "Sorry, can't hear you over the sound of the bullshit coming from your mouth."
    jeff "BUT I COULD HEAR HIM."
    john "Jeff, it was a figure of speech, idiot."
    jeff "OH."
    "The argument goes on for the next 4 minutes. Somewhere in the chaos, Sonja manages to slip out."
    jojo "What was that about?"
    son "Oh, them? They get way too excited about coding."
    jojo "That actually seems like something they would do."
    jojo "We all know Lua is the best."
    son "Well obviously."
    jojo "Then why did you tell them to use C++?"
    son "I just like creating conflict."
    son "Marijuana is considered a stress reliever."
    son "Create stress and you can increase sales!"
    jojo "Do you ever worry that might be manipulative?"
    son "I learned the Jew's game. It's the only way a business can survive in this god-eat-god world."
    jojo "That makes a lot of sense. Well, you may have created more stress than you prepared for. They look violent."
    son "Oh come on. They are computer programmers. What are they going to do, code spam-bots?"
    jojo "More like aim machine guns at each other and open fire."
    son "That seems unlikely."
    jojo "Typically, if an event is currently happening, it means it's probability is 100 percent."
    john "for(int i = 0; i < 10; i--) openFire()!"
    te "while(true) openFire()!"
    jeff "I don't know how to code, but I have a knife!"
    son "This hardly seems friendly."
    jojo "I think you may have started a war."
    son "Yeah, sorry. It's a difficult habit to break. I wonder what would happen if they were on acid..."
    jojo "Trap trips."
    son "Anyways, you should probably fix this war. Otherwise, your lovers might die."
    jojo "You aren't going to do anything to help, are you?"
    son "Want some weed?"
    jojo "Later. I have business to attend to. That business is killing."
    "Dang. Okay, who do I help?"
    menu:
        "Help John":
            jump WarJohn
        "Help Teddy":
            jump WarTeddy
        "Help Jeff":
            jump WarJeff


label end_credits:

    "End."

    return

#label search:  #just in case you want example on how to do more imagemap-driven events.
#    $ day += 10
#
#    $ period = "search"
#
#    call screen city_map
#
#    if _return == "apoth":
#        $ act = "apoth"
#    
#    elif _return == "play":
#        $ act = "play"
#
#    elif _return == "school":
#        $ act = "school"
#
#    elif _return == "zoo":
#        $ act = "zoo"



label JackIntro:
    "I approach the military base."
    "I desperately look for women to flirt with, but find myself trapped in a field of sausage."
    ja "You know, I'm pretty sure it's illegal for civilians to be here."
    jojo "Hmm? No I'm a..."
    jojo "Totally a soldier. Trust me."
    ja "Yea, no. Not even for a second."
    jojo "Hey, wait, come back!"
    return
    
label HalloweenJack:
    jojo "Hey Jack, how are you doing?"
    ja "Oh, hey Joseph. You came dressed as... an XCOM Alien?"
    jojo "Do you like it?"
    ja "Sure? You kind of just look like a generic alien."
    ja "Original enemies weren't really the selling point of that game."
    jojo "But I did it just for you!"
    ja "What? You know, I already have a girlfriend..."
    jojo "Wait, what?"
    ja "Yea. Actually, we are getting married in a few weeks."
    jojo "Oh... congratulations?"
    ja "Yep. Oh hey, she's here now. Godsta go, son."
    "Damn, jealousy is a foreign emotion."
    "Being the flirtatious man I am, I'm so used to being able to get anyone I want..."
    "Seeing Jack denied from me makes me feel horrible..."
    jojo "No... I will not let her win."
    jojo "He doesn't love me because there is someone else in his life."
    jojo "I just have to get rid of her!"

    jump SonjaThreeJack

    return
    
label SonjaThreeJack:
    "I need Sonja's help."
    son "Hey JoJo. You came back pretty quickly. How's the whole bomb thing going?"
    jojo "It might be bad for business if you scream that near the customers."
    son "They are stoned off their ass anyways. They won't hear a thing."
    jojo "It hasn't been going great."
    jojo "I met someone named Jack."
    jojo "He was on your map but..."
    jojo "He already has a girlfriend."
    son "Oh right. Sorry. My Trap Map doesn't get updated often."
    jojo "Why do you have that anyways?"
    son "They tend to be the easiest to manipulate."
    jojo "Hmm, alright. Anyways, I hate the feeling of being shot down."
    jojo "I am Joseph Joestar!"
    jojo "The only reason I lose a fight is because I want to extend my episode's runtime!"
    jojo "I will not let this girl beat me"
    jojo "How do I... remove her?"
    son "I have a collection of knives just for this occasion."
    jojo "I believe there is a social expectation to be at least a little concerned about what I just said."
    son "Sure. There is also a social expectation not to have a collection of knives."
    son "Are we really going to worry about what is expected of us when you are considering murder for the sake of suicide bombing?"
    jojo "Fair point. Anyways, give me that knife. I am going to go... solve problems."
    son "Good luck JoJo!"
    "I leave the store, but I still hear what she is saying."
    son "Shit... Jack's girlfriend in the military too..."
    son "This can't possibly go well for Joseph."
    son "It sure will be funny to watch though."

    jump JackFinale

    return

label JackFinale:
    "I return to the military base. It's ladies night, so Jack and all the other males are gone."
    "I'm pretty sure that's not how this thing works, but whatever."
    "Aha! There she is. Now I just need to sneak up behind her."
    "I sit and wait, gathering my will."
    "If I don't kill her now, I will explode on the spot."
    "I can't let her make me fail my mission."
    "I have to strike fast."
    "My thoughts match the racing pace of my heart."
    "I know that this is the right thing for me."
    "With my heart moving this fast, there is no risk of the bomb ever going off."
    jg "What are you doing!?!?"
    jojo "Uh... um..."
    "Shit, I've been caught. I must strike!"
    "I leap forward, knife in hand. I aim straight for the neck in an attempt to take out the jugular." #jesus fucking christ all the misspellings in this sentence I had to fix... GOD
    "And I succeed in doing fuck all."
    "Jack's girlfriend manages to tackle me to the ground and disarm me."
    "She runs off with the knife to look for help."
    "Failing to kill my target, I can feel my heart sink." # "Having had failed to kill his target, I can feel heart sink"
    "Heart... sink...?"
    "SHIIIIIIIII{size=-10}IIIIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIIIIIIII{size=-10}IIIIIIIIIIIII{size=-10}IIIIIIIIIIIIIIIIII{size=-10}IIIIIIT!{/size}{/size}{/size}{/size}{/size}{/size}{/size}{/size}{/size}{/size}{/size}"

    jump badEnd

    return





label goodEnd:
    son "Testing if I get to here"
    $ renpy.movie_cutscene("FinalCutscene.mp4")
    son "Testing if I get to here"
    return

label badEnd:
    son "Bad End."
    return