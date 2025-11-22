import random
import tkinter as tk
import time



class Algorithm:
    def __init__(self):
        arr = list(range(20, 31))
        self.array = []
        random.shuffle(arr)
        self.bubbleSort(arr)
        self.i = 0
        self.visualizeSort(self.array)
        
    
    def visualizeSort(self, arr):
        root = tk.Tk()
        root.title("Lorenzo")

        w = 500
        h = 500

        canvas = tk.Canvas(root, width=w, height=h, bg="white")
        canvas.pack()


        xoffset = 25
        yoffset = h - 100
        barwidth = 4
        barheight = 3

        # arrays = []

        def visualize(array):
            canvas.delete("all")
            for i, num in enumerate(array):
                canvas.create_rectangle((barwidth*i)+xoffset,
                                            yoffset-(barheight*(num)),
                                            (barwidth*(i+1))+xoffset,
                                            yoffset,
                                            fill="black", outline="black")
                
        def animate():
            visualize(arr[self.i])

            root.after(10, animate)
            self.i += 1

        animate()
        root.mainloop()

    
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.array.append(arr.copy())
    
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr
    
    def bavoSort(self, arr):
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                curr = arr[j]
                if arr[j] > arr[j+1]:
                    arr[j] = arr[j+1]
                    arr[j+1] = curr
        return arr
    
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

if __name__ == "__main__":
    Algorithm()