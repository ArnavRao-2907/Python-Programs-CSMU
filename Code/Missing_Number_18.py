#18. Find missing number in a list

def missing_number():

    n=int(input("Enter the number of elements in the list:\n"))
    lst=[]
    for i in range(n):
        x=int(input("Enter the integer:\n"))
        lst.append(x)
    lst.sort()
    print("The list is:\t",lst)
    for i in range(lst[0],lst[-1]):
        if i not in lst:
            print("The missing number in the list is:\t",i)
            break


def mn(lst):

    n=len(lst)+1
    t=(n*(n+1))//2
    r=t - sum(lst)
    print(r)

if __name__ == "__main__":
    mn([1,3,4,5])