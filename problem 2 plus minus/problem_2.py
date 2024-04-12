
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr_2 = arr[:] #copying the list 
    min_number = min(arr_2) #finding the minimum element of the list 
    arr_2.remove(min_number) #removing it 
    max_sum = sum(arr_2) #suming it , the max sum will be without minimum element
    max_number = max(arr) # finding max number
    arr.remove(max_number) #removing it 
    min_sum =  sum(arr)  # min sum will be found if the if the max number will be removed 
    print(f"{min_sum} {max_sum}") #printing it 

if __name__ == '__main__':

    arr = [1,3,5,7,9]

    miniMaxSum(arr)