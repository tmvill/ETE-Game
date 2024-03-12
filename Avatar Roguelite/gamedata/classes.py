import time
import json

class Player(object):
    """User information and combat stats, """
    def __init__(self, name: str, backpack, mainType, level: int, levelxp: float, stats: dict, tier: int, case: int):
        self.name = name
        #self.backpack = Backpack(None, [])    #Player Backpack Class
        self.mainType = {
            1: 'Water',
            2: 'Fire',
            3: 'Earth',
            4: 'Air',
            }[mainType]    #Players starting type
        self.level = level          #Level multiplier
        self.levelxp = levelxp      #Level progression system
        self.stats = {'default':{'hp': 100, 'atk': 50, 'def': 50, 'spe': 50,}}
        self.tier = tier            #Level tier as int
        self.case = case

    def CheckBag(self, backpack):
        """Lists items in bag, with quantity"""
        for i in self.backpack.getItem(i).name():
            print(i)

    @staticmethod
    def createCharactor(): 
        """Asks for username and usertype. Returns Player.__dict__ for saveCharacter function"""
        username = ''
        usertype = 0

        while username == '':
            username = input('Enter your name to begin your journey..')
        while usertype == 0:
            usertype = int(input('Choose your main element type:\n\t1. Water\n\t2. Fire\n\t3. Earth\n\t4. Air\n'))

        userPlayer = Player(username, None, usertype, level=1, levelxp=1.0, stats='default', tier=1, case=1)      
        
        if usertype == 1:
            userPlayerType = Water(usertype)
            
            # Copy and modify the 'default' stats into a new key
            userPlayer.stats[userPlayerType.__class__.__name__] = dict(userPlayer.stats['default'])
            del userPlayer.stats['default']

            # Print stats in a human-readable format
            print(f"Starting element: {userPlayer.stats.keys()}")
            for key, stats in userPlayer.stats.items():
                print(f"\t{key}: {stats}")  # Print each stat on a new line

        elif usertype == 2:
            userPlayerType = Fire(usertype)
            
            # Copy and modify the 'default' stats into a new key
            userPlayer.stats[userPlayerType.__class__.__name__] = dict(userPlayer.stats['default'])
            del userPlayer.stats['default']

            # Print stats in a human-readable format
            print(f"Starting element: {userPlayer.stats.keys()}")
            for key, stats in userPlayer.stats.items():
                print(f"\t{key}: {stats}")  # Print each stat on a new line

        elif usertype == 3:
            userPlayerType = Earth(usertype)
            userPlayer.stats['default']['def'] *= float(Earth.defBuffValue(userPlayerType))
            userPlayer.stats['default']['spe'] *= float(Earth.speDebuffValue(userPlayerType))
            # Copy and modify the 'default' stats into a new key
            userPlayer.stats[userPlayerType.__class__.__name__] = dict(userPlayer.stats['default'])
            del userPlayer.stats['default']

            # Print stats in a human-readable format
            print(f"Starting element: {userPlayer.stats.keys()}")
            for key, stats in userPlayer.stats.items():
                print(f"\t{key}: {stats}")  # Print each stat on a new line

        elif usertype == 4:
            userPlayerType = Air(usertype)
            
            # Copy and modify the 'default' stats into a new key
            userPlayer.stats[userPlayerType.__class__.__name__] = dict(userPlayer.stats['default'])
            del userPlayer.stats['default']

            # Print stats in a human-readable format
            print(f"Starting element: {userPlayer.stats.keys()}")
            for key, stats in userPlayer.stats.items():
                print(f"\t{key}: {stats}")  # Print each stat on a new line


        savedata = userPlayer.__dict__
        return savedata
        
    def saveCharacter(savedata):
        """Saves the character data to a JSON file."""
        with open('save.json', 'w') as save:
            # Ensure stats dictionary is JSON-serializable
            if isinstance(savedata['stats'], dict):
                stats = {key: list(value.values()) for key, value in savedata['stats'].items()}
                savedata['stats'] = stats

            # Write the data to the JSON file
            json.dump(savedata, save, indent=4)
            print('Save complete')

    def advanceCase(self):
        self.case += 1

    def loadCharacter():
        """Opens save file and returns player information"""
        with open('save.json', 'r') as save:
            savedata = json.load(save)
            print('Loaded save data')
        return savedata
    
    def getStats(self, stat):
        "Retrieve's player stats as dictionary and returns value for type pair"
        #value = self.stats[]
    
    def dealdmg(self, enemy):
        atkpoints = self.stats.keys()['atk'].values()
        print(atkpoints)

    
    def enterCombat(self, enemy):
        while True: #Enter combat loop
            userinput = ''
            while userinput == '':
                userinput = int(input('Choose an option:\n\t1. Attack!\n\t2. Block\n\t3. Check Bag'))
                if userinput == 1:
                    Player.dealdmg(self, enemy)
                    


class Enemy(Player):
    """Enemy npc information, inherits from Player class"""
    def __init__(self, name: str, mainType: object, level: int, stats: dict, tier: int, xpvalue: float):
        super().__init__(name, mainType, level, stats, tier)
        self.xpvalue = xpvalue      #Float amount of XP stored in enemy npc
                 
        
class Backpack(object):
    """Backpack class with """
    def __init__(self, item, itemlist: list):
        self.item = Item
        itemlist = []

    def getItem(self, Item):
        for i in self.item:
            print(i)

    def addItem(self, Item):
        if Item not in self.itemlist:
            self.itemlist.append(Item)
        else:
            for Item in self.itemlist:
                Item.count += 1

print('PlayerIni.py is ready')        



itemlist = 'itemlist.json'

class Item(object):
    """Usuable items """
    def __init__(self, name: str, attribute: str, tier: int, amount_to_merge: int, power: float, count: int): 
        self.name = name
        self.count = count
        self.attribute = attribute
        self.power = power
        self.amount_to_merge = amount_to_merge

    def ConsumeItem(self, Player):
        if self.attribute == 1:
            Player.stats['Health'] += self.power
            print('')
        else:
            Player.stats[self.attribute] *= self.power


    def MergeItems(self):
        if self.count >= self.amount_to_merge:
            self.count -= self.amount_to_merge


    def initLoadItems():
        with open(itemlist, 'r') as file:
            templist = json.load(file)
            for i in range(len(templist)):
                Item(templist[i]['name'], templist[i]['type'], templist[i]['tier'], templist[i]['amount_to_merge'], templist[i]['power'], count=0)
                print(f'Loaded {templist[i]['name']} into Item class')


print('items.py is ready')

def Dialogue(caseNum: int, delay=0.025, script_path='script.json'):
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
                    time.sleep(delay)

    except IndexError:
        text = "You've gone too far.. I need more time to develop more dialogue"

        # Display text character by character when text is not available
        if text:
            #print('Displaying dialogue:')
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)

    except FileNotFoundError as e:
        print(f"Error: Script file '{script_path}' not found.")

    except Exception as e:  # Catch other potential exceptions
        print(f"Unexpected error: {e}")

print('Story.py is ready')

class Type(object):
    """Type information for the different elements, contains advantages and disadvantage"""
    def __init__(self, typename, strengths=None, weaknesses=None, immunity=None):
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
    def __init__(self, typename, defBuff=1.25, speDebuff=0.25):
        super().__init__(typename)
        self.defBuff = defBuff
        self.speDebuff = speDebuff

    def defBuffValue(self):
        return self.defBuff
    def speDebuffValue(self):
        return self.speDebuff


class Air(Type):
    """Air Element inherit from Type class"""

print('Typeini.py is ready')
print('\n###--###--###--###--###\n')