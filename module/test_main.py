import unittest
from unittest.mock import patch, MagicMock #https://docs.python.org/3/library/unittest.mock.html tried reserching this
import main

class TestMain(unittest.TestCase):
#there doesnt seem to be much to test in main,but I cant get this to work properly. See test_classes.py for addittional unit tests
    @patch('main.c.Dialogue')
    @patch('main.input', side_effect=['', 's', 'showcase', 'showstats', 'simlevelup', 'simtierup', '_jump2combat'])
    def test_main_loop_options(self, mock_input, mock_dialogue):
        

        myPlayer = MagicMock(case=0, levelxp=0.0)
        myPlayer.levelup.return_value = None
        myPlayer.tierup.return_value = None
        main.inCombat = False
        
    
        main.main()

        self.assertTrue(myPlayer.advCase.called)  
        self.assertTrue(myPlayer.showStats.called)  
        self.assertTrue(myPlayer.levelup.called) 
        self.assertTrue(myPlayer.tierup.called) 
        myPlayer.setCase.assert_called_once_with(10) 

if __name__ == '__main__':
    unittest.main()
