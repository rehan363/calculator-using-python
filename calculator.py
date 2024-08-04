a = float(input("Enter the first number:"))
operator = str(input("Enter the operator, + ,- ,* ,/ ,% "))
if operator not in ('+','-','*','/','%'):
    print("Enter valid operator!!")
else:
     b = float(input("Enter the secound number:"))


if operator == '+':
    sum=(a+b)
    print(str(f'Sum of {a} and {b} is {sum}'))

elif operator == '-':
    differ =(a-b)
    print(str(f'Differancr b/w {a} and {b} is {differ} '))

       
elif operator == '*':
    product =(a*b)
    print(str(f'Product of {a} and {b} is {product}'))


elif operator == '/':
    division =(a/b)
    print(str(f'Division of {a} and {b} is {division}'))

elif operator=='%':
    mod=(a%b)
    print(str(f'Mod of {a} and {b} is {mod}'))



    












