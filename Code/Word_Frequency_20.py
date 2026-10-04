#20. Word Frequency in a sentence

def word_frequency():

    x=input("Enter a String:\n")
    s=x.split()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print("Frequency of Words:\n",d)

#20. Word Frequency in a sentence

def wf(x):

    print(x)
    s=x.split()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)

if __name__ == "__main__":
    wf("")