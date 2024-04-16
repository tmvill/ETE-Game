import module.classes as c
from module.inventory import Backpack, Item
from time import sleep
import os

def clear():
    os.system('cls')

def main():
    start = c.start()
    inCombat = False

    if start == 1: # Get user inputs for player class
        username = c.getUsername()
        inputtype = c.getUsertype()
        myPlayer = c.Player(name=username, maintype=inputtype)
        myPlayer.updateStats(1, inputtype)
        print(f"Starting element: {myPlayer.maintype}")
        myPlayer.showStats()
        save = myPlayer.__dict__
        c.saveCharacter(save)
        c.Dialogue(1)
        myPlayer.setCase(3)

    else: # Get dictionary from savefile, recreate player class
        save = start
        c.Dialogue(2)
        myPlayer = c.Player(save['name'], save['maintype'], save['level'], save['levelxp'], save['stats'], save['tier'], save['case'])
        myPlayer.maintype = save['maintype'] # Set value back to integer for reloading

    print('\n')
    c.Dialogue(0)
    input('\n')
    clear()

    while not inCombat:
        c.Dialogue(myPlayer.case)
        try:
            key_press = input()
            #Options during dialogue
            if key_press == '':
                myPlayer.advCase()
                clear()
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
            else:
                raise ValueError
        except:
            pass
        

        if myPlayer.case == 14:
            inCombat = True
            tutorial = c.NPC.getRandomEnemy(myPlayer.tier)
            # myPlayer.backpack.additem(ItemIndex[x])
            while inCombat:
                while True:
                    # clear()
                    try:
                        myPlayer.combatEntry(tutorial)
                    except ValueError:  # Raised when conversion to int fails (string input)
                            print('You will lose a turn if you make a misinput (bad command)')
                    except IndexError:
                        print('You will lose a turn if you make a misinput (number out of range)')
                    # finally:
                    #     input(". . .")

if __name__ == '__main__':
    main()


