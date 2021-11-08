VOWELS = set("aeiou")
def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """


    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            # get(lts,0) => returns 0 if ltr isn't in counter yet (allows function to run without an error)
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter

    # return {
    #     "a": phrase.lower().count('a'),
    #     "e": phrase.lower().count('e'),
    #     "i": phrase.lower().count('i'),
    #     "o": phrase.lower().count('o'),
    #     "u": phrase.lower().count('u')
    #     }