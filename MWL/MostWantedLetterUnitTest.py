from unittest import TestCase
from MWL.TheMostWantedLetter import checkio

class TestsIo(TestCase):
    
    def test_Hello_test(self):
        self.assertEqual("l", checkio("Hello World!"))

    def test_How_do_you_do(self):
        self.assertEqual("o", checkio("How do you do?"))

    def test_all_only_once(self):
        self.assertEqual("e", checkio("One"))

    def test_forget_about_lowercase(self):
        self.assertEqual("o", checkio("Oops!"))

    def test_only_letters(self):
        self.assertEqual("a", checkio("AAaooo!!!!!"))

    def test_the_first(self):
        self.assertEqual("a", checkio("abe"))

    def test_long_test(self):
        self.assertEqual("a", checkio("a"*9000 + "b"*1000))
