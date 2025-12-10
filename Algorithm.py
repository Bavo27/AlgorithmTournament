import random
import tkinter as tk
import time


class Algorithm:
    def __init__(self):
        self.arraySteps = [[]]  # to store steps for visualization
        self.timeCounter = 0

    def run(self, arr, algorithm):
        result = []
        startTime = time.time()
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
                self.mergeSort(arr)
                result = self.arraySteps
            case "heap":
                return self.heapSort(arr)
            case "radix":
                return self.radixSort(arr)
            case "bogo":
                return self.bogoSort(arr)
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return result
    
    def bubbleSort(self, arr):
        startTime = time.time()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.arraySteps.append(arr.copy())
            
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return self.arraySteps # return the steps for visualization

    def bavoSort(self, arr):
        startTime = time.time()
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                curr = arr[j]
                if arr[j] > arr[j+1]:
                    arr[j] = arr[j+1]
                    arr[j+1] = curr
                    self.arraySteps.append(arr.copy())
            
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return self.arraySteps
    
    def insertionSort(self, arr):
        startTime = time.time()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                self.arraySteps.append(arr.copy())
            arr[j + 1] = key
        
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return self.arraySteps

    def selectionSort(self, arr):
        startTime = time.time()
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.arraySteps.append(arr.copy())
        
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return self.arraySteps
    

    def mergeSort(self, arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1

        if left < right:
            mid = (left + right) // 2

            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)

            self.merge(arr, left, mid, right)
    
    def merge(self, arr, left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            self.arraySteps.append(arr.copy())

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            self.arraySteps.append(arr.copy())

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            self.arraySteps.append(arr.copy())  
    
    
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
        self.arraySteps.append(arr.copy())

    def heapSort(self, arr):
        startTime = time.time()
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return self.arraySteps

    def radixSort(self, arr):
        startTime = time.time()
        maxNum = max(arr)
        exp = 1
        
        while maxNum // exp > 0:
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            
            for num in arr:
                index = (num // exp) % 10
                count[index] += 1
                
            for i in range(1,10):
                count[i] += count[i-1]
            
            for i in range(n - 1, -1, -1):
                index = (arr[i]// exp) %10
                output[count[index] - 1] = arr[i]
                count[index] -= 1
                
            for i in range(n):
                arr[i] = output[i]
            
                self.arraySteps.append(arr.copy())
            exp *= 10
        
        endTime = time.time()
        self.timeCounter = endTime - startTime
        return self.arraySteps
    
    def bogoSort(self,arr, maxIters = 100):
        iters = 0
        while True:
            iters += 1
            if iters > maxIters:
                break
            sorted = True
                
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    sorted = False
                    break
            
            if sorted:
                break
            n = len(arr)
            for i in range(n):
                r = random.randint(0, n-1)
                arr[i], arr[r] = arr[r], arr[i]
                self.arraySteps.append(arr.copy())
        return self.arraySteps
    
    def getStepCounter(self):
        return self.stepCounter

    def getTimeCounter(self):
        return self.timeCounter
    
    
Algorithm()