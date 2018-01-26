'''
This is purely a review of others code that I have read and want to learn more about
none of this code is my own
'''
# string class has some good methods, so look under this when dealing with strings
import string


def checkio(text):
    #the count function here is confusing
    print(text.count)
    #returns <built-in method count of str object at [memory reference]>
    print(text.count(string.ascii_lowercase))
    #adds a zero below the memory reference
    print(text.count('e'))
    #adds the number of e's

    #it seems as though key can be a parameter within the max function
    return max(string.ascii_lowercase,key=text.lower().count)
    '''
    so the above function says return the maxium of ascii_lowercase letters,
    based on the key of counting where each of these characters occur in the  lowercase
    version of the inputted text
    
    Note how this guy talked about what his algorithm actually was within the code
    
    '''

    #Also the ascii method can put the lowercase alphabet in order to be compared against
    #also the max functions key will be useful


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")