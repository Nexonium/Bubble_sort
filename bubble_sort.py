
# Bubble sort v.0.1
# Made by the greatest programmer of all time

list = list()
list_length = int(input("Please enter array length: \n"))
for item in range(list_length):
  i = int(input(f'Please enter number in array № {item+1}: \n'))
  list.append(i)
print(list)


def bubble_sorter():
  for item in list:
    i = list[item]
    print(i)
bubble_sorter()