
                      # user defined functions without return value
def table(n):
    for i in range(1,11):
        print(f'{n} X {i}={n*i}')
table(7)


# write a function to print area and perimeter of a rectangle
def area1(n1,n2):
    area=n1*n2
    perimeter=2*(n1+n2)
    print(area)
    print(perimeter)
area1(12,12)


# write a function to find greatest among three numbers
def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f'{n1} is greatest')
    elif  n2>n3:
        print(f'{n2} is greatest')
    else:
        print(f'{n3} is greatest')
greatest(1,5,99)


#smallest among three numbers
def smallest(n1,n2,n3):
    if n1<n2 and n1<n3:
        print(f'{n1} is smallest')
    elif  n2<n3:
        print(f'{n2} is smallest')
    else:
        print(f'{n3} is smallest')
smallest(1,5,99)



# write a function to print discount and total bill of purchase
def discount1(mrp,discount):
    discount=mrp*(discount/100)
    bill=mrp-discount
    print(bill)
discount1(1599,7)


                        # functions with retuen statements


# function with addition of 2 numbers
def addition(n1,n2):
    sum=n1+n2
    return sum
print(addition(1,2)+5)




# write a program to calculate age of a person
def agecal(birthyear,presentyear):
    return presentyear-birthyear
print(agecal(2005,2026))




# task:
# write a 3 functions one for calculate total expences of a company 2. calculate the sales of a company 3
#     3.which takes the above two functions as arguments and calculate revenue as profot or loss


def total_expenses():
    expenses=[10000, 15000, 20000]
    return sum(expenses)
def total_sales():
    sales=[30000, 25000, 20000]
    return sum(sales)
def revenue(expenses,sales):
    profit=sales-expenses
    loss=expenses-sales
    if profit>0:
        print(f'company got {profit} money was profit ')
    else:
        print(f'company got {loss} of money was loss')
expenses=total_expenses()
sales=total_sales()
revenue(expenses,sales)


                        #  positional arguments
# wriite a function to print a person name and course
def welcome(name,course):
    return(f' welcome to {name} your course  is {course} ')
print(welcome('kishore','bpharm'))


#write a function to find area of a rectangle and circle
def rectangle(lenght,breadth,radius):
    area=lenght*breadth
    circle_area=3.14*radius*radius
    return area,circle_area
print(rectangle(2,4,5))




                             # keywords arguments:

# these are used to pass arguments to our parameters without worrying aboutn the order of the parameters
# we can pass arguments in any order based on keywords


# write a function to print a person name,place,course
def details(name,place,course):
    print(f' {name} is belongs to {place} place and learning {course} course')
details('chandu','cumbum','data analytics')
details(name='chandu',course='data analytics',place='cumbum')



# write a function to print total expense of current bill based on number of units consumed
def bill(units,charge,unit):
    total=(unit*units)+charge
    print(f'the total number of units is {units} and charge is {charge} and total bill is {total}')
bill(10,25,8)
bill(charge=100,units=1,unit=100)



# write a function to print login and not login based on time ,username,passwords
def loginsys(username,password,logintime):
    if logintime>=10 and logintime<=7:
        if username=='chandu' and password=='kumar':
            print('login successful')
        else:
            print('invalid details')
    else:
        print('not login at thiss time ')
loginsys(username='chandu',password='kumar',logintime=5)




                    # variable lenght arguments

# find the sum and product of a number and print the highest among them
def calcu(*num):
    sum=0
    pro=1
    for i in num:
        sum+=i
        pro*=i
    print(f'the sum is {sum}')
    print(f'the product is {pro}')
    if sum>pro:
        print('sum is grater')
    else:
        print('product is greater')
calcu(1,2,3,4,5,6,7,8,9,10)


# count even and odd numbers and print that numbers
def count(*args):
    even_count=0
    odd_count=0
    even_numbers=[]
    odd_numbers=[]
    for i in args:
        if i%2==0:
            even_count+=1
            even_numbers.append(i)
        else:
            odd_count+=1
            odd_numbers.append(i)
    print(f'even numbers count is  {even_count} and even numbers are : {even_numbers}')
    print(f'odd numbers count is {odd_count} and odd numbers are : {odd_numbers}')
count(1,45,34,45,3,34,67,99)


























































