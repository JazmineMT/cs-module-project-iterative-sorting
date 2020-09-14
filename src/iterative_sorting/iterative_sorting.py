

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        # cur_index = i
        # smallest_index = cur_index
        min_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


        # TO-DO: swap
        # Your code here

        
    return arr 


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for passnum  in range(len(arr) -1 , 0 , -1):
        for i in range(passnum):
            if arr[i] > arr[ i + 1]:
                temp = arr[i]
                arr[i] = arr[ i + 1]
                arr[i + 1] = temp
    

    return arr

# faster bubble search -> shortbubbleSort
#it tests to see if it's been sorted therefore the final search through it not neccessary 
def short_bubble_sort(arr):
    exchanges = True
    passnum = len(arr) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if arr[i] > arr[ i + 1]:
                exchanges = True
                temp = arr[i]
                arr[i] =  arr[i + 1]
                arr[ i + 1] = temp
        passnum = passnum - 1
    return arr 



'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(array, maxval= None):
    """in-place counting sort"""
    if maxval == None:
        return array
    
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array
