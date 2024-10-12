# PROGRAM:  Palindrome_rbd.py
# AUTHOR:  Robert Depweg                                     DESIGNER:  Kaminski
# Modification: Strings Only clc
# THE TASK:  Use 2 techniques to test if a string is a palindrome (i.e.,
#       the word/phrase reads the same forwards and backwards) - assuming the
#       program first fixes the word/phrase so it's all the same case (say all
#       lower case) AND spaces & punctuation have been removed.  So, for
#       example, these are palindromes:
#           'Mom', '123454321', 'UFO tofu?'
#
# FOLLOW THESE INSTRUCTIONS:
# main ALGORITHM: Call the following steps 6 times- once for each phrase
#   1) "clean up" the phrase by calling the clean function
#   2) call use_index function with the phrase

# use_index & clean functions are in separate module (together)
# clean prints original phrase, then (on next line) the cleaned up phrase
#       - the only punctuation the function has to remove are what's in these
#           test cases, so that's : , . - ? and spaces
# use_index uses a loop to compare characters, where index1 starts at 0 and
#       index2 starts at the end
#       - each time around the loop, index1 increments, index2 decrements
#       

# use_index - check if it's a palindrome or not & print result
#
# FOOTNOTE:  the phrases are taken from the website:
#           https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("/033c")
import check_palindrome_rbd as cp

PHRASE1 = 'Was it a car or a cat I saw?'
PHRASE2 = 'Do geese see God?'
PHRASE3 = 'A man, a plan, a canal: Panama.'
PHRASE4 = 'AA'
PHRASE5 = '1-3-5-77531'
PHRASE6 = 'Kalamazoo Valley'

def main():

    #clean_p1 = cp.clean(PHRASE1)
    clean_p1 = cp.clean("nodn")
    cp.use_index_while(clean_p1)
    cp.use_index_for(clean_p1)
    cp.use_index_enum(clean_p1)

    clean_p2 = cp.clean(PHRASE2)
    cp.use_index_while(clean_p2)
    cp.use_index_for(clean_p2)
    cp.use_index_enum(clean_p2)

    clean_p3 = cp.clean(PHRASE3)
    cp.use_index_while(clean_p3)
    cp.use_index_for(clean_p3)
    cp.use_index_enum(clean_p3)

    clean_p4 = cp.clean(PHRASE4)
    cp.use_index_while(clean_p4)
    cp.use_index_for(clean_p4)
    cp.use_index_enum(clean_p4)
  
    clean_p5 = cp.clean(PHRASE5)
    cp.use_index_while(clean_p5)
    cp.use_index_for(clean_p5)
    cp.use_index_enum(clean_p5)

    clean_p6 = cp.clean(PHRASE6)
    cp.use_index_while(clean_p6)
    cp.use_index_for(clean_p6)
    cp.use_index_enum(clean_p6)
    
    print('\nTHE END')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Conditional call to main()
if __name__ == '__main__':
    main()
