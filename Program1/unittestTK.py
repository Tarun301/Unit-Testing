import unittest

from countCharacters import count_characters

#class TestCountingMethods(Unittest.TestCase):
class TestCountingMethods(unittest.TestCase):    
    # case assertion no1
    '''
    word = Tarunkimati1786
    should return [1, 10, 4]
    '''


    def test_count_characters_word_result_array_1_15_4(self):


        # arrange
        word = "Tarunkimati1786"


        # act
        result = count_characters(word)


        # assert
        self.assertEqual(result, [1, 10, 4])
        
        print('\nNormal word test is passed\n')


    # case assertion no2
    '''
    word = TTTUUYYIOH
    should return [10, 0, 0]
    '''

    def test_count_characters_word_result_array_10_3_0(self):


        # arrange
        word = "TTTUUYYIOH"

        # act
        result = count_characters(word)

        # assert
        self.assertEqual(result, [10, 0, 0])

        print('\nUppercase only test is passed\n')


    # case assertion no3
    '''
    word = aagguuuhhff
    should return [0, 11, 0]
    '''

    def test_count_characters_word_result_array_0_12_7(self):

        # arrange
        word = "aagguuuhhff"

        # act
        result = count_characters(word)

        # assert
        self.assertEqual(result, [0, 11, 0])

        print('\nLowercase only test is passed\n')


    # case assertion no4
    '''
    word = 097868668
    should return [0, 0, 9]
    '''

    def test_count_characters_word_result_array_2_6_9(self):

        # arrange
        word = "097868668"

        # act
        result = count_characters(word)

        # asasert
        self.assertEqual(result, [0, 0, 9])

        print('\nOthercase only test is passed\n')

        
    
        



if __name__ == '__main__':
    unittest.main()
    temp=0




