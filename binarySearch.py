def binarySearch(arr,start,end,num):
    found = False
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num :
            found = True 
            return found 
        elif arr[mid] < num :
            start = mid + 1
        elif arr[mid] > num :
            end = mid -1 
        

    return found

arr = [1,2,3,7,10,11]
num = 15

result = binarySearch(arr,0,len(arr)-1,num)

if (result) :
    print ("Found")
else:
    print ("Not Found")

