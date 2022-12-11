
#recursive version
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        result = factorial_recursive(n-1)
        return result * n


#non-recursive version 
def factorial_non_recursive(n):
    result = 1
    for i in range(2,n+1):
        result *= i 
    return result

number = input("Enter your number")
print("Recursive Version",factorial_recursive(int(number)))
print("Non Recursive Version",factorial_non_recursive(int(number)))

