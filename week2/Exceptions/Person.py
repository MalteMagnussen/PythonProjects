# 1. Create a class called: Person with a constructor that takes a string: name.

# 2. Check if name contains only letters and each new word starts with a capital letter.
#    If this is not the case raise an InvalidArgumentException (your own exception here)

# 3. Test you new class by making 2 instances
#    (one with a name, that follows the rules and another that violates them)

import string

# Custom Exception


class InvalidArgumentException(ValueError):

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


class Person():
    """arg: name = String"""

    def __init__(self, name):

        for index, x in enumerate(name):
            if x != " ":
                if x not in string.ascii_letters:
                    raise InvalidArgumentException(
                        "Name must only contain letters or spaces.")
            if index == 0 and not x.isupper():
                raise InvalidArgumentException(
                    "Words must begin with a capitalized letter.")
            if index > 0 and name[index-1] == " " and not x.isupper():
                raise InvalidArgumentException(
                    "Words must begin with a capitalized letter.")

        self.name = name


rightPerson = Person("Niels Jensen")
wrongPerson = Person("johnson $$$")
wrongPerson2 = Person("Johnson D$$$$")
