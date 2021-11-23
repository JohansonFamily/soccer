class player:
    def __init__(self, name):
        self.name = name

    def deletePlayer


class team:
    def __init__(self, name):
        self.name=name
        self.db = database.DB()
        players = []
        players = db.getPlayers()

    def close(self):
        self.db.close()
