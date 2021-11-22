import sqlite3

class DB:
	def __init__(self):
		self.dbase = 'soccer.db'

		self.conn()

	def conn(self):
		global conn
		global c

		conn = sqlite3.connect(self.dbase)
		c = conn.cursor()

	def getTeams(self):
		c.execute("""
				SELECT name, year
				FROM team
				WHERE active = true
				;""")
		rows = c.fetchall()
		return rows

	def addTeam(self, name, year, num_players):
		team = [name, year, num_players, True]
		sql = "INSERT INTO team values (?,?,?,?)"
		print(sql)
		c.execute(sql, team)

	def create_tables(self):
		c.execute("""CREATE TABLE team (
				name text,
				year text,
				num_players integer,
				active boolean
	
				);""")

	def drop_tables(self):
		c.execute("""
			DROP TABLE IF EXISTS team;
			"""
			)

	def commit(self):
		conn.commit()

	def close(self):
		conn.commit()
		conn.close()

