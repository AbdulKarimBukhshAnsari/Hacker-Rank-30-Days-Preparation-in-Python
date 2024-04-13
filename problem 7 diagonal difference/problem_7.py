
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
"""As we know that the main diagonal element in the condition in which i == j 
and for the other diagonal is that in which i+j = n-1 """

def diagonalDifference(arr):
    sum_1 = 0  #making the variable to store the sum of both diagonal 
    sum_2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j : 
                sum_1 = sum_1 + arr[i][j]
            if i+j == len(arr) -1 :
                sum_2 = sum_2 + arr[i][j]
    result = abs(sum_1 - sum_2)   # abs will convert negative number in to positive too 
    print(result)
if __name__ == '__main__':
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

  
