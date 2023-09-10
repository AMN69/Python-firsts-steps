import unittest # first we import the test library
import cap # second we add as many py scripts as we want to test

class TestCap(unittest.TestCase): # third we create a class that uses unittest.TestCasse method

    def test_one_word(self): # fourth we create a function with def and self
        text = 'python' # fifth we define what we want to test
        result = cap.cap_text(text) # sixth we execute the code to test
        self.assertEqual(result,'Python') # seventh we assess the test comparing the our code with the result expected
    
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()