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
        noun = ['car', 'gull', 'rat', 'ant', 'rock', 'tomato', 'fish', 'king']
    else:
         noun = ['cars', 'gulls', 'rats', 'ants', 'rocks', 'tomatoes', 'fish', 'kings']

    noun = random.choice(noun)
    return noun

def get_verb(quantity, tense):

    tense = ['past', 'present', 'future']
    tense = random.choice(tense)

    if tense == 'past':
        verb = ['danced', 'swam', 'died', 'fought', 'shook', 'screamed', 'sank', 'returned']
    elif tense == 'present' and quantity == 1:
        verb = ['dances', 'swims', 'dies', 'fights', 'shakes', 'screams', 'sinks', 'returns']
    elif tense == 'present' and quantity != 1:
        verb = ['dance', 'swim', 'die', 'fight', 'scake', 'scream', 'sink', 'return']
    elif tense == 'future':
        verb = ['will dance', 'will swim', 'will die', 'will fight', 'will shake','will scream', 'will sink', 'will return']
    
    verb = random.choice(verb)
    return verb

quantity = [1,2]
quantity = random.choice(quantity)

get_determiner(quantity)