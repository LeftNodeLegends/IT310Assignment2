import time
import random
from fractions import Fraction
def bubbleSort(numbers, numbersize):
    for i in range(numbersize):
        for j in range(numbersize - i - 1):
            if numbers[j] >numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers

def selectionSort(numbers, numbersize):
    for i in range(numbersize):
        min_idx = i
        for j in range(i + 1, numbersize):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


def insertionSort(numbers, numbersize):
    for i in range(1, numbersize):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def getRandomList():
    randomList = []
    #Changed for loop from 1000 to 2000 to 3000 etc. for items in list
    for i in range(1000):
        #Numbers appened were from 1 to 5000
        randomList.append(random.randrange(5000))
    return randomList

def getFractionList():
    randomList = []
    number = random.randrange(5000)
    for i in range(1000):
        randomList.append(Fraction(number, number))
    return randomList

L = getRandomList()
F = getFractionList()

#Selection Sort
startTime = time.time()
selectionSort(L[:], len(L))
endTime = time.time()
print("Selection sort integers:", round(endTime-startTime, 5))

startTime = time.time()
selectionSort(F[:], len(F))
endTime = time.time()
print("Selection sort fractions:", round(endTime-startTime, 5), "\n")

#Bubble Sort
startTime = time.time()
bubbleSort(L[:], len(L))
endTime = time.time()
print("Bubble sort integers:", round(endTime-startTime, 5))

startTime = time.time()
bubbleSort(F[:], len(F))
endTime = time.time()
print("Bubble sort fractions:", round(endTime-startTime, 5), "\n")

#Insertion Sort
startTime = time.time()
insertionSort(L[:], len(L))
endTime = time.time()
print("Insertion sort integers:", round(endTime-startTime, 5))

startTime = time.time()
insertionSort(F[:], len(F))
endTime = time.time()
print("Insertion sort fractions:", round(endTime-startTime, 5), "\n")
