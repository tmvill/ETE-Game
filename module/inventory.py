import json

class Item:
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
        ItemIndex = []
        with open('module\itemlist.json', 'r') as file:
            templist = json.load(file)
            for i in range(0, len(templist)):
                ItemIndex.append(Item(templist[i]['name'], templist[i]['type'], templist[i]['tier'], templist[i]['amount_to_merge'], templist[i]['power'], count=0))
                print(f'Loaded {templist[i]} into ItemIndex:{i} Item class')


class Backpack:
    """Player's bag with items"""
    def __init__(self, entity, slot:dict={}, slotno:int = 0, item:str = '') -> None:
        self.entity = entity
        self.slot = slot
        self.slotno = slotno

    def additem(self, object):
        self.slot[self.slotno] = object
        print(f'Added {object} to slot {self.slotno}')
        self.slotno += 1
        
    def openbag(self):
        for i, items in enumerate(self.slot.values()):
            print(f"{i}: {items}")         
        try:
            while True:
                command = int(input('Enter number to consume item. (0 to go back)\n\t'))
                return command   
        except ValueError:
            pass
    
    def useitem(self, listnum):
        if listnum is not 0:
            print(f'Consumed {self.slot[listnum].values()}')



    

        
