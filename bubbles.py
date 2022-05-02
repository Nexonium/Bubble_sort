
array = [2,6,8,1,6,9,0,3,1,6]
print("Unsorted array is: ")
print(array)

def bubbleSort(array):
    l = len(array)
    for item in range(l):
        for i in range(0, l-item-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

bubbleSort(array)

print("Sorted array is: ")
print(array)