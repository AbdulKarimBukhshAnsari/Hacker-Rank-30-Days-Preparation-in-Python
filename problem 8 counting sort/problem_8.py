

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    result_array = [0 for _ in range(100)]
    for i in arr:
        result_array[i]+=1
    print(result_array) 

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

   
