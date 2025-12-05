import random
import tkinter as tk
import time
import main

class Algorithm:
    def __init__(self):
        self.arraySteps = [[]]  # to store steps for visualization
    

    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.arraySteps.append(arr.copy())
        return self.arraySteps # return the steps for visualization
        
    
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