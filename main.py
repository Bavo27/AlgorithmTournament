import random
import tkinter as tk
import time



root = tk.Tk()
root.title("Lorenzo")

w = 500
h = 500

canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack()


xoffset = 100
yoffset = h - 100
barwidth = 10
barheight = 10

def visualize(array):
    canvas.delete("all")
    for i, num in enumerate(array):
        canvas.create_rectangle((barwidth*i)+xoffset,
                                yoffset-(barheight*(num)),
                                (barwidth*(i+1))+xoffset,
                                yoffset,
                                fill="black", outline="black")

nums = list(range(1,11))
random.shuffle(nums)

root.after(1000, visualize, nums)
root.mainloop()


# def swap(A, a, b):
#     print("swapping ", a, " and ", b)
#     for i in range(0, len(A)):
#         if(A[i] == a):
#             break
#     for j in range(0, len(A)):
#         if(A[j] == b):
#             break
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp
#     print(A)

# def quicksort(nums):
#     print(nums)
#     pivot = 5
#     temp = nums[pivot]
#     nums[pivot] = nums[9]
#     nums[9] = temp
#     pivot = 9
#     print(nums)

#     i = 0
#     j = 8
#     while True:
#         while(nums[i] <= nums[pivot]):
#             i = i + 1
#         while(nums[j] >= nums[pivot]):
#             j = j - 1

#         print("i ", i)
#         print("j ", j)
        
#         if(i > j):
#             swap(nums, i, pivot)
#             pivot = i
#             print(nums)
#             break

#         swap(nums, i, j)

#         print(nums)

# def quicksort(A, low, high):
#     if(low < high):
#         pivot_location = partition(A, low, high)
#         quicksort(A, low, pivot_location)
#         #quicksort(A, pivot_location+1, high)

# def partition(A, low, high):
#     pivot = A[low]
#     print("pivot: ", pivot)
#     leftwall = low
#     print("leftwall: ", leftwall)
#     for i in range(low+1, high+1):
#         print("i: ", i)
#         if (A[i] < pivot):
#             swap(A, A[i], A[leftwall])
#             leftwall = leftwall + 1
#             print("leftwall: ", leftwall)
#     swap(A, pivot, A[leftwall])
#     return(leftwall)

#nums = [5,10,9,4,8,6,7,1,2,3]
# print(nums)
# quicksort(nums, 0, 9)

    


