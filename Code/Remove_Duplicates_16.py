#16. Remove Duplicates from a list

def remove_duplicates():
    
    n=int(input("Enter the number of elements in the list:\n"))
    lst=[]
    for i in range(n):
        x=int(input("Enter the integer:\n"))
        lst.append(x)
    lst=set(lst)
    print("The list after removing duplicates is:\n",lst)

#16. Remove Duplicates from a list

def rd(x):
    r=[]
    for i in x:
        if i not in r:
            r.append(i)
    return r
    print(r)


