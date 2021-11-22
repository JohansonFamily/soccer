from tkinter import *
import gui

root = Tk()
root.title('Soccer Plan')
root.geometry("1500x1000+100+100")
# root.config(bg='white')


def escape(e):
	try:
		root.quit()
	except Exception as exc:
		print(str(e.type) + ": " + str(exc))


root.bind("<Escape>", escape)

# Add fonts for all the widgets
root.option_add("*Font", "Arial 14")

# Setup initial root dimensions to span width of window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

gui.startingScreen(root)

mainloop()
