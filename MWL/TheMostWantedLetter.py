def checkio(text):

    #replace this for solution
            textList = [[x] for x in sorted(set(text.lower())) if x.isalpha()]
            for x in text.lower():
                for y in textList:
                    if x == y[0]:
                       y.append(x)
            common = []
            for y in textList:
                if len(y) > len(common):
                    common = y
            return common[0]

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