def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> v
        1
    """
    multiple = 1
    for n in nums: 
        if n % 2 == 0:
            multiple *= n
        
    else: 
        return multiple