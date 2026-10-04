#12. Reverse a String without using [::-1]

def reverse_string():

    x=input("Enter a String:\n")
    r=""
    for i in x:
        r=i+r
    print("Reverse of the String is:\t",r)


#12. Reverse a String without using [::-1]

def rs(x):

    r=""
    for i in x:
        r=i+r
    print("Reverse of the String is:\t",r)

if __name__ == "__main__":
    rs("Ladu")