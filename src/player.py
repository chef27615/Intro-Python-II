# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.strength = 10
        self.current_room = starting_room
        self.items = []
    def move(self, direction):
        if getattr(self.current_room, f'{direction}') is not None:
            self.current_room = getattr(self.current_room, f'{direction}')
            print(self.current_room)
        else:
            print('cannot move to this direction', '\n')
    def _get_item_str(self):
        if len(self.items) > 0:
            return ', '.join([item.name for item in self.items])
        else:
            return ''
    def get_inventory(self):
        # print(f'Your strength is {self.strength}')
        if len(self.items) > 1:
            print('You are carrying: \n' + ', '.join([item.name for item in self.items])+ '\n')
        else:
            print('you have nothing')
    def eat(self, item_name):
        item_to_eat = None
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item_to_eat = item
                break
            if item_to_eat is None:
                print(f'Did not find {item.name}')
                return
            if item_to_eat.can_eat():
                self.strength += item.item_to_eat.calories
                print(f'you eat{item_name}')
                self.items.remove(item_to_eat)
            else:
                print(f'You cannot eat {item_name}')
                return
