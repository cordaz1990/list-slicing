"""Functions that manipulate lists without using Python's built-in list methods.

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations.
They include:

    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

Implement functions that each use just one of the above operations.

The docstring of each function describes what it should do.

DO NOT USE ANY OF THE BUILT IN LIST METHODS, OR len()!
"""


def head(input_list):

	
    return input_list[0]

print(head(['jan','feb',"mar"]))


def tail(input_list):
    return input_list[1:]

print(tail(['jan','feb','mar']))

def last(input_list):
    
    return input_list[-1]

print(last(['jan','feb','mar']))


def init(input_list):
    

    return input_list[:2]

print(init(['jan','feb','mar']))


# ##############################################################################
# Do yourself a favor and get a short code review here.

def first_three(input_list):
    

    return input_list[:3]

print(first_three(['jan','feb','mar','apr','may']))

def last_five(input_list):
   

    return input_list[5:]

print(last_five([0,3,6,9,12,15,18,21,24,27]))


def middle(input_list):
    
    
    return input_list[2:8]

print(middle([0,3,6,9,12,15,18,21,24,27]))

def inner_four(input_list):
   
   
    return input_list[2:6]

print(inner_four([0,3,6,12,15,18,21,24,27]))

def inner_four_end(input_list):
   
    return input_list[4:8]

print(inner_four_end([0,3,6,9,12,15,18,21,24,27]))


def replace_head(input_list):
    """Replace the head of input_list with the value 42 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

    """
    input_list[0]= 42
    return input_list
   
    
print(replace_head([0,3,5,12,15,21,19]))

def replace_third_and_last(input_list):
    
    input_list[2] = 37
    input_list[-1]= 37
    return input_list

print(replace_third_and_last([0,3,6,9,12,15,18,21,24,27]))


def replace_middle(input_list):
    """Replace all elements of a list but the first and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples == [0, 3, 42, 37, 24, 27]
    True

    """

print()


# def delete_third_and_seventh(input_list):
#     """Remove third and seventh elements of input_list and return nothing.

#     For example:

#     >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#     >>> delete_third_and_seventh(notes)
#     >>> notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Do']
#     True

#     """

#     pass


# def delete_middle(input_list):
#     """Remove all elements from input_list except the first two and last two.

#     Return nothing.

#     For example:

#     >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#     >>> delete_middle(notes)
#     >>> notes == ['Do', 'Re', 'Ti', 'Do']
#     True

#     """

#     pass


# ##############################################################################
# # END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
# #
# # Please ask for a code review from an Education team member before proceeding.
# ##############################################################################

# # This is the part were we actually run the doctests.

# if __name__ == "__main__":
#     import doctest

#     result = doctest.testmod()
#     if result.failed == 0:
#         print("ALL TESTS PASSED")
