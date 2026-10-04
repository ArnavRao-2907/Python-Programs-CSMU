#05. Generate Fibonacci Series

def fibonacci_series():

    x=int(input("Enter number of terms (min:3):\n"))
    i=2
    a=1
    b=1
    print("\n"*5)
    print("FIBONACCI SERIES\n\n")
    print(a)
    print(b)
    while i<x:
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1

#05. Generate Fibonacci Series

def fs(x):
    
    i=2
    a=1
    b=1
    print("FIBONACCI SERIES\n\n")
    print(a)
    print(b)
    while i<x:
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1

