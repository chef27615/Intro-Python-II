class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def can_eat(self):
        return False
    def pick_up(self):
        return(f'you picked up {self.name}')
    def drop_off(self):
        return(f'you dropped {self.name}')
    


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories
    def can_eat(self):
        return True