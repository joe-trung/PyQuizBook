from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    return list(t)
    """
    This function takes a tuple of elements and returns a list containing those elements of the tuple.
    """


def drop_last(lst):
    return lst[:len(lst) - 1]
    """
    This function takes a list and returns a list with the last item removed.
    """


def drop_first_two(lst):
    return lst[2:]
    """
    This function takes a list and returns a list with the first two items removed.
    """


def drop_mangle(lst):
    return lst[2:len(lst) - 1]
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """


def add_item_front(lst, a):
    lst.insert(0, a)
    return lst
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """


def add_item_end(lst, a):
    lst.append(a)
    return lst
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """


def add_list_to_list(lsta, lstb):
    return lsta + lstb
    """
    This function takes two lists and appends one to the other,
    returning a list
    """


def list_and_list_to_tuple(lsta, lstb):
    return (lsta, lstb)
    """
    This function takes two lists and returns a tuple containing the two lists
    """


def list_and_list_to_list(lsta, lstb):
    return [lsta, lstb]
    """
    This function takes two lists and returns a list containing the two lists
    """


##
##
##

def list_from_range(n):
    return [i for i in range(n)]

    """
    This function returns list with 0..n as integers in a list
    """


def list_from_range2(n, m):
    return [i for i in range(n, m)]
    """
    This function returns list with n..m (without m) as integers in a list
    """


def list_from_range3(n, m):
    return list(range(n, m + 1))
    """
    This function returns list with n..m (including m(!)) as integers in a list
    """


def list_from_range4(n, m):
    return [i for i in range(n + 1, m + 1)]
    """
    This function returns list with n..m (WITHOUT n and including m) as integers in a list
    """


def list_from_range_by(n, step):
    return list(range(0, n, step))
    """
    This function returns list with 0..n as integers by step in a list
    (read the test)
    """


def rev_list(lst):
    return lst[::-1]
    """
    This function returns list which is a reverse of the argument list
    (read the test)
    """


def concat_list_indexwise(lst1, lst2):
    if len(lst2) >= len(lst1):
        for i in range(len(lst1)):
            lst2[i] = lst1[i] + lst2[i]
        return lst2
    else:
        for i in range(len(lst2)):
            lst1[i] += lst2[i]
        return lst1

    """
    Write a program to add two lists index-wise. 
    Create a new list that contains the 0th index item from both the list, 
    then the 1st index item, and so on till the last element. 
    Any leftover items will get added at the end of the new list.
    """


def square_each_item(lst):
    return [i * i for i in lst]
    """
    This function returns list which each item in argument list has been squared
    (read the test)
    """


def remove_empty_strs(lst):
    return [i for i in lst if i != '']
    """
     Remove empty strings from the list of strings
     """
    pass


def remove_item_from(lst, aaa):
    return [i for i in lst if i != aaa]
    """
    Remove all occurrences of a specific item from a list.
    """



def leave_item_in(lst, aaa):
    return [i for i in lst if i == aaa]
    """
    Leave all occurrences of a specific item in a list.
    """



def length_of(lst):
    return len(lst)
    """
    return the length of the list
    """

