def linearSearch (arr, num):
    found = False
    for i in range (0,len(arr)):
        if arr[i] == num:
            found = True
    return found


print(linearSearch([1,2,34,5,8,10],7))