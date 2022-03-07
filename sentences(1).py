import random
from unittest.mock import call
def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    
    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity ==1:
        nouns = ['car', 'gull', 'rat', 'ant', 'rock', 'tomato', 'fish', 'king']
    else:
         nouns = ['cars', 'gulls', 'rats', 'ants', 'rocks', 'tomatoes', 'fish', 'kings']

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):

    tense = ['past', 'present', 'future']
    tense = random.choice(tense)

    if tense == 'past':
        verbs = ['danced', 'swam', 'died', 'fought', 'shook', 'screamed', 'sank', 'returned']
    elif tense == 'present' and quantity == 1:
        verbs = ['dances', 'swims', 'dies', 'fights', 'shakes', 'screams', 'sinks', 'returns']
    elif tense == 'present' and quantity != 1:
        verbs = ['dance', 'swim', 'die', 'fight', 'scake', 'scream', 'sink', 'return']
    elif tense == 'future':
        verbs = ['will dance', 'will swim', 'will die', 'will fight', 'will shake','will scream', 'will sink', 'will return']
    
    verb = random.choice(verbs)
    return verb

def get_preposition():

    preps = ['for', 'above', 'under', 'before', 'after', 'by']

    prep = random.choice(preps)
    return prep

def get_prepositional_phrase(quantity):

    phrase = get_preposition; get_determiner; get_noun

    return phrase