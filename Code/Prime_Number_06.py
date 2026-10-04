#06. Check Prime Number

def prime_number():
    
    x=int(input("Enter an Integer:\n"))
    t=0
    n=x//2
    i=2
    c=0
    while(t==0):
        if(x==0):
            c=0
        elif(x==1):
            c=1
        elif(x==2 or x==3):
            c=2
        else:
            while(i<=n):
                if(x%i==0):
                    c=c+1
                    i=i+1
                else:
                    i=i+1
            c=c+2
        t=1
    if(c==0):
        print("0 is neither a Prime or Composite nor Co-Prime Number")
        print("Number of factors of:",x,"is\t infinite")

        
    elif(c==1):
        print("1 is not a Prime Number, and is a Co-Prime Number")
        print("Number of factors of:",x,"is\t",c)

    elif(c==2):
        print(x,"is a Prime Number")
        print("Number of factors of:",x,"is\t",c)

    else:
        print(x,"is not a Prime Number, and is a Composite Number")
        print("Number of factors of:",x,"is\t",c)


#06. Check Prime Number

def pn(x):

    t=0
    n=x//2
    i=2
    c=0
    while(t==0):
        if(x==0):
            c=0
        elif(x==1):
            c=1
        elif(x==2 or x==3):
            c=2
        else:
            while(i<=n):
                if(x%i==0):
                    c=c+1
                    i=i+1
                else:
                    i=i+1
            c=c+2
        t=1
    if(c==0):
        print("0 is neither a Prime or Composite nor Co-Prime Number")
        print("Number of factors of:",x,"is\t infinite")

        
    elif(c==1):
        print("1 is not a Prime Number, and is a Co-Prime Number")
        print("Number of factors of:",x,"is\t",c)

    elif(c==2):
        print(x,"is a Prime Number")
        print("Number of factors of:",x,"is\t",c)

    else:
        print(x,"is not a Prime Number, and is a Composite Number")
        print("Number of factors of:",x,"is\t",c)


if __name__ == "__main__":
    pn(45)