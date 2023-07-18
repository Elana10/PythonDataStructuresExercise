def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """ 
    answer = list(s)
    index = 0
    index_swap = 0
    lst_index = []
    lst_char = []
    for char in s: 
        for v in 'aeiou':
            if char == v:
                lst_index.append(index)
                lst_char.append(char)
        index += 1
    lst_index.reverse();
    for i in lst_index:
        answer[i] = lst_char[index_swap]
        index_swap +=1
    
    return "".join(answer)
    