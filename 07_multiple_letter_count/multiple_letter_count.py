def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    keys = set(phrase)
    dict_count = {}
    for k in keys:
        dict_count[k] = phrase.lower().count(k)
    return dict_count