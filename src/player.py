# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, sta_r):
        self.cur_r = sta_r
        self.bag = []

    def inv(self):
        if len(self.bag)>0:
            for item in self.bag:
                if item is None:
                    pass
                else:
                    print(item)
        else:
            print('nothing in your bag')
    
    def look(self):
        if len(self.cur_r.items)>0:
            for item in self.cur_r.items:
                print(item)
        