"""
*** SIMPLE PIG LATIN ***
This is a project I resolved in codewars.com
---------------------------------------------

Instructions:
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched. Examples
 pig_it('Pig latin is cool') # igPay atinlay siay oolcay
 pig_it('Hello world !')     # elloHay orldway !"""

# I applied list comprehension, using an if/else statement validation, then
# formatted the entries (words) to the list as strings in which first letter
# of every word was move to the end of the word, then adding "ay".
# The resulting list was joined, separating entries with space " "".

#Test for GitHub purposes...
def pig_it(text):
    return " ".join([(f"{word[1:]}{word[0]}ay") if word.isalnum() else word for word in text.split(" ")])


# Testing my solution...
print(pig_it('Hello world !'))
