
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar.sort()
    pair = 0
    check = []  #it will contain all the element which has been done
    for i in ar: 
        if i not in check: #will check whether the i is already has counted or not 
            pair += int(ar.count(i)/2) # we use int suppose if we have the float answer it completely means that there is no pair because otherwise this number should be divided by 2 

            check.append(i) #for which we have worked will append into list
    print(pair)


if __name__ == '__main__':
  

    n = int(input())

    ar = [1,2,1,2,1,3,2]

    result = sockMerchant(n, ar)

 
