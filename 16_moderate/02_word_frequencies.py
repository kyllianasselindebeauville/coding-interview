# 16.2 Word Frequencies

import unittest


def get_frequencies(text):
    word_frequencies = dict()

    for word in text.lower().split():
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    return word_frequencies


class Test(unittest.TestCase):
    def test_get_frequencies(self):
        text = """
            This is a test
            This is another test
        """

        self.assertEqual(
            get_frequencies(text),
            {
                'this': 2,
                'is': 2,
                'a': 1,
                'another': 1,
                'test': 2
            }
        )


if __name__ == '__main__':
    unittest.main()
