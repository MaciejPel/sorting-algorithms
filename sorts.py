import random

def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j>=0 and arr[j]>key: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def mergeSort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1

def selectionSort(arr):
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
 
def partition(arr, l, h):
    i = ( l - 1 )
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)
def quickSortIterative(arr, l, h):
    print(arr)
    if len(arr)<=1:
        return arr
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition( arr, l, h )
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def partitionRandom(arr, l, h):
    i = ( l - 1 )
    pivot = random.randint(l, h) # <-- tu zmieniac
    x = arr[pivot]
    arr[pivot], arr[h] = arr[h], arr[pivot]
    for j in range(l, h):
        if   arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def quickSortRandom(arr, l, h):
    if len(arr)<=1:
        return arr
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partitionRandom( arr, l, h )
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def partitionMiddle(arr, l, h):
    i = ( l - 1 )
    pivot = (h+l)//2
    x = arr[pivot]
    arr[pivot], arr[h] = arr[h], arr[pivot]
    for j in range(l, h):
        if   arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def quickSortMiddle(arr, l, h):
    if len(arr)<=1:
        return arr
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partitionMiddle( arr, l, h )
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

# def partition(arr,l,h):
#     i = ( l - 1 )
#     x = arr[h]
#     for j in range(l , h):
#         if   arr[j] <= x:
#             i = i+1
#             arr[i],arr[j] = arr[j],arr[i]
  
#     arr[i+1],arr[h] = arr[h],arr[i+1]
#     return (i+1)

# def quickSortIterative(arr,l,h):
#     size = h - l + 1
#     stack = [0] * (size)
#     top = -1
#     top = top + 1
#     stack[top] = l
#     top = top + 1
#     stack[top] = h
#     while top >= 0:
#         h = stack[top]
#         top = top - 1
#         l = stack[top]
#         top = top - 1
#         p = partition( arr, l, h )
#         if p-1 > l:
#             top = top + 1
#             stack[top] = l
#             top = top + 1
#             stack[top] = p - 1
#         if p+1 < h:
#             top = top + 1
#             stack[top] = p + 1
#             top = top + 1
#             stack[top] = h

###################################
# QUICKSORT RECURSIVE
##################################
# def partition(arr, low, high): 
#     i = (low-1)
#     pivot = arr[high]
#     for j in range(low, high): 
#         if arr[j] <= pivot: 
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i] 
#     arr[i+1], arr[high] = arr[high], arr[i+1] 
#     return (i+1) 
  
# def quickSort(arr, low=0, high=None): 
#     if high is None:
#         high = len(arr) - 1
#     if len(arr) == 1: 
#         return arr 
#     elif low < high: 
#         pi = partition(arr, low, high) 
#         quickSort(arr, low, pi-1) 
#         quickSort(arr, pi+1, high)

#################################
# INSERTION C
#################################
# def insertionC(arr):
#     temp=0
#     for i in range(0, len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp 

#################################
# INSERTION 0
#################################
# def insertion0(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1]=arr[j+1], arr[j]

#################################
# BUBBLE
#################################
# def bubbleSort(arr): 
#     for i in range(len(arr)-1): 
#         for j in range(0, len(arr)-i-1): 
#             if arr[j] > arr[j+1] : 
#                 arr[j], arr[j+1] = arr[j+1], arr[j] 

#################################
# BOGO
#################################
# def bogoSort(arr):
#     while (is_sorted(arr)== False): 
#         shuffle(arr) 
# def is_sorted(arr): 
#     n = len(arr) 
#     for i in range(0, n-1): 
#         if (arr[i] > arr[i+1] ): 
#             return False
#     return True
# def shuffle(arr): 
#     n = len(arr) 
#     for i in range (0,n): 
#         r = random.randint(0,n-1) 
#         arr[i], arr[r] = arr[r], arr[i] 

#################################
# Shell
#################################
# def shellSort(arr): 
#     n = len(arr) 
#     gap = n//2
#     while gap > 0: 
#         for i in range(gap,n): 
#             temp = arr[i] 
#             j = i 
#             while  j >= gap and arr[j-gap] >temp: 
#                 arr[j] = arr[j-gap] 
#                 j -= gap 
#             arr[j] = temp 
#         gap //= 2

