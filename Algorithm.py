import random
import tkinter as tk
import time
import main

class Algorithm:
    def __init__(self):
        self.arraySteps = [[]]  # to store steps for visualization
        self.stepCounter = 0
        self.timeCounter = 0

    def run(self, arr, algorithm):
        self.arraySteps = [[]]
        match algorithm:
            case "bubble":
                return self.bubbleSort(arr)
            case "bavo":
                return self.bavoSort(arr)
            case "insertion":
                return self.insertionSort(arr)
            case "selection":
                return self.selectionSort(arr)
            case "merge":
                return self.mergeSort(arr)
    
    def bubbleSort(self, arr):
        # timeStart = time.time()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.arraySteps.append(arr.copy())
                    self.stepCounter += 1
    
        # timeStop = time.time()
        # self.timeCounter = timeStop - timeStart
        return self.arraySteps # return the steps for visualization

    def bavoSort(self, arr):
        # timeStart = time.time()
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                curr = arr[j]
                if arr[j] > arr[j+1]:
                    arr[j] = arr[j+1]
                    arr[j+1] = curr
                    self.arraySteps.append(arr.copy())
                    self.stepCounter += 1
        # timeStop = time.time()
        # self.timeCounter = timeStop - timeStart
        return self.arraySteps
    
    def insertionSort(self, arr):
        # timeStart = time.time()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                self.arraySteps.append(arr.copy())
                self.stepCounter += 1
            arr[j + 1] = key
        # timeStop = time.time()
        # self.timeCounter = timeStop - timeStart
        return self.arraySteps

    def selectionSort(self, arr):
        # timeStart = time.time()
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.arraySteps.append(arr.copy())
            self.stepCounter += 1
        # timeStop = time.time()
        # self.timeCounter = timeStop - timeStart
        return self.arraySteps
    
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
            
            self.arraySteps.append(arr.copy())
        return self.arraySteps
    
    def getStepCounter(self):
        return self.stepCounter

    def getTimeCounter(self):
        return self.timeCounter

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[l] > arr[largest]:
            largest = l
        
        if r < n and arr[r] > arr[largest]:
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
            
    def heapSort(arr):
        n = len(arr)
        
        for i in range(n // 2, -1, -1, -1):
            heapify(arr, n , i)
        
        for i in range(n - 1, 0 , 1):
           arr[i], arr[0] = arr[0], arr[i]
           heapify(arr, i, 0) 
           

Algorithm()