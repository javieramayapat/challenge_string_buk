"""
Create a function that transforms the first letter of a
of a phrase to lowercase and the other letters to uppercase.

Example: this is an example
result = tHIS iS aN eXAMPLE
"""


def tranform_string(phrase):
    if type(phrase) not in [str]:
        raise TypeError("The phrase must be a string.")

    if len(phrase) < 1:
        raise ValueError("The phrase length must contain at least 1 character")

    upper_phrase = phrase.upper()

    list_of_upper_phrases = upper_phrase.split()

    final_list = [phrase[0].lower() + phrase[1:] for phrase in list_of_upper_phrases]

    final_phrase = " ".join(final_list)

    return final_phrase
