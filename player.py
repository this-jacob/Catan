class Player:

    def __init__(self, name):
        self.name = name
        self.vps = 0
        self.knights = 0

        self.resources = {}
        self.developments = {}

        self.settlements = []
        self.cities = []
        self.roads = []

        self.resources['wool'] = 0
        self.resources['wheat'] = 0
        self.resources['brick'] = 0
        self.resources['stone'] = 0
        self.resources['wood'] = 0

        self.developments['vps'] = 0
        self.developments['yearofplenty'] = 0
        self.developments['monopoly'] = 0
        self.developments['roads'] = 0
        self.developments['knight'] = 0

        return
