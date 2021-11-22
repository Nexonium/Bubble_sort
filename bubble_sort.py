# Bubble sort v.0.1
# Made by the greatest programmer of all time

array = list()
array_length = int(input("Please enter array length: \n"))
for index in range(array_length):
    i = int(input(f'Please enter number in array index {index}: \n'))
    array.append(i)
print(array)


def bubble_sort():
    for index in range(len(array)):
        print(index, array[index])
        if index > 0:
            if array[index - 1] < array[index]:
                i = array[index]
                i2 = array[index - 1]
                array[index] = i2
                array[index - 1] = i
                print('Sorted:', index, 'Value:', array[index], 'To:', array[index - 1])
    print(array)
    for index in range(len(array)):
        print('Result: ', index, array[index])

bubble_sort()
