def bubbleSort(arr):
    iteration = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1-i):
            iteration += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp 
    return arr, iteration

A = [5,1,9,10,2,3]
print(bubbleSort(A))


    