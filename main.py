import module.classes as c
from time import sleep
####### NOTE:    It looks like you already updated your game in the main branch. These are the edits for the version that was originally posted from last week's version
###### Don't merge the pull request since you already updated the game files
def combat_handler(myPlayer): #main is a little crowded, so I added this combat handling method to clean it up a bit.
    """you can consider creating a class in modules.py that is used for game handling and
management or something similar that suits your needs. 
Can't wait to see how the combat plays out when it's complete"""
    while myPlayer.case <= 20 and myPlayer.case >= 10:
            c.Dialogue(myPlayer.case)
            key_press = input() 
            if key_press == '':
                myPlayer.advCase()
            if myPlayer.case == 14:
                while True:
                    try:
                        combatEntry = input('\t1. ATTACK\t2. DEFEND\n\t3. BAG\t\t4. DODGE\n')
                        combatEntry = int(combatEntry) #takes int value first
                        if 1 <= combatEntry <= 4:
                            if combatEntry == 1:
                                print('myPlayer.dealDmg(target)')
                            elif combatEntry == 2:
                                print('myPlayer.setDef()')
                            elif combatEntry == 3:
                                print('myBackpack.showInventory()')
                            else:  # combatEntry == 4 (dodge)
                                print('myPlayer.dodge()')
                        else:
                            raise IndexError  # Handle invalid integer input (out of range)
                    except ValueError:  # Raised when conversion to int fails (string input)
                        combatEntry = combatEntry.lower()  # Convert to lowercase for string comparison
                        if combatEntry in ["attack", "defend", "bag", "dodge"]:
                            # Use string values for case handling
                            if combatEntry == "attack":
                                print('myPlayer.dealDmg(target)')
                            elif combatEntry == "defend":
                                print('myPlayer.setDef()')
                            elif combatEntry == "bag":
                                print('myBackpack.showInventory()')
                            else:  # combatEntry == "dodge"
                                print('myPlayer.dodge()')
                        else:
                            print('You will lose a turn if you make a misinput (bad command)')
                    except IndexError:
                        print('You will lose a turn if you make a misinput (number out of range)')

def dialogue_ANDinputhandler(myPlayer):
    "again, this is to help clean up main"
    while True: #just added true as a placeholder for now

        c.Dialogue(myPlayer.case)
        try:
            key_press = input()

            #Options during dialogue
            if key_press == '':
                myPlayer.advCase()
            elif key_press.lower() == 's':
                save = myPlayer.__dict__
                c.saveCharacter(save)
            elif key_press.lower() == 'showcase':
                print(F'Current casenum: {myPlayer.case}')
            elif key_press.lower() == 'showstats':
                myPlayer.showStats()
            elif key_press.lower() == 'simlevelup':
                myPlayer.levelxp += .75
                myPlayer.levelup()
                myPlayer.checkxp()
            elif key_press.lower() == 'simtierup':
                myPlayer.tierup()
            elif key_press.lower() == '_jump2combat':
                myPlayer.setCase(10)
                #inCombat = True
                combat_handler(myPlayer) #can call the funciton here in place of inConbat = True to help with compartamentalization in main()
                break
            else:
                raise ValueError
            
        except ValueError:
            pass



def main():
    start = c.start()
    inCombat = False

    if start == 1: #Get user inputs for player class
        username = c.getUsername()
        inputtype = c.getUsertype()
        myPlayer = c.Player(name=username, maintype=inputtype)
        myPlayer.updateStats(1, inputtype)
        save = myPlayer.__dict__
        c.saveCharacter(save)
        myPlayer.setCase(3)

    else: #Get dictionary from savefile, recreate player class
        save = start
        c.Dialogue(2)
        myPlayer = c.Player(save['name'], save['maintype'], save['level'], save['levelxp'], save['stats'], save['tier'], save['case'])
        myPlayer.maintype = save['maintype']

    print('\n')
    c.Dialogue(0)
    print('\n')


   
    dialogue_ANDinputhandler(myPlayer)
    #combat_handler(myPlayer)

    """while not inCombat: #Start of main loop #######################################
        c.Dialogue(myPlayer.case)
        try:
            key_press = input()

            #Options during dialogue
            if key_press == '':
                myPlayer.advCase()
            elif key_press.lower() == 's':
                save = myPlayer.__dict__
                c.saveCharacter(save)
            elif key_press.lower() == 'showcase':
                print(F'Current casenum: {myPlayer.case}')
            elif key_press.lower() == 'showstats':
                myPlayer.showStats()
            elif key_press.lower() == 'simlevelup':
                myPlayer.levelxp += .75
                myPlayer.levelup()
                myPlayer.checkxp()
            elif key_press.lower() == 'simtierup':
                myPlayer.tierup()
            elif key_press.lower() == '_jump2combat':
                myPlayer.setCase(10)
                inCombat = True
                break
            else:
                raise ValueError
            
        except ValueError:
            pass"""
    
    

    """while inCombat: #Figured out how to trigger the combat loop by looking at the code. "_jump2combat" 
        if myPlayer.case <= 20 and myPlayer.case >= 10:
            c.Dialogue(myPlayer.case)
            key_press = input() 
            if key_press == '':
                myPlayer.advCase()
            if myPlayer.case == 14:
                while True:
                    try:
                        combatEntry = input('\t1. ATTACK\t2. DEFEND\n\t3. BAG\t\t4. DODGE\n')
                        combatEntry = int(combatEntry) #takes int value first
                        if 1 <= combatEntry <= 4:
                            if combatEntry == 1:
                                print('myPlayer.dealDmg(target)')
                            elif combatEntry == 2:
                                print('myPlayer.setDef()')
                            elif combatEntry == 3:
                                print('myBackpack.showInventory()')
                            else:  # combatEntry == 4 (dodge)
                                print('myPlayer.dodge()')
                        else:
                            raise IndexError  # Handle invalid integer input (out of range)
                    except ValueError:  # Raised when conversion to int fails (string input)
                        combatEntry = combatEntry.lower()  # Convert to lowercase for string comparison
                        if combatEntry in ["attack", "defend", "bag", "dodge"]:
                            # Use string values for case handling
                            if combatEntry == "attack":
                                print('myPlayer.dealDmg(target)')
                            elif combatEntry == "defend":
                                print('myPlayer.setDef()')
                            elif combatEntry == "bag":
                                print('myBackpack.showInventory()')
                            else:  # combatEntry == "dodge"
                                print('myPlayer.dodge()')
                        else:
                            print('You will lose a turn if you make a misinput (bad command)')
                    except IndexError:
                        print('You will lose a turn if you make a misinput (number out of range)')"""


if __name__ == '__main__':
    main()


