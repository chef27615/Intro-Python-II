# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room_name, room_desc):
        self.room_name = room_name
        self.room_desc = room_desc
        self.n = None
        self.w = None
        self.s = None
        self.e = None
    def __str__(self):
        return f'{self.room_name}, {self.room_desc}'
