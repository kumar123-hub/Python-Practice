# n=int(input("Enter a number:"))
# if (n%2==0):
#     print("Even")
# else:
#     print("odd")


# #password leght has enough characters are not

# password=(input("Enter a number:"))
# if len(password)>=8:
#     print("enough characters")
# else:
#     print("not enough characters")




# #write a program to withdraw oney from my account
# money=int(input("Enter your money:"))
# withdraw=int(input("Enter how much amount withdraw: "))
# if money>withdraw:
#     money-=withdraw
#     print(f' withdraw is successful and remaining balance is{money}')
# else:
#     print("withdraw not successfull")



# #write a program to check login or not
# n=input("Enter a password: ")
# password='kumar@123'
# if password==n:
#     print("login successful")
# else:
#     print("login failed! try again")



# #tax based on salary
# salary=int(input("Enter your salary: "))
# if salary<300000:
#     print("no tax")
# elif salary<700000:
#     salary-=salary*0.04
#     print(f'you need to pay tax {salary}')
# elif salary<1000000:
#     salary-=salary*0.10
#     print(f'you need to pay tax {salary}')
# else:
#     print(f' you need to pay tax :{salary*0.12}')



# #write a program to print notofication we get based on battery percentage
# percentage=int(input("Enter your battery percentage: "))
# if percentage==100 :
#     print("battery fully charged")
# elif percentage<=10:
#     print("your battery is running low ")
# elif percentage<=30:
#     print("power saving mode")
# else:
#     print(" normal mode")


# #write a program to give discount
# bill=int(input("Enter your purchase bill: "))
# if bill>10000:
#     discount=bill*50/100
#     total=bill-discount
#     print(f'total bill you have to pay is {total}')
# elif bill<5000:
#     discount=bill-0.2/100
#     total=bill-discount
#     print(f'total bill you have to pay is {total}')
# else:
#     print ("you have no discoun " ) 


### NESTED IF ELSE

# age=int(input("Enter your age: "))
# if age>18:
#     license=input("do you have license: ")
#     license=='yes'
#     if license=='yes':
#         print("you can drive")
#     else:
#         print("need license to drive")
# else:
#     print('minors cannot drive ')


# fees=(input("do you pay fees: "))
# if fees=='yes':
#     attendence=int(input("Enter your attendence: "))
#     if attendence>75:
#         print("you cannot pay condonation and ready for exams")
#     else:
#         print("you pay condonation and ready for exam")
# else:
#     print("you cannot write exam")


# card=input("insert your card:")
# if card=='yes':
#     pin1=5632
#     pin=int(input("Enter your pin: "))
#     if pin1==pin:
#         print('you can withdraw your money')
#     else:
#         print('invalid pin')
# else:
#     print("please insert card properly")



# experience=int(input('enter your  experience: '))
# if experience>3:
#     performence=input('you have best performence or not: ')
#     if performence=='yes':
#         print('you are eligible for prootion')
#     elif performence=='good':
#         print("'you are eligible for salary hike")
#     else:
#         print('improve your perfromance')
# else:
#     print('do not have any experience')




# card=int(input('enter your card number: '))
# card1=564564
# cv=int(input('enter your cv '))
# cv1=563
# if card==card1 and cv==cv1:
#     otp=int(input('enter your otp: '))
#     myotp=1234
#     if otp==myotp:
#         print("order placed")
#     else:
#         print('order not placed')
# else:
#     print('invalid card details')
















