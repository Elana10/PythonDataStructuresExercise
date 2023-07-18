def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    updated_phrase = ''
    for ltr in phrase:
        if ltr == to_swap:
            new_ltr = ltr.swapcase()
        elif ltr.swapcase() == to_swap:
            new_ltr = ltr.swapcase()
        else:
            new_ltr = ltr
        updated_phrase += new_ltr
    return updated_phrase