#finding the variations of the given string 
def permutation (string, pocket = ""):
    if len(string) == 0 :
        print(pocket)
    else:
        for i in range(0,len(string)):
            letter = string[i]
            #print("letter", letter)
            front = string[0:i]
            #print("front", front)
            back = string[i+1:]
            #print("back", back)
            together = front + back 
            #print("together", together)
            permutation (together, letter + pocket)
print(permutation("ABC",""))