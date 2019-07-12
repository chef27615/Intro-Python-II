# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room_name, room_desc):
        self.title = room_name
        self.desc = room_desc
        self.n = None
        self.w = None
        self.s = None
        self.e = None
        self.items = []
    def __str__(self):
        str = f"""
            \n----------------------------------
              \n{self.title}
              \n   {self.desc}\n
              \n {self. _get_exits_string()} 
              \n Item in the room: {self._get_item_string()}
            """
        return str
    def _get_item_string(self):
        if len(self.items) > 0:
            return ', '.join([item.name for item in self.items])
        else:
            return ''
    def _get_exits_string(self):
        exits = []
        if self.n is not None:
            exits.append('n')
        if self.s is not None:
            exits.append('s')
        if self.e is not None:
            exits.append('e')
        if self.w is not None:
            exits.append('w')
        return 'Exits: ' + ', '.join(exits)