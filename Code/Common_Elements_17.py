#17. Find common elements in two lists

def common_elements():

    a=int(input("Enter the number of elements in the first list:\n"))
    b=int(input("Enter the number of elements in the second list:\n"))
    m=[]
    n=[]
    for i in range(a):
        x=int(input("Enter the integer for first list:\n"))
        m.append(x)
    for i in range(b):
        y=int(input("Enter the integer for second list:\n"))
        n.append(y)

    print("The first list is:\t",m)
    print("The second list is:\t",n)
    print("\n"*3)
    c=[]
    for i in m:
        if i in n:
            c.append(i)
    print("The common elements in the two lists are:\t",c)

#17. Find common elements in two lists

def ce(x,y):

    m=x
    n=y

    print("The first list is:\t",m)
    print("The second list is:\t",n)
    print("\n"*3)
    c=[]
    for i in m:
        if i in n:
            c.append(i)
    print("The common elements in the two lists are:\t",c)

