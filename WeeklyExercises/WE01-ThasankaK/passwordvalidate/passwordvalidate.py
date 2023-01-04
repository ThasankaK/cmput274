# PASSWORD VALIDATOR TEMPLATE: REPLACE THIS LINE WITH YOUR FILE HEADER


def validate(password):
    # defines a function called validate, which has a input called password. It's main goal is to decide whether a given password is Invalid,Secure
    # or Insecure 
    forbidden = ' @#'  
    specials = '!-$%&’()*+,./:;<=>?_[]^‘{|}~'

    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters
    
    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """
    
    if (len(password) < 8) or (any((letter in forbidden) for letter in password)):
        # If the length of the password is less than 8 OR 
        # if a letter in the forbidden string is a letter in password, then the statement continues
        # note: 'letter' could be any other word like 'a'. It is a placeholder which states that 'a' will be the values
        # in forbidden, then it checks if the values in 'a' are in password and produces True or False.
        return("Invalid")
    elif (any((lett1.isupper()) for lett1 in password)) and (any((lett2.islower()) for lett2 in password)) and (any((num.isdigit()) for num in password)) and (any((specialschars in specials) for specialschars in password)):
        # lett1 is a capital, and it uses lett1 to check if there is a capital in password
        # lett2 is a lowercase letter, and it uses lett2 to check if there is a lowercase.
        # num is a digit, and using num it checks if there is a digit in password
        # a word is given the values inside the 'specials' variable and then using the word, it checks if the value
        # are in password 
        return("Secure")
    else:
        return("Insecure") 
def generaten(n):
    import random 
    import string # these two commands call in two modules from the python library
    letters = string.ascii_letters + string.digits + '!-$%&’()*+,./:;<=>?_[]^‘{|}~' 
    # In the string module, there exists a constant called ascii_letters which returns a string of letters a-z both 
    # lowercase and uppercase. 
    # There also exists a constant called digits which returns a string of the numbers 0-9.
    # When used together, along with the string of special characters, the variable 'letter' becomes a long string
    # of a-z,A-Z,0-9 

    return ( ''.join(random.choice(letters) for i in range(n)) )
    # starts the statement with a blank string, then joins that string with random characters in the string 'letters'. It keeps adding
    # on letters for every i in range n. E.G: if n was 9 it would loop 9 times, therefore add 9 characters.

""" 
Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
pass
if __name__ == "__main_":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    pass 
