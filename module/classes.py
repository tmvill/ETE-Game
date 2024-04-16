import json
import os
from time import sleep
from module.inventory import Item, Backpack
from module.healthbar import HealthBar

#idk how to use decorators
class Player(object):
    """Stores user information and combat actions"""
    def __init__(self, name:str, 
                 maintype:int, 
                 level:int=1, 
                 levelxp:float=0.0, 
                 stats:dict={'hp': 100, 'atk': 50, 'def': 50, 'spe': 50,}, 
                 tier:int=1, 
                  case:int=0) -> None:
        self.name = name
        self.maintype = Type(maintype)
        self.level = level
        self.levelxp = levelxp
        self.stats = stats
        self.tier = tier
        self.case = case
        self.max_health = stats['hp']
        self.current_health = stats['hp']
        self.buffed = False
        self.dodge = False
        self.healthbar = HealthBar(self)
        self.backpack = Backpack(self)

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

    def dealdmg(self, target):
        if target.dodge is True:
            if self.stats['spe'] > target.stats['spe']:
                target.dodge = False
                return
        target.current_health = target.current_health - abs(self.stats['atk']/(5-self.level))
        if target.buffed == True:
            target.current_health = target.current_health - target.stats['def']
            target.buffed = False
            print(f"{target.name} defended against the attack")
        print(f"{self.name} did damage to {target.name}!")

    def defend(self):
        self.current_health = self.current_health + self.stats['def']
        print(f'{self.name} braced itself!')
        self.buffed = True

    def initStats(self, usertype:int):
        if usertype == 1:
            userPlayerType = Water(usertype)
            
            # set usertype as maintype
            self.maintype = usertype
            self.healthbar.color = userPlayerType.typecolor

            # Print stats in a human-readable format
            print(f"Starting element: {userPlayerType.__class__.__name__}")
            # self.showStats()

        elif usertype == 2:
            userPlayerType = Fire(usertype)
        
            # Copy and modify the 'default' stats into a new key
            self.maintype = usertype
            self.healthbar.color = userPlayerType.typecolor
            
            # Print stats in a human-readable format
            print(f"Main element: {userPlayerType.__class__.__name__}")
            # self.showStats()

        elif usertype == 3:
            userPlayerType = Earth(usertype)
            
            self.stats['def'] *= float(userPlayerType.defBuffValue())
            self.stats['spe'] *= float(userPlayerType.speDebuffValue())
            
            self.maintype = usertype
            self.healthbar.color = userPlayerType.typecolor
            
            # Print stats in a human-readable format
            print(f"Main element: {userPlayerType.__class__.__name__}")
            # self.showStats()

        elif usertype == 4:
            userPlayerType = Air(usertype)
    
            self.stats['def'] *= float(userPlayerType.defDebuffValue())
            self.stats['spe'] *= float(userPlayerType.speBuffValue())
            self.maintype = usertype
            self.healthbar.color = userPlayerType.typecolor

            # Print stats in a human-readable format
            print(f"Main element: {userPlayerType.__class__.__name__}")
            # self.showStats()

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
            self.initStats(usertype)
            
    
        elif variation == 2:
            for key, value in self.stats.items():
                self.stats[key] = abs(value + (self.level*5)/(5-self.tier))

        elif variation == 3:
            for key, value in self.stats.items():
                value = abs(value + self.tier*5)
                self.level = 1

    def combatEntry(self, target):
        try: # this shit barely works
            self.healthbar.draw()
            target.healthbar.draw()
            action = input((f'1. ATTACK\t2. DEFEND\n'
                            f'3. BAG\t\t4. DODGE'))
            if action in ["1",'2',3,4, 'attack','defend','bag','dodge']:
                print('Checking')
                if action in ['1', 'attack']:
                    print("Queueing attack")
                    self.dealdmg(target=target)
                elif action in [2, 'defend']:
                    print("Queueing defense")
                    self.defend()
                elif action in [3, 'bag']:
                    self.backpack.openbag()
                elif action in [4, 'dodge']:
                    return  self.stats['spe']
                self.healthbar.update()
                target.healthbar.update()
            elif 0>=int(action)<=4:
                return IndexError
            # else:
            #     return TypeError
        except:
            pass

# but at least i know what theyre called
class NPC(Player):
    """Enemy characters"""
    def __init__(self, name: str, 
                 maintype: int, 
                 storedxp: float, 
                 level: int = 1, 
                 stats: dict = {}, 
                 tier: int = 1) -> None:
        super().__init__(name, maintype, level, 1, stats, tier, 0) #todo fix this 
        self.storedxp = storedxp
        self.current_health = stats['hp']

    def getRandomEnemy(tier):
        from random import randint
        typerng = randint(1, 4)
        levelrng = randint(1, 3)
        enemy = NPC('Bhaddie', maintype=typerng, storedxp=(0.1*typerng*levelrng), stats={ 'hp': 100,'atk': 50,'def': 50,'spe': 50 }, level=levelrng, tier=tier)
        enemy.updateStats(1, typerng)
        enemy.updateStats(2)
        enemy.updateStats(3)
        return enemy
        


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
        if isinstance(savedata['healthbar'], object):
            try:
                healthbar = savedata['healthbar'].__dict__
                savedata['healthbar'] = healthbar
                savedata['healthbar']['entity'] = 'self'
            except AttributeError:
                pass
        if isinstance(savedata['backpack'], object):
            try:
                backpack = savedata['backpack'].__dict__
                savedata['backpack'] = backpack
                savedata['backpack']['entity'] = 'self'
            except AttributeError:
                pass
            
        # print(savedata['healthbar'])
        # input()
        # Write the data to the JSON file
        json.dump(savedata, save, indent=4)
        print('Save complete')

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
    def __init__(self, typename):
        super().__init__(typename)
        self.typecolor = "blue"

class Fire(Type):
    """Fire Element inherit from Type class"""
    def __init__(self, typename):
        super().__init__(typename)
        self.typecolor = "red"

class Earth(Type):
    """Earth Element inherit from Type class"""
    def __init__(self, typename, defBuff=1.35, speDebuff=0.35):
        super().__init__(typename)
        self.defBuff = defBuff
        self.speDebuff = speDebuff
        self.typecolor = "green"

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
        self.typecolor = "grey"

    def defDebuffValue(self) -> float:
        return self.defDebuff

    def speBuffValue(self) -> float:
        return self.speBuff



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
    os.system('cls')
    try:
        usersave = loadCharacter()
        return usersave
    except FileNotFoundError:
        return 1
    except json.decoder.JSONDecodeError:
        return 1
    input("Press any key to continue")
    os.system('cls')



