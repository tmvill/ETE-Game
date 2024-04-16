import unittest
import module.classes as c
from io import StringIO
from unittest.mock import patch, MagicMock #imported this with hopes of isolating some functions, but I'm not a wizard 
                                            #https://docs.python.org/3/library/unittest.mock.html

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = c.Player(name="AdrianTestPlayer", maintype=1)

    def test_player_initialization_water(self):
        player = c.Player(name="AdrianTestPlayer", maintype=1)
        self.assertEqual(player.name, "AdrianTestPlayer")
        self.assertEqual(player.maintype, "Water")

    def test_player_initialization_fire(self):
        player = c.Player(name="AdrianTestPlayer", maintype=2)
        self.assertEqual(player.name, "AdrianTestPlayer")
        self.assertEqual(player.maintype, "Fire")

    def test_player_initialization_earth(self):
        player = c.Player(name="AdrianTestPlayer", maintype=3)
        self.assertEqual(player.name, "AdrianTestPlayer")
        self.assertEqual(player.maintype, "Earth")

    def test_player_initialization_air(self):
        player = c.Player(name="AdrianTestPlayer", maintype=4)
        self.assertEqual(player.name, "AdrianTestPlayer")
        self.assertEqual(player.maintype, "Air")

    def test_tier_up(self):
            self.player.level = 3
            self.player.tierup()
            self.assertEqual(self.player.tier, 2) #seems to be working. Each level has 3 tiers, and each level starts at the first tier? 

    def test_show_stats(self):
        self.player.stats = {'hp': 100, 'atk': 50, 'def': 50, 'spe': 50}
        expected_output = "\thp: 100\n\tatk: 50\n\tdef: 50\n\tspe: 50\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.player.showStats()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_player_level_up(self):
        """Used to test player level up. I am having issues isolating this method though. I can see
        that the ouput is 5, but the unit test still makes an error in the terminal"""
        mock_player = MagicMock(spec=c.Player)
        with patch('module.classes.Player', return_value=mock_player):
            self.player.level = 4
            self.player.levelxp = 2
            self.player.levelup()
        
            mock_player.updateStats.assert_called_once_with(2)

class TestType(unittest.TestCase):

    def test_type_initialization(self):
        """using this to test if the player types are initialized correctly. In my playthrough, only earth (3) and air (4) worked"""
        element_type = c.Type(1)
        self.assertEqual(element_type.typename, "Water")
    
        element_type = c.Type(2)
        self.assertEqual(element_type.typename, "Fire")

        element_type = c.Type(3)
        self.assertEqual(element_type.typename, "Earth")

        element_type = c.Type(4)
        self.assertEqual(element_type.typename, "Air")

if __name__ == '__main__':
    unittest.main()
