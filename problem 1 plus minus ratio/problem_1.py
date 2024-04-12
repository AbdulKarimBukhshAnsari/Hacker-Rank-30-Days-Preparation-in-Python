
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr): 
    count_positive = 0  #made the count of each of the type
    count_negative = 0
    count_zero = 0
    for i in arr:
        if i == 0:     #checking the condition and incrementing the count
            count_zero+=1
        elif i>0:
            count_positive+=1
        else:
            count_negative+=1
    total = len(arr)   #finding the total length of the list
    ratio_positive = count_positive/total  #finding the ratio and at the end printing them so we can be able to see the result
    ratio_negative = count_negative/total
    ratio_zero = count_zero/total
    print(ratio_positive)
    print(ratio_negative)
    print(ratio_zero)
if __name__ == '__main__': 
    n = int(input().strip())   #take the length of the list 

    arr = list(map(int, input().rstrip().split())) #take the input of the list 

    plusMinus(arr)