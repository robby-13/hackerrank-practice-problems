'''
Check if a given string is a pangram - a sentence that contains every letter in the alphabet
'''

def is_pangram(s):
    # create a list that will store letters, the program tests the string to make sure 
    # each letter in the string only appears once in the array
    letters = []
    # make the string lowercase to make it easier to test
    s = s.lower()
    # loop through the string
    for i in s:
        # test each character's ASCII value and make sure 1.) it falls under the parameters of lowercase letters
        # and 2.) make sure it does not appear in the letters array already
        if (ord(i) >= 97 and ord(i) <= 122) and i not in letters:
            # if it does not, add it to the list
            letters.append(i)
    # if the length of letters is 26 then we have a pangram :)
    if len(letters) == 26:
        return True
    # otherwise it is not
    return False
