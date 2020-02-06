import string

# Create a Python module, which consists of a class TextContainer. The class shall implement methods for computing statistics on texts.
# 1. Counting the amount of words used in a text.
# 2. Counting the amount of chars used in a text.
# 3. Counting the amount of letters, where letters are all ASCII characters, see

# import string
# string.ascii_letters  # returns 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 4. Remove all punctuation characters, see
# import string
# string.punctuation  # returns '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


class TextContainer():
    def __init__(self, text):
        self.text = text

    def amountWords(self):
        counter = 1
        for x in self.text:
            if (x == " "):
                counter += 1

        return counter

    def amountChars(self):
        counter = 0
        for x in self.text:
            if (x != " "):
                counter += 1
        return counter

    def ascii(self):
        counter = 0
        for x in self.text:
            if x in string.ascii_letters:
                counter += 1
        return counter

    def removePunctuation(self):
        myString = ""
        for x in self.text:
            if x not in string.punctuation:
                myString += x
        return myString

# TESTING BELOW:


test = TextContainer("tes!t tes(t tes$t []tes^^t")

print("amount of words: " + str(test.amountWords()))
print("amount of chars: " + str(test.amountChars()))
print("amount of ascii: " + str(test.ascii()))
print("String with punctuation removed: "+test.removePunctuation())
