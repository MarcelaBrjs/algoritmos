#  ACTIVIDAD: Heapsort & Radixsort - 31/08/2021

# HEAPSORT
def heapSort(array):
    heapSize = len(array)

    for i in range(heapSize//2 - 1, -1, -1):
        heapify(array, heapSize, i)

    for i in range(heapSize - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


def heapify(array, heapSize, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heapSize and array[largest] < array[left]:
        largest = left

    if right < heapSize and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, heapSize, largest)


# RADIXSORT
def radixSort(array):
    maxNumber = max(array)
    place = 1
    while maxNumber // place > 0:
        countingSort(array, place)
        place *= 10


def countingSort(array, place):
    size = len(array)
    sortedArray = [0] * size
    countArray = [0] * 10

    for i in array:
        index = i // place
        countArray[index % 10] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        sortedArray[countArray[index % 10] - 1] = array[i]
        countArray[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = sortedArray[i]


# PRUEBAS
print("HEAPSORT")
array = [10, 3, 76, 34, 23, 32]
print("Original array: ", array)
heapSort(array)
print("Sorted array: ", array)

print("RADIXSORT")
array = [121, 432, 564, 23, 1, 45, 788]
print("Original array: ", array)
radixSort(array)
print("Sorted array: ", array)
