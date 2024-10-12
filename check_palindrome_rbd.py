"""
MODULE:           check_palindrome_rbd.py   
used by PROJECT:  Palindrome.py
DESCRIPTION:  clean prints original phrase, 
                      then (on next line) the cleaned up phrase
       - the only punctuation the function has to remove are what's in these
           test cases, so that's : , . - ? and spaces
 use_index uses a loop to compare characters, where index1 starts at 0 and
       index2 starts at the end
       - each time around the loop, index1 increments, index2 decrements
       
 use_index - check if it's a palindrome or not & print result
AUTHOR:
"""
# You must use a for loop to implement clean()
# You may NOT use a continue or break
def clean(phrase):
    print(phrase)
    phrase = phrase.lower()
    bad_puc = " :,.-?"
    for p in bad_puc:
          if p in phrase:
                phrase = phrase.replace(p, '')
    print(phrase)
    return phrase



# Implement with a while loop
# You may use a break
def use_index_while(phrase):
    palindrome = True
    i = 0
    j = len(phrase) - 1
    while (i < len(phrase)) and (j > -1) and palindrome:
        if phrase[i] != phrase[j]:
            palindrome = False
            #break 
        i = i + 1
        j = j - 1

    if palindrome:
        print('Palindrome')
    else:
        print('Not a palendrome.')

# Implement with a for loop
def use_index_for(phrase):
    palindrome = True
    j = len(phrase) - 1
    for i in range(0, len(phrase)):
        if phrase[i] != phrase[j]:
            palindrome = False
            break
        j = j - 1

    if palindrome:
        print('Palindrome')
    else:
        print('Not a palendrome.')

# Implement with a for-enumeration loop
# You may use a break
def use_index_enum(phrase):
    palindrome = True

    for i, j in enumerate(range((len(phrase) - 1), 0, -1)):
        if phrase[i] != phrase[j]:
            palindrome = False
            break

    if palindrome:
        print('Palindrome')
    else:
        print('Not a palendrome.')