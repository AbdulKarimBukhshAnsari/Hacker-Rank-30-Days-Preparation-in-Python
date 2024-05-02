import math 
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    if (n-p) > p :
    
        print(int(p/2))
    else:
        print(int((n-p)/2))

if __name__ == '__main__':


    n = int(input().strip())

    p = int(input().strip())

    pageCount(n, p)

print(math.ceil(1/2))