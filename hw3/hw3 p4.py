n=int (input('pick a number: '))
if n%3==0 and n%5==0:
    print("this number is divisible by 3 and 5")
elif n%3==0:
    print("this number is divisible by 3")
elif n%5==0:
    print("this number is is divisible by 5")
else:
    print("this number is not is divisible")