import unittest


def fun(string: str, letter, case_sensitive=True):
    if isinstance(string, int):
        string = str(string)
    if isinstance(letter, int):
        letter = str(letter)

    if string is None or letter is None:
        return "ERROR"

    if not case_sensitive:
        string = string.lower()
        letter = letter.lower()

    if isinstance(string, int) and isinstance(letter, int):
        string = str(string)
        letter = str(letter)
        return string.count(letter)

    elif isinstance(string, str) and isinstance(letter, str):
        return string.count(letter)

    return "ERROR"


class TestBasic(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(fun("cucumber", "u"), 2)
        self.assertEqual(fun("cucumber", "x"), 0)
        self.assertEqual(fun("Cucumber", "c"), 1)

a = TestBasic()
print(a.test_basic_cases())
class TestAdvanced(unittest.TestCase):
    def test_advanced_cases(self):
        self.assertEqual(fun("cucumber", "U", False), 2)
        self.assertEqual(fun("Cucumber", "c", False), 2)
        self.assertEqual(fun("Cucumber", "Uc", False), 1)


class TestExpert(unittest.TestCase):
    def test_expert_cases(self):
        self.assertEqual(fun("The boy was 5 years old", "5"), 1)
        self.assertEqual(fun(60224012, 2), 3)
        self.assertEqual(fun(60224012, "12"), 1)


b = TestExpert()
b.test_expert_cases()
