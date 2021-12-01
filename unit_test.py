import unittest

def sample_sum_function(a=0,b=0):
    return a + b

def sample_sub_function(a=0,b=0):
    return a-b

class Sample_Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum_withInput(self):
        result = sample_sum_function(a=1,b=1)
        assert result == 2

    def test_sub_noInput(self):
        result = sample_sub_function()
        assert result == 0

    def test_sub_noInput(self):
        result = sample_sum_function()
        assert result == 0

    def test_sum_withInput(self):
        result = sample_sub_function(a=1,b=1)
        assert result == 0

if __name__ == '__main__':
    unittest.main()

    

