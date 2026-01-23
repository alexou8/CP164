"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-11-15"
-------------------------------------------------------
"""
# Imports
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # your code here
    
    for line in file_variable:
        for char in line:
            if char.isalpha():  
                letter = Letter(char.upper()) 
                retrieved = bst.retrieve(letter) 
                if retrieved is None:
                    print(f"Failure... Unable to find {char.upper()}")

    return

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    
    total = 0  

    for letter in bst.inorder():
        total += letter.comparisons

    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    
    total_count = sum(letter.count for letter in bst.inorder())

    print("Letter Count/Percent Table")
    print(f"\nTotal Count: {total_count:,}")
    print("\nLetter  Count       %")
    print("---------------------")

    for letter in bst.inorder():
        percent = (letter.count / total_count) * 100 if total_count > 0 else 0
        print(f"    {letter.letter}  {letter.count:6,}   {percent:5.2f}%")

    return

