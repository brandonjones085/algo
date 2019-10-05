#################################
#Author: Brandon Jones
#Description: Takes input from a txt file and returns a sorted list using insertion sort
#Date: 10/4/19
###################################


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
    
    file2 = "data.txt"  #The text file holding the numbers
    
    inFile2 = open(file2, 'r')   #Reads in the txt file
    outFile2 = open('test2.txt', 'w')   #Creates and writes to the new test1.txt file

    for i in inFile2: 
        a = list(map(int, i.split()))  #Takes the string, converts to int, and splits values

        line = a[1:]   #takes the list
        

        sorted = sort(line)     #returnsthe sorted list


        #Converts back to string line by line
        for c in sorted: 
            outFile2.write(str(c) + ' ')

        outFile2.write('\n')


    inFile2.close()
    outFile2.close()
    



if __name__ =="__main__":
    main()

