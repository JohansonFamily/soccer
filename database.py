import sqlite3

class DB:
	DB_LOCATION = "soccer.db"

	def __init__(self):
		self.connection = sqlite3.connect(self.DB_LOCATION)
		self.cursor = self.connection.cursor()

	def getTeams(self):
		self.cursor.execute("""
				SELECT name, year
				FROM team
				WHERE active = true
				;""")
		rows = self.cursor.fetchall()
		return rows

	def addTeam(self, name, year, num_players):
		team = [name, year, num_players, True]
		sql = "INSERT INTO team values (?,?,?,?)"
		self.cursor.execute(sql, team)

	def create_tables(self):
		self.cursor.execute("""CREATE TABLE team (
				name text,
				year text,
				num_players integer,
				active boolean
	
				);""")

	def drop_tables(self):
		self.cursor.execute("""
			DROP TABLE IF EXISTS team;
			"""
			)

	def commit(self):
		self.connection.commit()

	def close(self):
		self.connection.commit()
		self.connection.close()

	def __enter__(self):
		return self

	def __exit__(self, ext_type, exc_value, traceback):
		self.cursor.close()
		if isinstance(exc_value, Exception):
			self.connection.rollback()
		else:
			self.connection.commit()
		self.connection.close()