def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))
    """
    This function returns a dict made from two lists.
    """


def merge_two_dicts(d1, d2):
    return d1|d2

    # return {**d1, **d2}
    """
    Merge two Python dictionaries into one
    """


def init_dict_with_values(lst, d1):
    return {key: d1 for key in lst}


    """
    Create a dict with default values for each key listed.
    """
    pass


def extract_keys_to_dict(datadict, keylist):
    final_dict = {element: datadict[element] for element in keylist}
    return final_dict
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """



def delete_keys_from_dict(datadict, keylist):
    for element in keylist:
        datadict.pop(element)
    return datadict
    """
    Delete a list of keys from a dictionary
    """
    # return {i: datadict[i] for i in datadict if i not in keylist}


def check_dict_for_key(datadict, value):
    return value in datadict.values()
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """


def get_key_of_min_value(ddd):
    mini = min(ddd.values())
    keymin = 0
    for key in ddd:
        if ddd[key] == mini:
            keymin = key
    return keymin

    # return min(ddd, key=ddd.get)

    """
    Get the key of the minimum value from a dictionary
    """


def get_key_of_max_value(ddd):
    maxi = max(ddd.values())
    keymax = 0
    for key in ddd:
        if ddd[key] == maxi:
            keymax = key
    return keymax

    # return max(ddd, key=ddd.get)
    """
    Get the key of the maximum value from a dictionary
    """