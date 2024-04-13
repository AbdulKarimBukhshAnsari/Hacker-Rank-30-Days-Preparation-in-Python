"""Pangram is a string that contain all the alphabet of english language without checking its case(lower/upper)"""
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    lower_string = s.lower()
    list_of_alphabet = [chr(i) for i in range(97,123)] 
    check = True  
    for i in list_of_alphabet:
        if i not in lower_string:
            check = False
    if check == True:
        print("pangram")
    else:
        print("not pangram")
        



if __name__ == '__main__':
    

    s = input("Enter the string: ")

    result = pangrams(s)

  
