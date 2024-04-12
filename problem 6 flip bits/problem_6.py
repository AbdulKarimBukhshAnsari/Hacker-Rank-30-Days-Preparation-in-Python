
#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary_number =  bin(n)  #converting the given integer into binary number 
    binary_number_final = binary_number[2:].zfill(32) #ensure that the number would be 32 bites and without binary notation
    
    flip_number = ""        #making a string 
  
    for i in binary_number_final:            #checking the condition and changing the number            
        if i == "0":
            flip_number = flip_number+"1"
        else:
            flip_number = flip_number+"0"
    result_flip_number = int(flip_number,2)  #changing the flip number as you know that this number would be in bianry it will change this number in decimal 
    print(result_flip_number)                # the 2 represent that the number is given is in bianry form 
if __name__ == '__main__':
    

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

