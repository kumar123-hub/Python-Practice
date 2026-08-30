
# # Task: A company wants to display the first letter of a customer's name.
# string=input('enter a string: ')
# print (string[0])



# #  Task: An office system needs to display an employee ID in reverse order.
# id=input('enter a emp id: ')
# # rev=''
# # for i in range(len(id)):
# #     rev+=i
# # print(rev)
# print(str(id[::-1]))



# # Task: A website requires a password to contain at least 8 characters. Print 'Valid Password' 
# # when the requirement is satisfied; otherwise print 'Invalid Password'.

# password=input('enter your password: ')
# if len(password)>8:
#     print('valid password')
# else:
#     print('not valid')
    


# #  A mobile banking app receives an SMS containing a 6-digit OTP. Extract the OTP from the message.

# otp=input('enter your opt: ')
# for i in range(len(otp)):
#     if otp[i] .isdigit():
#         print (otp[i],end='')




# # Task: A messaging application wants to count the vowels a, e, i, o and u in a message.

# message=input('enter your message: ')
# vowelscount=0
# for ch in message:
#     if ch in 'AEIOUaeiou':
#         vowelscount+=1
# print(f'the vowelscount is: {vowelscount}')



# # Task: An online shopping cart contains the prices of purchased products. Calculate the total price.


# n=int(input('enter how many prices: '))
# list=[]
# for i in range (1,n+1):
#     price=int(input(f'enter {i} price: '))
#     list.append(price)
#     total=0
#     for price in list:
#         total+=price
# print(f'the total is: {total}')




# #  A weather application stores temperatures recorded over five days. Find the highest temperature.


# n=int(input('enter how many teperatures: '))
# list=[]
# highest=0
# for i in range(1,n+1):
#     value=int(input(f'enter your {i} value: '))
#     list.append(value)
#     if value >highest:
#         highest=value
# print(f'the highest value is: {highest}')




# #  A delivery company records delivery times in minutes. Print only deliveries that took more than 60 minutes.


# n=int(input('enetr number of delivery times: '))
# list=[]
# for i in range(1,n+1):
#     times=int(input(f'enter your {i} time: '))
#     if times>60:
#         list.append(times)
# print(f'the time above 60 mins is: {list}')
        



# #  Task: A teacher stores students' test scores. A score of -1 means the student 
# #  did not attend. Remove all -1 values.

# n=int(input('enetr number of test scores: '))
# list=[]
# for i in range(1,n+1):
#     times=int(input(f'enter your {i} score: '))
#     if times>0:
#         list.append(times)
# print(f'the removed test scores is: {list}')



# #  Task: An online shopping cart contains product names. 
# #  Check whether the requested product is present. Print 'Product Found' or 'Product Not Found'.

# cart=['and','apple','ox','egg']
# search=input('enter your search element: ')
# if search in cart:
#     print('element found')
# else:
#     print('not found')



# # Task: A school stores a student's marks in different subjects. Calculate the total marks.

# score={'python':85,'sql':72,'linux':90}
# total=0
# for value in score.values():
#     total+=value
# print(f'the total is: {total}')





# score={}
# total=0
# n=int(input('enter how many subjects: '))
# for i in range(n):
#     sub=input(f'enter a subject {i+1}: ')
#     marks=int(input(f'enter marks for {sub}: '))
#     score[sub] = marks
# for value in score.values():
#     total+=value
# print(f'the total score is: {total}')




# # Task: A store maintains product prices. Ask the user for a product name and display its price.

# products = {'laptop': 55000, 'mouse': 800, 'keyboard': 1500}
# search = input('Enter your product name: ')
# keys = list(products.keys())
# values = list(products.values())
# for i in range(len(keys)):
#     if search == keys[i]:
#         print(values[i])





# Task: A gaming application stores players and their scores. Find the player with the highest score.

score={'rahul':85,'rohit':264,'kohli':0}
highest=0
value=list(score.values())
for i in range(len(score)):
    if value[i]>highest:
        highest=value[i]
print(f'the highest score is: {highest}')










    
    




















    






















    
    

















