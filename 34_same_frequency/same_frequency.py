def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num1 = list(num1)
    num1.sort()

    num2 = str(num2)
    num2 = list(num2)
    num2.sort()
    
    if num1 == num2:
        return True
    return False