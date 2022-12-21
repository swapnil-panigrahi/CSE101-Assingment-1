def digit_names(x):
    name_list=["Zero","One","Two","three","four","five","six","seven","eight","nine"]
    return name_list[x+1]

def two_digit_names(y):
    name_list=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eigthteen","nineteen"]
    return name_list[y-10]

def multiples_of_ten(z):
    name_list=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    return name_list[z-2]

number=str(int(input()))

if len(number)==1:
    print(digit_names(int(number)-1))
elif int(number)>=10 and int(number)<20:
    print(two_digit_names(int(number)))
else:
    print(multiples_of_ten(int(number[0]))+" "+digit_names(int(number[1])-1))