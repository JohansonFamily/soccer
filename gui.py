import tkinter as tk
#from PIL import ImageTk  # , Image
import database

def manageTeam():
    None

class startingScreen:
    def __init__(self, root):
        self.root = root
        self.frmSplash = tk.Frame(self.root)
        self.frmSplash.grid(row=0, sticky='NSEW')

        self.listTeams()
        self.queryTeams()

    def listTeams(self):
        self.frmSplash.grid_rowconfigure(0, weight=1)
        self.frmSplash.grid_rowconfigure(1, weight=1)
        self.frmSplash.grid_rowconfigure(2, weight=2)
        self.frmSplash.grid_columnconfigure(0, weight=1)
        self.frmSplash.grid_columnconfigure(1, weight=1)
        self.lbl = tk.Label(self.frmSplash, text="Soccer Coach", font='Arial 38')
        self.lbl.grid(row=0, columnspan=2, sticky='S', pady=20)
        self.lbl = tk.Label(self.frmSplash, text="Which team would you like to manage?", font="Arial 24")
        self.lbl.grid(row=1, columnspan=2, sticky='N')

    def queryTeams(self):
        teamList = []

        db = database.DB()
        teamList = db.getTeams()
        db.close()

        for i in range(len(teamList)):
            lbl = tk.Button(self.frmSplash, text=teamList[i], width=30, height=10,
                            command= lambda team=teamList[i]: self.selectTeam(team))
            lbl.grid(row=2, column=i, sticky='N')

    def selectTeam(self, team):
        self.frmSplash.destroy()
        teamScreen(self.root, team)

class teamScreen:
    def __init__(self, root, team):
        self.frame = tk.Frame(root)
        self.team = team
        self.frame.grid(row=0)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        lbl = tk.Label(self.frame, text=self.team[0])
        lbl.grid(row=0)