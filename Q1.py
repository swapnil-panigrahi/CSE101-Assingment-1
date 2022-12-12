def digit_names(x):
    name_list=["Zero","One","Two","three","four","five","six","seven","eight","nine"]
    return name_list[x+1]

def two_digit_names(y):
    name_list=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eigthteen","nineteen"]
    return name_list[y-11]

def multiples_of_ten(z):
    name_list=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    return name_list[z//10-1]

def powers_of_ten(w):
    name_list=["hundred","thousand","thousand","lakhs","lakhs","crores","crores"]
    return name_list[w-3]

def two_digit_numbers(u):
    if u==0:
        return ""
    elif u>0 and u<=9:
        return digit_names(u-1)
    elif u>=11 and u<20:
        return two_digit_names(u)
    elif u%10==0:
        return multiples_of_ten(u)
    else:
        return multiples_of_ten(u)+" "+digit_names(u%10-1)

number=input()
number_name=[]
i=0

while i<len(number):
    if len(number)==1:
        digit_names(int(number))
    elif int(number)>10 and int(number)<20:
        number_name.append(two_digit_names(int(number)))
        break
    elif int(number)==0:
        number_name.append("Zero")
        break
    else:
        if i==0 and number[-2]=='1':
            number_name.append(two_digit_numbers(int(number[-2::])))
            i+=2            
        elif i==0 and int(number[-1]):
            number_name.append(digit_names(int(number[-i-1])-1))
            i+=1
        elif i==0 and not int(number[-1]):
            i+=1
            continue
        elif i==1 and int(number[-2]):
            number_name.append(multiples_of_ten(int(number[-i-1])*10))
            i+=1
        elif i==1 and not int(number[-2]):
            i+=1
            continue
        elif i==2 and int(number[-i-1]):
            number_name.append(digit_names(int(number[-i-1])-1)+" "+powers_of_ten(i+1))
            i+=1
        elif i==2 and not int(number[-i-1]):
            i+=1
            continue
        elif len(number)>=i+2 and not int(number[-i-2:-i]):
            i+=2
            continue
        elif len(number)>=i+2 and int(number[-i-2:-i]):
            number_name.append(two_digit_numbers(int(number[-i-2:-i]))+" "+powers_of_ten(i+1))
            i+=2
        else:
            number_name.append(digit_names(int(number[-i-1])-1)+" "+powers_of_ten(i+1))
            i+=2

for i in number_name[::-1]:
    print(i,end=" ")