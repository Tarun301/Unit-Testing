import unittest

from fiboNacci import recur_fibo

#class TestFibonacciSeries(Unittest.TestCase):
class TestFibonacciSeries(unittest.TestCase):
    # case assertion no1
    '''
    n = 1
    Should return [2]
    '''


    def test_recur_fibo_number_result_number(self):

        # arrange
        n = 1

        # act
        result = recur_fibo(n)

        #assert
        self.assertEqual(result, 1)

        print('\nFibonacci sequence\n')


    # case assertion no2
    '''
    n = -1
    Should return [0]
    '''

    def test_recur_fibo_number_result_number(self):

        # arrange
        n = -1

        # act
        result = recur_fibo(n)

        # assert
        self.assertEqual(result, -1)

        print('\nPlease enter a positive number\n')


    # case assertion no3
    '''
    n = 8
    Should return [15]
    '''

    def test_recur_fibo_number_result_number(self):

        # arrange
        n = 8

        # act
        result = recur_fibo(n)

        # assert
        self.assertEqual(result, 21)

        print('\nTest 3 is Passed\n')


    # case assertion no4
    '''
    n = 14
    Should return [89]
    '''


    def test_recur_fibo_number_result_number(self):

        # arrange
        n = 14

        # act
        result = recur_fibo(n)

        # assert
        self.assertEqual(result, 377)

        print('\nTest 4 is Passed\n')


    

if __name__ == '__main__':
    unittest.main()
    
    
