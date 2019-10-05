#################################
#Author: Brandon Jones
#Description: Creates arrays of random ints and sorts them. The merge sort function is timed
#Date: 10/5/19
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



##Resource: geeksforgeeks.org/merge-sort/
##Algorithm to perform the merge sort
def sort(arr): 
    if len(arr) > 1:
        i = 0
        j = 0
        k = 0

        middle = len(arr) // 2  #splits the array in two
        left = arr[:middle]  #left side of splie  
        right = arr[middle:]  #right side of split

        #performs sort on each side
        sort(left)
        sort(right)

        #Moves elements to temp arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j +=1
            k += 1

        #checks for missing elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


#main function where program is run

def main():
    arr = [5000, 7000, 12000, 20000, 30000, 40000]
    outFile2 = open('test3.txt', 'w')   #Creates and writes to the new test1.txt file

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

