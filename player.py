class Player:

    def __init__(self, name):
        self.name = name
        self.resources = {}
        self.setlements = []
        self.cities = []
        self.resources['wool'] = 0
        self.resources['wheat'] = 0
        self.resources['brick'] = 0
        self.resources['stone'] = 0
        self.resources['wood'] = 0
        return
