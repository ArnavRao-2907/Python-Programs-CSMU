#14. Count freqency of characters

def char_frequency():

    x=input("Enter a String:\n")
    s=x
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print("Frequency of Characters:\n",d)

#14. Count freqency of characters

def cf(x):

    s=x
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)

if __name__ == "__main__":
    cf("xXc")