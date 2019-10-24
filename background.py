import Tkinter as Tk
from rocket import Rocket

rocket = Rocket

class Background():
    def __init__(self):
        self.a = Tk.Tk()
        self.rocket = rocket
        canvas = Tk.Canvas(self.a, width=1000, height=800)
        self.canvas = canvas
        canvas.create_rectangle(0, 700, 1000, 800, fill="grey")
        canvas.pack()
        rocket.pack()
        self.a.mainloop()
        print "background created"
