def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a = len(list1)*[list1[0]]==list1

    return a
    
print(main([0,0,0,0,0,0,0,0,0,1,0]))