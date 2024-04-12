import os 
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion():
    s ="06:40:03AM"
    if ("AM" in s) and s[0:2] == "12":
        t = str(0)+str(int(s[0:2]) -12 ) + s[2:-2]
    elif ("PM" in s) and s[0:2] != "12":
        t = str(int(s[0:2])+12) + s[2:-2]
    else:
        t = s[0:-2]

    return t 

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Enter the time in 12 hour format: ")

    result = timeConversion(s)
    print(result)