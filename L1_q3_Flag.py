from tkinter import Tk, Canvas, Frame, BOTH
from math import pi, cos, sin

k, l, m, n, o=479, 180, 465, 232, 347

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Flag")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)


        def Sun(x, y, r, e, l, b):
            p, a, h=[], 2*pi/e, r*l
            c, d=[0, -a/2][b], [a/2, 0][b]
            for i in range(e):
                p+=[(x+r*cos(i*a+c), y+r*sin(i*a+c)), (x+h*cos(i*a+d), y+h*sin(i*a+d))]
            canvas.create_polygon(p, fill="white")

        # Step 1: Drawing blue triangular polygon

        #outer polygon with blue color
        canvas.create_polygon((0, 0), (393, 246), (144, 246), (375, k), (0, k), fill="#003893")

        #Step 2: Filling red color in blue polygon
        # inner polygon with red color over blue polygon
        canvas.create_polygon((14, 25), (o, n), (110, n), (o, m), (14, m), fill="#DC143C") 
        
        #Step 3: Drawing moon 
        #Semi cricle for the moon
        canvas.create_arc(31, 84, 163, 220, start=-180, extent=l, fill="#ffffff", outline="#ffffff")
        
        #another smaller semicircle filled red color over the previous semicircle to make it small
        canvas.create_arc(26, 60, 168, 190, start=-180, extent=l, fill="#DC143C", outline="#DC143C")
        
        #Sun shape above the moon semicicle
        Sun(96, 182, 40, 16, .7, 1) 

        #Step4: Drawing Sun
        #Sun Shape at lower part
        Sun(96, o, 68, 12, .6, 0) 
        
        

        canvas.pack(fill=BOTH, expand=1)



root = Tk()
ex = Example()
root.geometry("600x600")
root.mainloop()
