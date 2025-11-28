import random
import tkinter as tk
import time


class Algorithm:
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

        self.bubbleSort(arr1)
        self.i = 0
        self.j = 0
        self.visualizeSort(self.array1, 50)
         
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
    
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.array1.append(arr.copy())
    
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
        self.array.append(arr.copy())
    
    def bavoSort(self, arr):
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                curr = arr[j]
                if arr[j] > arr[j+1]:
                    arr[j] = arr[j+1]
                    arr[j+1] = curr
        print("completed")
    
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        self.array.append(arr.copy())

    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.array.append(arr.copy())


Algorithm()