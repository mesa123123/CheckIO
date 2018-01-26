from MWL.TheMostWantedLetter import checkio

def test_qwerty():
    assert(checkio("qwertyuioplkjhgfdsamnbvcxz123456789") == "a")

# def test_gigebyte():
#     assert(checkio("100002305401"))

def test_foundit():
    assert(checkio("Its here!") == "e")

def test_triggerHappy():
    assert(checkio("triggger happy") == "g")

def test_numbersonly():
    assert(checkio("11001010") == "")