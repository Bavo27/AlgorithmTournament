import random
import tkinter as tk
import time



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

arrays = []

def visualize(array):
    canvas.delete("all")
    for i, num in enumerate(array):
        canvas.create_rectangle((barwidth*i)+xoffset,
                                    yoffset-(barheight*(num)),
                                    (barwidth*(i+1))+xoffset,
                                    yoffset,
                                    fill="black", outline="black")


def merge_sort(A, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(A, low, mid)
        merge_sort(A, mid+1, high)
        merge(A, low, mid, high)
        

def merge(A, low, mid, high):
    n1 = mid - low +1
    n2 = high - mid
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = A[low + i]
    for j in range(n2):
       R[j] = A[mid + 1 + j]
    
    #arrays.append(A)
       
    i = 0
    j = 0
    
    for k in range(low, high + 1):
        if i >= n1:
            A[k] = R[j]
            j += 1
        elif j >= n2:
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        arrays.append(A.copy())
        
            


#root.after(100, visualize, A)
A = list(range(1,101))
random.shuffle(A)

def bavoSort(arr):
    for i in range(len(arr)):
        for j in range(i - 1, -1, -1):
            curr = arr[j]
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = curr
                arrays.append(arr.copy())
    #return arr



merge_sort(A, 0, len(A) - 1)

#bavoSort(A)

i = -1
def animate():
    global i
    i = i + 1
    array = arrays[i]
    visualize(array)

    root.after(3, animate)

animate()
root.mainloop()

    


