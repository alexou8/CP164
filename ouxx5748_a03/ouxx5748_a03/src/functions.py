"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:      169025748
Email:   ouxx5748@mylaurier.ca
__updated__ = "2024-09-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    
    target = Stack()
    index = 1

    while (not source1.is_empty()) or (not source2.is_empty()):
        if (index % 2 == 0) and (not source2.is_empty()) or source1.is_empty():
            value = source2.pop()
            target.push(value)
        else:
            value = source1.pop()
            target.push(value)

        index += 1

    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    array = []

    while not source.is_empty():
        value = source.pop()
        array.insert(0, value)

    for index in range(len(array) - 1, -1, -1):
        value = array.pop(index)
        source.push(value)

    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    palindrome = True
    stack = Stack()
    reverse_index = len(string) - 1
    index = 0
    add = True
    
    while index < len(string) and reverse_index > 0 and palindrome:
        if string[index].isalpha() and add:
            stack.push(string[index].lower())
        elif string[reverse_index].isalpha() and add:
            reverse_index += 1
        else:
            add = True
        if reverse_index < len(string):
            if string[reverse_index].isalpha():
                if (not stack.is_empty()):
                    if string[reverse_index].lower() != stack.pop():
                        palindrome = False
            elif string[index].isalpha():
                add = False
                index -= 1
                
        reverse_index -= 1
        index += 1
        
    return palindrome

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """

    stack = Stack()
    paths = Stack()
      
    stack.push('Start')
    paths.push([])  
    path = None

    while not stack.is_empty():
        cur = stack.pop()
        cur_path = paths.pop()
        if cur == 'X':
            path = cur_path + ['X']
            break
        opts = maze.get(cur, [])
        for opt in opts:
            stack.push(opt)
            if cur != 'Start':     
                paths.push(cur_path + [cur])
            else:
                paths.push(cur_path)

    return path  

    
# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    stack = Stack()
    mirror = MIRRORED.IS_MIRRORED
    
    split = string.split(m)
    
    for char in string:
        if char != m and char not in valid_chars:
            mirror = MIRRORED.INVALID_CHAR
            break
    
    if len(split) != 2:
        mirror =  MIRRORED.NOT_MIRRORED
    else:
        left, right = split 
        if len(left) > len(right):
            mirror =  MIRRORED.TOO_MANY_LEFT
        elif len(left) < len(right):
            mirror =  MIRRORED.TOO_MANY_RIGHT
        else:
            for char in left:
                stack.push(char)              
            for char in right:
                if stack.is_empty() or stack.pop() != char:
                    mirror =  MIRRORED.MISMATCHED

    return mirror
