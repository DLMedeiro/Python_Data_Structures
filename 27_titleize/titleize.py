def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    split_phrase = phrase.lower().split(" ")
    # ['this', 'is', 'awesome']

    updated = [word[0].upper() + word[1::] for word in split_phrase]
    
    return " ".join(updated)
