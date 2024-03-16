# First, we define the function that we want to test.
# In this case, it's a simple function to add two numbers.

def add(x, y):
    return x + y

# Now, we write a test case for the add function.
# We use the unittest module, which is a standard library module for writing and running tests.

import unittest

#TODO: After excuting this piece of code, change the line self.assertEqual(add(1, 2), 3)
#to self.assertEqual(add(1, 2), 2) and see what happens when executing it
class TestAddFunction(unittest.TestCase):
    
    def test_add(self):
        # Test that add function correctly adds two numbers
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

# This is the standard boilerplate to run the test suite.
if __name__ == '__main__':
    unittest.main()