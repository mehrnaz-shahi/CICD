import unittest
import cal


class TestAdd(unittest.TestCase):
    def test_list_int(self):
        result = cal.add(1, 2)
        self.assertEqual(result, 3)


class TestSub(unittest.TestCase):
    def test_minus(self):
        result = cal.sub(12, 5)
        self.assertEqual(result, 7)

    def test_minus_minus(self):
        result = cal.sub(3, 7)
        self.assertEqual(result, -4)


class TestMod(unittest.TestCase):
    def test_mod(self):
        result = cal.mod(12, 5)
        self.assertEqual(result, 2)


class TestDiv(unittest.TestCase):
    def test_div(self):
        result = cal.div(10, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
