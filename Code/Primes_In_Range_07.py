#07. Check Prime Numbers in a Range

def primes_in_range():

    s=int(input("Enter Starting Number:\n"))
    e=int(input("Enter Ending Number:\n"))
    print("Prime Numbers in the Range of",s,"to",e,"are:")
    for x in range(s,e+1):
        t=0
        n=x//2
        i=2
        c=0
        while(t==0):
            if(x==1):
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
        if(c==2):
            print(x)

#07. Check Prime Numbers in a Range

def pir(s,e):

    print("Prime Numbers in the Range of",s,"to",e,"are:")
    for x in range(s,e+1):
        t=0
        n=x//2
        i=2
        c=0
        while(t==0):
            if(x==1):
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
        if(c==2):
            print(x)

if __name__ == "__main__":
    pir(21,35)