#################################
#Author: Brandon Jones
#Description: Takes input from a txt file and returns a sorted list using stooge sort
#Date: 10/11/19
###################################


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
    
    array = []
   
    file1 = "data.txt"  #The text file holding the numbers
    
    #used to open the file
    with open(file1, 'r') as f:
        for line in f: #each line
            line = line.split() #splits each line
            if line:
                line = [int(i) for i in line] #converst string to int for each value
                array.append(line)  #adds each line to the new array


    outFile1 = open('stooge.txt', 'w')  #Creates and writes to the new test1.txt file

    #
    for i in range(0, len(array)):
        arr = array[i][1:] #takes one like at a time
        sort(arr, l, h) #sorting algorithm

        #outputs to the txt file
        for i in arr:
            outFile1.write(str(i) + " ")
        outFile1.write('\n')


    outFile1.close()



if __name__ =="__main__":
    main()



