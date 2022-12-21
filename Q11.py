#Word Guessing Game for 2 players

def list_print(a):
    b=""
    for i in a:
        b+=i

    return b

def index(x,l):
    for i in range(len(l)):
        if l[i]==x:
            return i
            break
    else:
        return -1
 
str=list(input("User1 string:"))
 
while len(str)>10:
    print("Re-Enter [Not more than 10 letters]")
    str=input("Enter string")
 
print("\n"*150)
 
guessed_str=list(str)
 
for i in range(len(str)):
    if str[i] in ("a","e","i","o","u"):
        continue
    elif str[i]>="a" and str[i]<="z":
        str[i]="_"
 
print(list_print(str))
 
penalty=0
count=0
n=[]
 
while count<=10:
    if guessed_str==str:
        break
    
    m=input("User 2 guess:").strip()
    count+=1
 
    if m in guessed_str:
        x=index(m,guessed_str)
        str[x]=m
    else:
        print(m,"is not in the word")
    
    if m in n:
        penalty=+2
        print("Penalty:",penalty)
    else:
        n.append(m)
    print(list_print(str))
 
print("Points:",20-count-penalty)