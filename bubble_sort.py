# Bubble sort v.0.4
# Made by the greatest programmer of all time

array = list()
array_length = int(input("Please enter array length: \n"))
for index in range(array_length):
    i = int(input(f'Please enter number in array index {index}: \n'))
    array.append(i)
print(array)


def bubble_sort():
    for index in range(len(array)):
        for index in range(len(array)):
            if index > 0:
                if array[index - 1] < array[index]:
                    i = array[index]
                    i2 = array[index - 1]
                    array[index] = i2
                    array[index - 1] = i
                    print('Sorted index:', index, 'Value:', array[index-1], 'With:', array[index])
    print(array)

bubble_sort()
