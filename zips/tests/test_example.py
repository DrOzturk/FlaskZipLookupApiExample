import unittest
import numpy as np
from zips import example


# tests folder should be put in each module
# but they do not get included in zipped package,
# since MANIFEST.in excludes tests folder

# run tests via:
#   python -m unittest -v <test_module>
# get help via:
#   python -m unittest -h
class TestExample(unittest.TestCase):

    def test_greater_than(self):
        example_arr = np.array([4, 5, 2, 3, 6])
        returned = example.greater_than(example_arr, 4)
        expected = np.array([False, True, False, False, True])
        np.testing.assert_array_equal(
            expected,
            returned,
            "greater_than() function failed")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
    # For more verbose output
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestExample)
    # unittest.TextTestRunner(verbosity=2).run(suite)
