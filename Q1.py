def digit_names(x):
    name_list=["zero","one","two","three","four","five","six","seven","eight","nine"]
    return name_list[x]

def two_digit_names(y):
    name_list=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eigthteen","nineteen"]
    return name_list[y-11]

def muliples_of_ten(z):
    name_list=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    return name_list[x//10-1]

def powers_of_ten(w):
    name_list=["hundred","thousand","lakhs","crores"]

number=int(input())