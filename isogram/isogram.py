def is_isogram(string):
    # Turn ths string into a list so that we can iterate over it
    listed = list(string.lower())

    # initializing a dictionary, against which we can check if a character has been seen before. Try to keep to O(n) time.
    lookup = dict()
    
    # iterate over all elements in the string-list
    for char in listed:
        # if a character is a alphanumeric we test to see if it's in the dict...
        if char.isalpha() == True:

            if char in lookup:
                # We've already seen this character before. NOT AN ISOGRAM. Return false.
                return False
            else:
                # We haven't seen an repeated character yet. Add this new character to the dict and proceed. 
                lookup[char] = True

        # ... if it's not alphanumeric (i.e. a number, a whitespace, punctuation) we skip it as we don't use these characters as a test of isogram
        else:
            continue

    # We made it to the end of the list-string without seeing a repeated character. IT IS AN ISOGRAM    
    return True
