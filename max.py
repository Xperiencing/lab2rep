array = []
num_elements = int(input('How many numbers would you like to enter into the array: '))

for n in range(num_elements):
    numbers = int(input('Enter a number '))
    array.append(numbers)
print('Maximum element in the list is :', max(array))
