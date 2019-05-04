def create_array(string):
    """
    This function takes a string as input and returns an array of the words in the string.
    Example:
        create_array("This is a sentence") --> ["This", "is", "a", "sentence"]

    Parameters:
        string == a string data type

    Algorithm:
        -Check the data type of string
        -If string's data type is a "string" then:
            Split string into separate words --> array[]
            Return array
        Else:
            generate error message
            return error message
    """

    # Check the data type as a string. If yes, returns bool true --> is_string. If no, returns bool false --> is_string
    is_string = type(string) is str

    # Begin logic
    if is_string:
        array = string.split(" ")
        return array
    else:
        error_message = "Argument must be of data type 'string'"
        return error_message


print(create_array("This is a string"))
