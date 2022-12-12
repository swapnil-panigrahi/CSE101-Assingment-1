def digit_names(x):
    name_list=["one","two","three","four","five","six","seven","eight","nine"]
    return name_list[x]

def two_digit_names(y):
    name_list=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eigthteen","nineteen"]
    return name_list[y-11]

def multiples_of_ten(z):
    name_list=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    return name_list[z//10-1]

def powers_of_ten(w):
    name_list=["hundred","thousand","thousand","lakhs","lakhs","crores"]
    return name_list[w-3]

number=input()
number_name=[]
i=0

while i<len(number):
"""    if i==0 and int(number[-1]):
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
    elif i>2 and len(number)>i+2:
        if number[-i-2]!='0':
            number_name.append(multiples_of_ten(int(number[-i-2])*10)+" "+digit_names(int(number[-i-1])-1)+" "+ powers_of_ten(i+1))
        elif number[-i-1:-i-3]=="00":
            continue    
        else:
            number_name.append(digit_names(int(number[-i-1])-1)+" "+ powers_of_ten(i+1))
        i=i+2
    else:
        i+=1"""
print(number_name)