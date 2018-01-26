import unittest
from MonkeyTyping.MyAnswer import count_words


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}),3)

    def test_two(self):
        self.assertEqual(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}),2)

    def test_three(self):
        self.assertEqual(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}),1)


if __name__ == '__main__':
    unittest.main()
