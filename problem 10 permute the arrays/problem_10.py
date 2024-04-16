
#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B



def twoArrays(k, A, B):
    # Write your code here
      # Write your code here
    A.sort()
    B.sort(reverse =  True) # we simply sort both of the arrays in revrese order if the sum of lesser value and greater value is equal to greater than 
    count = 0 #make the count variable to check whether the condition is satisfied or not 
    for a,b in zip(A,B):
        if a+b >= k: #checking the required condition
            count+=1 #increasing the counting if the condition  of if would be true

    if count == len(A): # if the value of count and the length of A is euqal it means for each value of A will be true
        print("YES")
    else:
        print("NO") 
    

if __name__ == '__main__':
    k = 10
    a = [1,2,3,4]
    b = [3,5,6,7]
    twoArrays(k,a,b)
