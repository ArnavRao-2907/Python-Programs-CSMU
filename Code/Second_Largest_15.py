#15. Find second largest number in a list

def second_largest():
    
    n=int(input("Enter the number of elements in the list:\n"))
    lst=[]
    for i in range(n):
        x=int(input("Enter the integer:\n"))
        lst.append(x)
    lst.sort()
    print("The second largest number in the list is:\t",lst[-2])
    
#15. Find second largest number in a list

def sl(x):
    arr=x
    max1=arr[0]

    for i in arr:
        if i>max1:
            max1=i
    print("The second largest number in the list is:\t",max1)

    
if __name__ == "__main":
    sl([5,6,5,7])