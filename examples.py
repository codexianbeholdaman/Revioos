from parsers import *

### Check validity
res = post_processing("""
First revioo
=====
TITLE: Blackguards
REVIEW:
                    Blackguards, based on 'das Schwarze Auge' ruleset, is a game focused on combat, and all its other elements are subservient: lightning-fast exploration is reminiscent of a puzzle game without puzzles, dialogues are straight and forward (usually towards the battle), and audiovisuals are best described as utilitarian.

                    As expected, the combat system is splendid. The game featured myriads of ways to develop characters, especially mages, ranging from giving them the ability to resist knockdowns or get enemies' stats to creating impenetrable walls or showering seven adjacent fields with arrows. There were no level-ups; every skirmish gave a certain amount of experience points, which can be used to buy abilities directly - what follows, the game features a strong sense of progression, as one can reinforce some characters before any string of fights. Different types of weapons offered different sets of properties (such as range or added abilities), unique items didn't become commonplace as the game progressed. Each encounter is handcrafted; the game didn't lose its grip even at the very end, as each of its five chapters provided quite a few memorable challenges with diverse enemies and interactive environments. Understanding the battlefield was oftentimes more important than knowledge of the combat system, as a lot of maps featured unique traps or constraints requiring tailored strategies.

                    The game had some hiccups, though: despite being combat-focused, the party is determined by the plot rather than by a player - which is a shame, as a lot of the encounters begged for testing them with a different party setup. Very few choices had actual consequences; while it's nice that the game doesn't reward do-gooders with unrealistic benefits, the game feels very linear most of the time. Both of those things limit replayability.

RATING: 6.5
TAGS: ['combat-focused', 'environmental interaction']
RPG: true
=====
and then,
=====
TITLE: Some title
REVIEW: Meh
RATING: 5.12312312
TAGS: []
HE: hehe
NOTES: xxxxx
=====
=====
TITLE: yes
=====
""")

for x in res:
    _ = [print(f'{key}: {x[key]}') for key in x],
    print()
