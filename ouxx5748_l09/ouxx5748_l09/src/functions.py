"""
-------------------------------------------------------
Lab 9, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-14"
-------------------------------------------------------
"""
# Imports

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    
    '''
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- --------------------")

    for value in values:
        crypt = sum(ord(c) for c in value.name)
        slot = crypt % slots
        print(f"{crypt:>8} {slot:>4} {value.name}, {value.origin}")

    return
    '''
    
    print("Hashes")
    print("Hash     Slot Key")
    print("-------- ---- --------------------")

    for value in values:
        crypt = hash(value)  # Uses the custom __hash__ method
        slot = crypt % slots
        print(f"{crypt:>8} {slot:>4} {value.key()}")

    return