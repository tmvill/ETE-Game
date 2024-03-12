import classes as c
import time

def start():
    print('Beginning launch sequence...')
    c.Item.initLoadItems()
    print('\n\n')
    try:
        usersave = c.Player.loadCharacter()
        c.Dialogue(2)
    except FileNotFoundError:
        c.Dialogue(1)
        usersave = c.Player.createCharactor()
        user = c.Player.saveCharacter(usersave)
    global case
    case = usersave['case']
    
    
def main():
    start()
    global case
    type(case)
    combat = False

    while 1:
        c.Dialogue(case)
        key_pressed = input("")
        if key_pressed.lower() == "":
            case +=1 
            pass
        




    


if __name__ == '__main__':
    main()
