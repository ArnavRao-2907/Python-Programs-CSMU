#09. Check Palindrome Number

def palindrome_number():

    a=int(input("Enter a Number:\n"))
    x=a
    r=0
    while(x>0):
        d=x%10
        r=(r*10)+d
        x=x//10
    if a==r:
        print("The Number is a Palindrome Number")
    else:
        print("The Number is not a Palindrome Number")

#09. Check Palindrome Number

def pn(a):

    x=a
    r=0
    while(x>0):
        d=x%10
        r=(r*10)+d
        x=x//10
    if a==r:
        print("The Number is a Palindrome Number")
    else:
        print("The Number is not a Palindrome Number")

if __name__ == "__main__":
    pn(10)