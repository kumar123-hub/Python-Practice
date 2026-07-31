n=int(input("Enter a number:"))
if (n%2==0):
    print("Even")
else:
    print("odd")


#password leght has enough characters are not

password=(input("Enter a number:"))
if len(password)>=8:
    print("enough characters")
else:
    print("not enough characters")




#write a program to withdraw oney from my account
money=int(input("Enter your money:"))
withdraw=int(input("Enter how much amount withdraw: "))
if money>withdraw:
    money-=withdraw
    print(f' withdraw is successful and remaining balance is{money}')
else:
    print("withdraw not successfull")



#write a program to check login or not
n=input("Enter a password: ")
password='kumar@123'
if password==n:
    print("login successful")
else:
    print("login failed! try again")




#tax based on salary
salary=int(input("Enter your salary: "))
if salary<300000:
    print("no tax")
elif salary<700000:
    salary-=salary*0.04
    print(f'you need to pay tax {salary}')
elif salary<1000000:
    salary-=salary*0.10
    print(f'you need to pay tax {salary}')
else:
    print(f' you need to pay tax :{salary*0.12}')



#write a program to print notofication we get based on battery percentage
percentage=int(input("Enter your battery percentage: "))
if percentage==100 :
    print("battery fully charged")
elif percentage<=10:
    print("your battery is running low ")
elif percentage<=30:
    print("power saving mode")
else:
    print(" normal mode")


#write a program to give discount
bill=int(input("Enter your purchase bill: "))
if bill>10000:
    discount=bill*50/100
    total=bill-discount
    print(f'total bill you have to pay is {total}')
elif bill<5000:
    discount=bill-0.2/100
    total=bill-discount
    print(f'total bill you have to pay is {total}')
else:
    print ("you have no discount" )    







