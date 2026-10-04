#13. Check Palindrome String

def palindrome_string():
    
    x=input("Enter a String:\n")
    s=x.lower()
    r=""
    for i in s:
        r=i+r
    if s==r:
        print("The String is a Palindrome String")
    else:
        print("The String is not a Palindrome String")

#13. Check Palindrome String

def ps(x):
    
    s=x.lower()
    r=""
    for i in s:
        r=i+r
    if s==r:
        print("The String is a Palindrome String")
    else:
        print("The String is not a Palindrome String")

if __name__ == "__main__":
    ps("arA")