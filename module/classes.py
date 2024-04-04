import json
from time import sleep

class Player(object):
    """Stores user information and combat actions"""
    def __init__(self, name:str, maintype:dict, level:int=1, levelxp:float=0.0, stats:dict=None, tier:int=1, case:int=0) -> None:
        self.name = name
        self.maintype = {
            1: 'Water',
            2: 'Fire',
            3: 'Earth',
            4: 'Air',
        }[maintype]
        self.level = level
        self.levelxp = levelxp
        self.stats = stats
        self.tier = tier
        self.case = case

    def showStats(self):
        """Shows players stats"""
        for key, stats in self.stats.items():
            print(f"\t{key}: {stats}")  # Print each stat on a new line

    def advCase(self):
        self.case += 1

    def setCase(self, casenum):
        self.case = casenum

    def levelup(self):
        if self.levelxp >= 1.0 and self.level <= 5:
            self.levelxp %= 1.0
            self.level += 1
            print(f"You are now Lvl. {self.level}!")
            self.updateStats(2)
            self.showStats()

    def checkxp(self):
        print('Need %.2f more XP to level up' % (abs(1-self.levelxp)))

    def tierup(self):
        if self.level >= 3:
            self.tier += 1
            self.level = 1
            print(f"You are now Tier {self.tier}")
            self.updateStats(3)
            self.showStats()

    def updateStats(self, variation:int, usertype:int=None):
        """Update user stats based on variation.
        Args:
            Variation 1-4
            1: Initial stat change when selecting a type
            2: Level up stat increase
            3: Tier up stat increase
            4: Combat Stat change (in development)
            
            Type 1-4 (For varitation = 1)
            1: Water
            2: Fire
            3: Earth
            4: Air"""
        if variation == 1 and usertype is not None:
            
            self.stats = {'hp': 100, 'atk': 50, 'def': 50, 'spe': 50,}
            if usertype == 1:
                userPlayerType = Water(usertype)
                
                # set usertype as maintype
                self.maintype = usertype

                # Print stats in a human-readable format
                print(f"Starting element: {userPlayerType.__class__.__name__}")
                self.showStats()

            elif usertype == 2:
                userPlayerType = Fire(type)
            
                # Copy and modify the 'default' stats into a new key
                self.maintype = usertype

                # Print stats in a human-readable format
                print(f"Starting element: {userPlayerType.__class__.__name__}")
                self.showStats()

            elif usertype == 3:
                userPlayerType = Earth(usertype)
                
                self.stats['def'] *= float(userPlayerType.defBuffValue())
                self.stats['spe'] *= float(userPlayerType.speDebuffValue())
                
                self.maintype = usertype

                # Print stats in a human-readable format
                print(f"Starting element: {userPlayerType.__class__.__name__}")
                self.showStats()

            elif usertype == 4:
                userPlayerType = Air(usertype)
        
                self.stats['def'] *= float(userPlayerType.defDebuffValue())
                self.stats['spe'] *= float(userPlayerType.speBuffValue())
                self.maintype = usertype

                # Print stats in a human-readable format
                print(f"Starting element: {userPlayerType.__class__.__name__}")
                self.showStats()
    
        elif variation == 2:
            for key, value in self.stats.items():
                self.stats[key] = abs(value + (self.level*5)/(5-self.tier))

        elif variation == 3:
            for key, value in self.stats.items():
                value = abs(value + self.tier*5)
                self.level = 1


def loadCharacter():
    """Opens save file and returns player information as dictionary"""
    with open('save.json', 'r') as save:
        savedata = json.load(save)
        print('Loaded save data')
    return savedata
    
def saveCharacter(savedata):
    """Saves the character data to a JSON file. Takes in savedata as dictionary"""
    with open('save.json', 'w') as save:
        # Ensure stats dictionary is JSON-serializable
        if isinstance(savedata['stats'], dict):
            stats = {key: value for key, value in savedata['stats'].items()}
            savedata['stats'] = stats

        # Write the data to the JSON file
        json.dump(savedata, save, indent=4)
        print('Save complete')
           
class NPC(Player):
    """"""

class Type(object):
    """Type information for the different elements, contains advantages and disadvantage"""
    def __init__(self, typename:int, strengths=None, weaknesses=None, immunity=None):
        self.typename = {
            1: 'Water',
            2: 'Fire',
            3: 'Earth',
            4: 'Air',
        }[typename]
        self.strengths = strengths      #List of types that cause attacks to deal 2x dmg
        self.weaknesses = weaknesses    #List of types that cause attacks to deal 0.5x dmg

    def showType(self):
        print(self.typename.value())

