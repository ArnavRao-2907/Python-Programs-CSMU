#08. Reverse a Number

def reverse_number():
    
    x=int(input("Enter a Number:\n"))
    r=0
    while(x>0):
        d=x%10
        r=(r*10)+d
        x=x//10
    print("Reverse of the Number is:\t",r)

#08. Reverse a Number

def rn(x):
    
    r=0
    while(x>0):
        d=x%10
        r=(r*10)+d
        x=x//10
    print("Reverse of the Number is:\t",r)

if __name__ == "__main__":
    rn(123)