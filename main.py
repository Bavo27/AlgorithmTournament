import random
import tkinter as tk
from tkinter import ttk
import Algorithm

class MainApp:
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Algorithm Tournament")
        self.root.geometry("500x700")

        #-----MAIN MENU-------
        self.menu = tk.Frame(self.root)
        tk.Label(self.menu, text="Algorithm Tournament", font=("Arial", 30)).pack(pady=40)

        style = ttk.Style()
        style.configure("selected", background="lightgreen")

        self.selectedBttns = []
        self.selectedAlgs = []
        self.b1 = tk.Button(self.menu, text="Selection", command=lambda: self.selected(self.b1, "selection"))
        self.b2 = tk.Button(self.menu, text="Insertion", command=lambda: self.selected(self.b2, "insertion"))
        self.b3 = tk.Button(self.menu, text="Bubble", command=lambda: self.selected(self.b3, "bubble"))
        self.b4 = tk.Button(self.menu, text="Bavo", command=lambda: self.selected(self.b4, "bavo"))
        self.b5 = tk.Button(self.menu, text="Merge", command=lambda: self.selected(self.b5, "merge"))
        

        for bttn in (self.b1, self.b2, self.b3, self.b4, self.b5):
            bttn.pack(pady=10)
            bttn.config(highlightbackground="SystemButtonFace")

        tk.Button(self.menu,text="RUN", command=self.startTournament).pack(pady=10)


        #-----TOURNAMENT SCREEN-------
        self.tournament = tk.Frame(self.root)
        tk.Label(self.tournament, text="GO!", font=("Arial", 30)).pack(pady=40)
        tk.Button(self.tournament, text="BACK", command=self.mainMenu).pack(pady=10)

        self.w = 700
        self.h = 500

        self.canvas = tk.Canvas(self.tournament, width=self.w, height=self.h, bg="white")
        self.canvas.pack(fill="both", expand=True)


        self.menu.pack(fill="both", expand=True)
        self.root.mainloop()

    def selected(self, bttn, alg):
        if(bttn in self.selectedBttns):
            self.selectedBttns.remove(bttn)
            self.selectedAlgs.remove(alg)
            bttn.config(highlightbackground="SystemButtonFace")
        else:
            if(len(self.selectedBttns) >= 2):
                self.selectedBttns[0].config(highlightbackground="SystemButtonFace")
                self.selectedBttns[0] = self.selectedBttns[1]
                self.selectedAlgs[0] = self.selectedAlgs[1]
                self.selectedBttns[1] = bttn
                self.selectedAlgs[1] = alg
                bttn.config(highlightbackground="lightgreen")
            else:
                self.selectedBttns.append(bttn)
                self.selectedAlgs.append(alg)
                bttn.config(highlightbackground="lightgreen")
        
    def mainMenu(self):
        self.tournament.pack_forget()
        self.menu.pack(fill="both", expand=True)

    def startTournament(self):
        self.menu.pack_forget()
        self.tournament.pack(fill="both", expand=True)

        self.arr1 = list(range(1, 41))
        random.shuffle(self.arr1)
        self.arr2 = list(range(1, 41))
        random.shuffle(self.arr2)
        self.arraySteps1 = [[]]
        self.arraySteps2 = [[]]

        self.i = 0

        algo = Algorithm.Algorithm()
        self.arraySteps1 = algo.run(self.arr1, self.selectedAlgs[0])
        self.arraySteps2 = algo.run(self.arr2, self.selectedAlgs[1])

        self.visualizeSort(50)
        

    def visualizeSort(self, x):
        maxLen = max(len(self.arraySteps1), len(self.arraySteps2))
        def animate():
            if(self.i < len(self.arraySteps1)):
                self.visualize1(self.arraySteps1[self.i], x)
            if(self.i < len(self.arraySteps2)):
                self.visualize2(self.arraySteps2[self.i], x+200)
            if self.i < maxLen:
                self.root.after(15, animate)
                self.i += 1

        animate()
        #self.root.mainloop()
    
    def visualize1(self, array, x):
        xoffset = x
        yoffset = self.h - 100
        barwidth = 4
        barheight = 3
        self.canvas.delete("alg1")
        for i, num in enumerate(array):
            self.canvas.create_rectangle((barwidth*i)+xoffset,
                                        yoffset-(barheight*(num)),
                                        (barwidth*(i+1))+xoffset,
                                        yoffset,
                                        fill="black", outline="black", tag="alg1")
            
    def visualize2(self, array, x):
        xoffset = x
        yoffset = self.h - 100
        barwidth = 4
        barheight = 3
        self.canvas.delete("alg2")
        for i, num in enumerate(array):
            self.canvas.create_rectangle((barwidth*i)+xoffset,
                                        yoffset-(barheight*(num)),
                                        (barwidth*(i+1))+xoffset,
                                        yoffset,
                                        fill="black", outline="black", tag="alg2")

if __name__ == "__main__":
    MainApp()