class Water(Type):
    """Water Element inherit from Type class"""
    def __init__(self, typename, tier, ):
        super().__init__(typename)

class Fire(Type):
    """Fire Element inherit from Type class"""

class Earth(Type):
    """Earth Element inherit from Type class"""
    def __init__(self, typename, defBuff=1.35, speDebuff=0.35):
        super().__init__(typename)
        self.defBuff = defBuff
        self.speDebuff = speDebuff

    def defBuffValue(self) -> float:
        return self.defBuff
    def speDebuffValue(self) -> float:
        return self.speDebuff


class Air(Type):
    """Air Element inherit from Type class"""
    def __init__(self, typename, defDebuff=0.5, speBuff=1.35):
        super().__init__(typename)
        self.defDebuff = defDebuff
        self.speBuff = speBuff

    def defDebuffValue(self) -> float:
        return self.defDebuff

    def speBuffValue(self) -> float:
        return self.speBuff

class Item(object):
    """Usuable items """
    def __init__(self, name: str, attributeType: str, tier: int, amount_to_merge: int, power: float, count: int): 
        self.name = name
        self.count = count
        self.attributeType = attributeType
        self.power = power
        self.amount_to_merge = amount_to_merge

    def ConsumeItem(self, Player):
        if self.attributeType == 1:
            Player.stats['Health'] += self.power
            print('')
        else:
            Player.stats[self.attribute] *= self.power


    def MergeItems(self):
        if self.count >= self.amount_to_merge:
            self.count -= self.amount_to_merge


    def initLoadItems():
        with open('module\itemlist.json', 'r') as file:
            templist = json.load(file)
            for i in range(len(templist)):
                Item(templist[i]['name'], templist[i]['type'], templist[i]['tier'], templist[i]['amount_to_merge'], templist[i]['power'], count=0)
                print(f'Loaded {templist[i]['name']} into Item class')


class Backpack(object):
    """Player's bag with items"""

def Dialogue(caseNum: int, delay=0.025, script_path='module\script.json'):
    """Displays game text char by char
    Args:
        caseNum (int): Case number for identifying the desired dialogue content.
        delay (float, optional): Delay between characters (default 0.025 seconds).
        script_path (str, optional): Path to the JSON file containing dialogue data.
    """
    #print('Attempting diaglogue')
    try:
        # Open the file in either read or write mode depending on context
        with open(script_path, 'r') as file:
            #print(f"Opened script '{script_path}'")

            # Access file content based on caseNum (implementation specifics needed here)
            data = json.load(file)
            text = data[caseNum]['text']

            # Display text character by character if text is available
            if text:
                #print('Displaying dialogue:')
                for char in text:
                    print(char, end='', flush=True)
                    sleep(delay)

    except IndexError:
        text = "You've gone too far.. I need more time to develop more dialogue"

        # Display text character by character when text is not available
        if text:
            #print('Displaying dialogue:')
            for char in text:
                print(char, end='', flush=True)
                sleep(delay)

    except FileNotFoundError as e:
        print(f"Error: Script file '{script_path}' not found.")

    except Exception as e:  # Catch other potential exceptions
        print(f"Unexpected error: {e}")

def getUsername() -> str:
    """Gets input for username, returns string"""
    while True:
        #Get username
        try:
            username = str(input('Enter your name to begin your journey: '))
            if username == '' or username == ' ' or username == '   ':
                raise TabError
            else:
                return username
                break
        except TabError:
            username = str(input('Please enter your name (Cannot be empty): '))
            
def getUsertype() -> int:
    """Gets usertype, returns int value 1-4"""
    while True:
        #Get starting type
        try:
            usertype = int(input('Choose your main element type:\n\t1. Water\n\t2. Fire\n\t3. Earth\n\t4. Air\n'))
            if usertype >= 5 or usertype <= 0:
                raise IndexError
            else:
                return usertype
                break
        except TypeError:
            usertype = int(input('Please enter an integer value:\n\t1. Water\n\t2. Fire\n\t3. Earth\n\t4. Air\n'))
        except IndexError:
            usertype = int(input('Please enter a value between 1 and 4:\n\t1. Water\n\t2. Fire\n\t3. Earth\n\t4. Air\n'))
    

def start() -> int:
    """Starts sequence. Returns savedict if save exists, otherwise 1; Create character"""
    print('Beginning launch sequence...')
    Item.initLoadItems()
    print('\n\n')
    try:
        usersave = loadCharacter()
        return usersave
    except FileNotFoundError:
        return 1



