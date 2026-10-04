#10. Find Sum of Digits

def sum_of_digits():

    x=int(input("Enter a Number:\n"))
    r=0
    while(x>0):
        d=x%10
        r=r+d
        x=x//10
    print("Sum of Digits is:\t",r)

#10. Find Sum of Digits

def sod(x):

    r=0
    while(x>0):
        d=x%10
        r=r+d
        x=x//10
    print("Sum of Digits is:\t",r)

if __name__ == "__main__":
    sod(91)