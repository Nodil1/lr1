import unittest


class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        self.assertEqual(add(1.1, 2.2), 3.3)

    def test_add_strings(self):
        self.assertEqual(add("hello ", "world"), "hello world")


def add(a, b):
    return a + b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
