import random
import tkinter as tk
from tkinter import ttk
import Algorithm
import time

class MainApp:
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Algorithm Tournament")
        self.root.geometry("900x700")

        #-----MAIN MENU-------
        self.menu = tk.Frame(self.root)
        tk.Label(self.menu, text="Algorithm Tournament", font=("Arial", 30)).pack(pady=40)

        style = ttk.Style()
        style.configure("selected", background="lightgreen")

        self.selectedBttns = []
        self.selectedAlgs = []
        self.selectedBigOs = []
        self.b1 = tk.Button(self.menu, text="Selection", command=lambda: self.selected(self.b1, "selection", "O(n^2)"))
        self.b2 = tk.Button(self.menu, text="Insertion", command=lambda: self.selected(self.b2, "insertion", "O(n^2)"))
        self.b3 = tk.Button(self.menu, text="Bubble", command=lambda: self.selected(self.b3, "bubble", "O(n^2)"))
        self.b4 = tk.Button(self.menu, text="Bavo", command=lambda: self.selected(self.b4, "bavo", "O(n+k)"))
        self.b5 = tk.Button(self.menu, text="Merge", command=lambda: self.selected(self.b5, "merge", "O(nlogn)"))
        self.b6 = tk.Button(self.menu, text="Heap", command=lambda: self.selected(self.b6, "heap", "O(nlogn)"))
        self.b7 = tk.Button(self.menu, text="Radix", command=lambda: self.selected(self.b7, "radix", "O(nk)"))
        self.b8 = tk.Button(self.menu, text="Bogo", command=lambda: self.selected(self.b8, "bogo", "O(n*n!)"))
        for bttn in (self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8):
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

        self.time1 = 0
        self.time2 = 0
        
        self.sort1Status = False
        self.sort2Status = False

        self.root.mainloop()


    def selected(self, bttn, alg, oh):
        if(bttn in self.selectedBttns):
            self.selectedBttns.remove(bttn)
            self.selectedAlgs.remove(alg)
            self.selectedBigOs.remove(oh)
            bttn.config(highlightbackground="SystemButtonFace")
        else:
            if(len(self.selectedBttns) >= 2):
                self.selectedBttns[0].config(highlightbackground="SystemButtonFace")
                self.selectedBttns[0] = self.selectedBttns[1]
                self.selectedAlgs[0] = self.selectedAlgs[1]
                self.selectedBigOs[0] = self.selectedBigOs[1]
                self.selectedBttns[1] = bttn
                self.selectedAlgs[1] = alg
                self.selectedBigOs[1] = oh
                bttn.config(highlightbackground="lightgreen")
            else:
                self.selectedBttns.append(bttn)
                self.selectedAlgs.append(alg)
                self.selectedBigOs.append(oh)
                bttn.config(highlightbackground="lightgreen")
        
    def mainMenu(self):
        self.tournament.pack_forget()
        self.menu.pack(fill="both", expand=True)
        self.canvas.delete("end")

    def startTournament(self):
        if(len(self.selectedAlgs) < 2):
            return
        self.menu.pack_forget()
        self.tournament.pack(fill="both", expand=True)

        self.arr1 = list(range(1, 101))
        random.shuffle(self.arr1)

        arrayText = "["+ str(self.arr1[0])
        
        for i in range(1, len(self.arr1)):
            arrayText += ", " + str(self.arr1[i])
        arrayText += "]"

        tk.Label(self.tournament, text="Array to sort: " + arrayText, font=("Arial", 10)).pack()

        self.arraySteps1 = [[]]
        self.arraySteps2 = [[]]

        self.i = 0
        self.alg1Steps = 0
        self.alg2Steps = 0

        self.sort1 = Algorithm.Algorithm()
        self.arraySteps1 = self.sort1.run(self.arr1.copy(), self.selectedAlgs[0])
        self.sort2 = Algorithm.Algorithm() #so that the sort counter and timer doesn't cross
        self.arraySteps2 = self.sort2.run(self.arr1.copy(), self.selectedAlgs[1])
        self.time1 = self.sort1.getTimeCounter()
        self.time2 = self.sort2.getTimeCounter()
        self.visualizeSort(20)
        

    def visualizeSort(self, x):
        maxLen = max(len(self.arraySteps1), len(self.arraySteps2))
        def animate():
            if(self.i < len(self.arraySteps1)):
                self.visualize1(self.arraySteps1[self.i], x)
            if(self.i < len(self.arraySteps2)):
                self.visualize2(self.arraySteps2[self.i], x+450)
            if self.i < maxLen:
                self.root.after(1, animate)
                self.i += 1
            else:
                self.endPage()
                

        animate()
    
    def visualize1(self, array, x):
        startTime = time.time()
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
            
        endTime = time.time()
        #self.time1 += endTime - startTime
        
        self.alg1Steps += 1
        
        #self.canvas.create_text(x+100, 50, text="Algorithm 1 time: " + "{:.5f}".format(self.time1), font=("Arial", 11), tag="alg1", fill="black")
        self.canvas.create_text(x+100, 70, text="Algorithm 1 steps: " + str(self.alg1Steps), font=("Arial", 11), tag="alg1", fill="black")
        t = self.selectedAlgs[0].capitalize() + " sort: " + self.selectedBigOs[0]
        self.canvas.create_text(x+100, 35, text = t, font=("Arial", 11), tag="alg1", fill="black")

            
    def visualize2(self, array, x):
        startTime = time.time()
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
        
        endTime = time.time()
        #self.time2 += (endTime - startTime)*10
        # self.time2 = round(self.time2)
        
        self.alg2Steps += 1
        
        #self.canvas.create_text(x+100, 50, text="Algorithm 2 time: " + "{:.5f}".format(self.time2), font=("Arial", 11), tag="alg2", fill="black")
        self.canvas.create_text(x+100, 70, text="Algorithm 2 steps: " + str(self.alg2Steps), font=("Arial", 11), tag="alg2", fill="black")
        t = self.selectedAlgs[1].capitalize() + " sort: " + self.selectedBigOs[1]
        self.canvas.create_text(x+100, 35, text = t, font=("Arial", 11), tag="alg2", fill="black")


    def endPage(self):
        self.canvas.create_text(150, 100, text= self.selectedAlgs[0] + " finished in " + str(self.sort1.getTimeCounter()), font=("Arial", 11), tag="end", fill="black")
        self.canvas.create_text(550, 100, text= self.selectedAlgs[1] + " finished in " + str(self.sort2.getTimeCounter()), font=("Arial", 11), tag="end", fill="black")

        
        
        

if __name__ == "__main__":
    MainApp()