import math
def is_prime(num):
    if type(num)!=int:
        raise TypeError("invalid type")
    
    if num < 0:
        raise ValueError("Num is negative value")

    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False  
    return True 

print(is_prime(5))