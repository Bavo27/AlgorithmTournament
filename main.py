import random
import tkinter as tk
import Algorithm

class MainApp:
    
    def __init__(self):
        self.arr1 = list(range(10, 21))
        random.shuffle(self.arr1)
        self.arraySteps = [[]]

        self.root = tk.Tk()
        self.root.title("Algo Tournament")

        self.w = 700
        self.h = 500

        self.canvas = tk.Canvas(self.root, width=self.w, height=self.h, bg="white")
        self.canvas.pack()
        
        self.i = 0

        self.chooseAlgorithm()
        self.visualizeSort(self.arraySteps, 50)

    def chooseAlgorithm(self):
        algo1 = Algorithm.Algorithm() # initializes Algorithm class
        self.arraySteps = algo1.bubbleSort(self.arr1) # calls bubbleSort and gets steps for visualization
        

    def visualizeSort(self, arr, x):
        def animate():
            self.visualize(arr[self.i], x)

            self.root.after(10, animate)
            if self.i < len(arr) - 1:
                self.i += 1

        animate()
        self.root.mainloop()
    
    def visualize(self, array, x):
        xoffset = x
        yoffset = self.h - 100
        barwidth = 4
        barheight = 3
        self.canvas.delete("all")
        for i, num in enumerate(array):
            self.canvas.create_rectangle((barwidth*i)+xoffset,
                                        yoffset-(barheight*(num)),
                                        (barwidth*(i+1))+xoffset,
                                        yoffset,
                                        fill="black", outline="black")


if __name__ == "__main__":
    MainApp()