#11. Count vowels and consonants

def vowels_consonants():

    x=input("Enter a String:\n")
    s=x.lower()
    v=0
    c=0
    for i in s:
        if i in "aeiou":
            v+=1
        else:
            c+=1
    print("Number of Vowels:\t",v)
    print("Number of Consonants:\t",c)

#11. Count vowels and consonants

def vc(x):

    s=x.lower()
    v=0
    c=0
    for i in s:
        if i in "aeiou":
            v+=1
        else:
            c+=1
    print("Number of Vowels:\t",v)
    print("Number of Consonants:\t",c)

if __name__ == "__main__":
    vc("1ac")