from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_noun():
    # 1. Test the single determiners.

    single_nouns = ['car', 'gull', 'rat', 'ant', 'rock', 'tomato', 'fish', 'king']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural determiners.

    plural_nouns = ['cars', 'gulls', 'rats', 'ants', 'rocks', 'tomatoes', 'fish', 'kings']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])