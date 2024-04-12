
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_positive = 0
    count_negative = 0
    count_zero = 0
    for i in arr:
        if i == 0:
            count_zero+=1
        elif i>0:
            count_positive+=1
        else:
            count_negative+=1
    total = len(arr)
    ratio_positive = count_positive/total
    ratio_negative = count_negative/total
    ratio_zero = count_zero/total
    print(ratio_positive)
    print(ratio_negative)
    print(ratio_zero)
if __name__ == '__main__': 
    n = int(input().strip())   

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)