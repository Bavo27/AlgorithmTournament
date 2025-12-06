import random
import tkinter as tk
import Algorithm

class MainApp:
    
    def __init__(self):
        self.arr1 = list(range(1, 41))
        random.shuffle(self.arr1)
        self.arr2 = list(range(1, 41))
        random.shuffle(self.arr2)
        self.arraySteps1 = [[]]
        self.arraySteps2 = [[]]

        self.root = tk.Tk()
        self.root.title("Algo Tournament")

        self.w = 700
        self.h = 500

        self.canvas1 = tk.Canvas(self.root, width=self.w, height=self.h, bg="white")
        self.canvas1.pack()

        #self.canvas2 = tk.Canvas(self.root, width=self.w, height=self.h, bg="white")
        #self.canvas2.grid(row=0, column=1)
        
        self.i = 0

        self.chooseAlgorithm()
        self.chooseAlgorithm2()
        self.visualizeSort(50)

    def chooseAlgorithm(self):
        algo1 = Algorithm.Algorithm() # initializes Algorithm class
        self.arraySteps1 = algo1.bubbleSort(self.arr1) # calls bubbleSort and gets steps for visualization
    
    def chooseAlgorithm2(self):
        algo2 = Algorithm.Algorithm() # initializes Algorithm class
        self.arraySteps2 = algo2.insertionSort(self.arr2) # calls bubbleSort and gets steps for visualization

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
        self.root.mainloop()
    
    def visualize1(self, array, x):
        xoffset = x
        yoffset = self.h - 100
        barwidth = 4
        barheight = 3
        self.canvas1.delete("alg1")
        for i, num in enumerate(array):
            self.canvas1.create_rectangle((barwidth*i)+xoffset,
                                        yoffset-(barheight*(num)),
                                        (barwidth*(i+1))+xoffset,
                                        yoffset,
                                        fill="black", outline="black", tag="alg1")
            
    def visualize2(self, array, x):
        xoffset = x
        yoffset = self.h - 100
        barwidth = 4
        barheight = 3
        self.canvas1.delete("alg2")
        for i, num in enumerate(array):
            self.canvas1.create_rectangle((barwidth*i)+xoffset,
                                        yoffset-(barheight*(num)),
                                        (barwidth*(i+1))+xoffset,
                                        yoffset,
                                        fill="black", outline="black", tag="alg2")


if __name__ == "__main__":
    MainApp()