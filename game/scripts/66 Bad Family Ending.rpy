label badFamilyEnding:

    show mom sad2 with dissolve
    play sound honk

    "She looks at us for a long while, the taxi honking a second time."

    show mom sad1 with dissolve

    voice "20-3-1.mp3" #kaito
    mom "I'm sorry."
    
    hide mom with dissolve

    voice "20-3-2.mp3" #potato
    pro "No, wait-"

    "I try to protest, but she's already left. Through the open door, I watch her put the bags in the taxi, and ride off."
    "The taxi crests the hill, and it's gone."

    show sis cry with dissolve

    voice "20-3-3.mp3" #amree
    sis "Please…"

    "It all happened so fast. She's gone, isn't she?"
    "Is this the last time that we'll ever see her?"
    "Will her last words to me really be 'I'm sorry'?"
    
    hide sis with dissolve    
    
    "Our family sits in silence, frozen still. We don't dare to move."

    show bro sad2 with dissolve

    voice "20-3-4.mp3" #kujira
    bro "Well… do we go after her?"

    show black with Dissolve(5.0)

    jump composite_future1

    ###########################################

label badFamilyEnding_future:

    if career < 8:
        "I sometimes think about the day Mom left."
    else:
        "The long awaited holiday is finally here, and I've come home to see my family."
        "Whenever I come home, I think about the day Mom left."
    
    "I remember how Alex words lingered in the air, and I remember waiting for the response that never came."
    "She never came back home, and since then we haven't heard a single word from her."
    "We could have filed a missing person's report, or phoned the taxi company, but in the end we were too tired of it all to really give it any effort."

    play sound knock
    pause 1.0
    play sound opendoor
    pause 1.0

    voice "20-3-5.mp3" #kujira
    bro "Hey, sis, it's time for dinner."

    scene bedroom with Dissolve(2.0)

    voice "20-3-6.mp3" #potato
    pro "R-right, I'll be right there."

    show bro sad2 with dissolve

    "My brother places a hand on my shoulder with a soft, reassuring squeeze before leaving my room."
    
    hide bro with dissolve
    
    "It's been tough, without Mom. Better, in some ways… but you can never really know if this 'better' is better than the alternative."
    "This doubt's been killing me lately."
    "Could I have done anything? Could I have stopped her?"
    "If so, why didn't I?"

    play sound fabric

    "I crawl out of bed, rubbing my eyes drowsily. It's over. No sense thinking about it."
    "Time to eat, then."

    scene hallway with dissolve
    play sound slamdoor

    "I can smell the food from the kitchen. It… it's some sort of meat? Bacon, probably. Eggs, too. Smells like we're having breakfast for dinner again."
    "I don't mind, it's something simple that my dad hopefully won't mess up."

    scene livingroom with dissolve   

    "Following the smell, I walk into the dining room to spot my dad and sister setting the table together."
    "My sister brings out the food, and my dad sets the plates."
    "I take my place at my normal spot, next to my sister's chair."
    "Alex sits across from us, lazily scribbling in a textbook, looking like he just woke up himself."

    show dad sad2 with dissolve

    voice "20-3-7.mp3" #lacTheWatcher
    dad "Sorry if the food's not so great, I'm still getting the hang of it…"

    voice "20-3-8.mp3" #potato
    pro "Yeah, it's okay dad. It'll be fine, I'm sure."

    show dad neutral1 with dissolve

    "I give him a weak smile, hoping that he's recovering better than we are."

    hide dad with dissolve

    "He reaches over, handing me a set of plates. I set one in front of myself, one in front of Maria's chair, and I give the last to Alex."
    "Looking next to me, I see a plate set aside with a small meal in front of an empty chair."
    "My mom's chair."
    "Grabbing it, I wave over Dad."

    show dad neutral1 with dissolve

    voice "20-3-9.mp3" #potato
    pro "You set an extra."

    show dad sad2 with dissolve

    "He looks at me with confusion on his face before he realizes."

    show dad sad1 with dissolve

    voice "20-3-10.mp3" #lacTheWatcher
    dad "Oh, right."

    show dad neutral with dissolve

    "He closes his eyes, shaking his head slightly. His expression is pained, tired."

    show dad sad1 with dissolve

    voice "20-3-11.mp3" #lacTheWatcher
    dad "You're completely right."

    hide dad with dissolve

    "He takes Mom's plate, putting the food on his own and putting hers in the sink."
    "Everyone takes a seat at the table, just like old times. We eat in silence, with only the odd awkward smalltalk filling the air."
    "The food’s pretty bland, and there are some eggshells left in. I still eat it without complaint, however."
    "Everyone's doing the best that they can."
    if love < 8:
        "My mind wanders over to the time Lauren cooked dinner for us."
    else:
        "Fortunately for us, Lauren sometimes helps Dad with the cooking."

    show sis sad1 with dissolve

    voice "20-3-12.mp3" #amree
    sis "So…"

    "Looking over to Maria, she's picking at her food, hardly any of it being eaten yet."

    show sis sad2 with dissolve

    voice "20-3-13.mp3" #amree
    sis "Do you think Mom will ever come home?"

    #Abrupt scene end
    show black with Dissolve(2.0)
    jump composite_future3
