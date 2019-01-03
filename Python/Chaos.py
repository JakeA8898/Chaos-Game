import tkinter as tk
import random

class chaos(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x800")
        self.startPoints = []
    
        self.w = tk.Canvas(self,width = 800,height = 800,bg = 'black')
        self.w.pack()
        self.bind("<Button-1>",self.plotPoint)
        self.bind ("s", self.start)



    def plotPoint(self,event):
        self.w.create_rectangle(event.x,event.y,event.x+1,event.y+1,outline = 'white')
        self.startPoints.append([event.x,event.y])

    
    def start(self,event):
        self.pointS = [self.startPoints[-1][0],self.startPoints[-1][1]]
        self.startPoints.pop()
        self.chaosLoop()



    def chaosPoint(self):
        i = random.randint(0,len(self.startPoints)-1)

        self.pointS[0] = (self.pointS[0] + self.startPoints[i][0])/2
        self.pointS[1] = (self.pointS[1] + self.startPoints[i][1])/2
        self.w.create_rectangle(self.pointS[0],self.pointS[1],self.pointS[0]+1,self.pointS[1]+1,outline = 'white')
        
    



    def chaosLoop(self):
        self.after(1,self.chaosLoop)
        self.chaosPoint()

    
if __name__ == "__main__":
    chaos().mainloop()
        