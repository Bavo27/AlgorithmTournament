
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
            
#Test
if __name__ == "__main__":
    A = [-1, 5, 20, 8, 300, 2]
merge_sort(A, 0, len(A) - 1)
print(A)  # should be sorted
