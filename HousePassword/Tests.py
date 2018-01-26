import unittest

from HousePassword.MyAnswer import checkio

class HousePasswordTest(unittest.TestCase):

    def test_FstExample(self):
        self.assertEqual(
            False,
            checkio('A121pokl')
        )

    def test_SndExample(self):
        self.assertEqual(
            True,
            checkio('bAse730onE4')
        )

    def test_TrdExample(self):
        self.assertEqual(
            False,
            checkio('asasasasasasasaas')
        )

    def test_FrthExample(self):
        self.assertEqual(
            False,
            checkio('QWERTYqwerty')
        )

    def test_FfthExample(self):
        self.assertEqual(
            False,
            checkio('123456123456')
        )

    def test_SxthExample(self):
        self.assertEqual(
            True,
            checkio('QwErTy911poqqqq')
        )


if __name__ == '__main__':
    unittest.main()