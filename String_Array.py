def create_array(string):
    """
    This function takes a string as input and returns an array of the words in the string.
    Example:
        create_array("This is a sentence") --> ["This", "is", "a", "sentence"]

    Parameters:
        string == a string data type

    Algorithm:
        Split string into separate words --> array[]
        Return array
    """

    array = string.split(" ")

    return array

