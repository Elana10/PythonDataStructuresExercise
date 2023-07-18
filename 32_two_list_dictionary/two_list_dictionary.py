def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    count = 0
    new_dictionary = {}
    if len(keys) == len(values) or len(keys) < len(values):
        for k in keys:
            new_dictionary[keys[count]] = values[count]
            count += 1
    else:
        for k in keys:
            try: 
                new_dictionary[keys[count]] = values[count]
                count += 1
            except IndexError:
                new_dictionary[keys[count]] = None
                count += 1
        
    return new_dictionary
