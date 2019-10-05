#################################
#Author: Brandon Jones
#Description: Takes input from a txt file and returns a sorted list using insertion sort
#Date: 10/4/19
###################################


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
    file1 = "data.txt"  #The text file holding the numbers
    
    inFile1 = open(file1, 'r') #Reads in the txt file
    outFile1 = open('test1.txt', 'w')  #Creates and writes to the new test1.txt file


    for i in inFile1: 
        a = list(map(int, i.split()))  #Takes the string, converts to int, and splits values

        line = a[1:]

        sort(line)  #sorting algorithm

        #Converts back to string line by line
        for c in line: 
            outFile1.write(str(c) + ' ')

        outFile1.write('\n')


    #closes files
    inFile1.close()
    outFile1.close()



if __name__ =="__main__":
    main()






