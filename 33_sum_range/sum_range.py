def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    answer = 0 
    count = 0
    if end == None:
        end = 0
    if end == 0 and start==0:
        for n in nums:
            answer += n    
    else: 
        if count == end:
            for n in nums: 
                try:
                    answer += nums[start+count]
                    count += 1
                except IndexError:
                    return answer
        else:
            for n in nums:
                try: 
                    if count+start <= end:
                        answer += nums[start+count] 
                        count += 1   
                except IndexError: 
                    return answer        
    return answer