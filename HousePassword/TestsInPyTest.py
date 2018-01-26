from HousePassword.MyAnswer import checkio

def test_checkio_1():
    assert(checkio("HelloWorld") == True)

def test_checkio_2():
    assert(checkio("2") == False)


