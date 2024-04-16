

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    if len(s) == 1:
        if s[0] == d:
            print(1)
    else:
        count = 0
        for i in range(len(s)-m+1):
            if sum(s[i:i+m]) == d:

                count+=1
            print(count)
        
        print(count)
if __name__ == '__main__':

    
    s = [1, 2, 1, 3, 2]
    d = 16
    m = 7

    result = birthday(s, d, m)
