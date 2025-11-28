import random
import tkinter as tk
import Algorithm

class MainApp:
    
    def __init__(self):
        arr1 = list(range(10, 31))
        arr2 = list(range(10, 31))
        self.array1 = []
        self.array2 = []
        random.shuffle(arr1)
        random.shuffle(arr2)

        self.root = tk.Tk()
        self.root.title("Algo Tournament")

        self.w = 700
        self.h = 500

        self.canvas = tk.Canvas(self.root, width=self.w, height=self.h, bg="white")
        self.canvas.pack()

        self.chooseAlgorithm()

    def chooseAlgorithm(self):
        Algorithm.Algorithm


if __name__ == "__main__":
    MainApp()