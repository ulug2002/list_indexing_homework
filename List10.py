def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    a = max (list_num[0], list_num[-1])
    return a

print(main([9, 32, 1, 4, 3]))