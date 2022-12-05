import math
#behold the gambiarra
def binary_to_decimal(binary):
    return sum([int(list(binary)[-1*(exp-(int(len(list(binary))-1)))])*(2**exp) for exp in range(len(list(binary))-1, -1, -1)]) 

def __init__():
    x = input('Input the positive integer in the binary form: ')
    
    print('Here is the number in decimal form ---> ', binary_to_decimal(x))

__init__()