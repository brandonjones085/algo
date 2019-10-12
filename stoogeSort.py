#################################
#Author: Brandon Jones
#Description: Takes input from a txt file and returns the run time using stooge sort
#Date: 10/11/19
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


##Resource: geeksforgeeks.org/stooge-sort/
#Performs the stooge algorithm
def sort(arr, l, h):

    #used to check the index number
    if h is None:
        h = len(arr) - 1

    #compares the first and last element of the array
    #If the first is smaller than the last, the elements are swapped
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t 

    #This checks for more than 2 elements in the array
    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)

        
        sort(arr, l, (h-t)) #sorts first 2/3 elements
        sort(arr, l+t, (h)) #sorts last 2/3 elements
        sort(arr, l, (h-t)) #sorts first 2/3 elements again

    return arr



#Main function the program is run from
def main():

    l = 0
    h = None
    arr = [20,40,60,100,200]

    outFile2 = open('stooge2.txt', 'w')  #Creates and writes to the new test1.txt file


    for num in arr: #loops through array of values

        for i in range(0, 1): #Loops through once
            rand = randomInt(num) #gets a random number 
            start = timeit.default_timer() #starts timer
            sort(rand, l, h) #sorting algorithm
            fin = timeit.default_timer() - start #ends timer

            outFile2.write(str(num) + ", " +  str(fin) + '\n') #for file output


    outFile2.close() #closes file



if __name__ =="__main__":
    main()



