#################################
#Author: Brandon Jones
#Description: Creates arrays of random ints and sorts them. The merge sort function is timed
#Date: 10/4/19
###################################

from random import randrange
import timeit


#Returns an unsorted array of random ints between 0 and num provided
def randomInt(num):
    numArr = []
    for x in range(num):
        getNum = randrange(10000)
        numArr.append(getNum)
    return numArr



##Resource: geeksforgeeks.org/python-program-for-insertion-sort/
#Performs the insertion sort algorithm
def sort(arr): 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
   


#Main function the program is run from
def main():
    arr = [5000, 7000, 12000, 20000, 30000, 40000]

    outFile2 = open('test4.txt', 'w')   #Creates and writes to the new test1.txt file

    for num in arr: 
        for x in range(0, 5):
            rand = randomInt(num)
            start = timeit.default_timer()
            sort(rand)
            fin = timeit.default_timer() - start

            outFile2.write(str(num) + ", " +  str(fin) + '\n')
    outFile2.close()



if __name__ =="__main__":
    main()






