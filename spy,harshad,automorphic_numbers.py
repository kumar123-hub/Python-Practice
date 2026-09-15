# # spy number

# def spy(num):
#     sum=0
#     pro=1
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit
#         pro*=digit
#         temp//=10
#     if sum==pro:
#         print(f'the number {num} is spy')
#     else:
#         print('not spy number')
# spy(22)


# #range of spy number

# def range_spy(start,end):
#     for n in range(start,end+1):
#         total=0
#         pro=1
#         temp=n
#         while temp>0:
#             digit=temp%10
#             total+=digit
#             pro*=digit
#             temp//=10
#         if total==pro:
#             print(n)
# range_spy(1,100)


# # harshad number

# def harshad(num):
#     total=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         total+=digit
#         temp//=10
#     if num%total==0:
#         print('harshad number')
#     else:
#         print('not harshad')
# harshad(18)



# # range of harshad number

# def range_harshad(start,end):
#     for n in range(start,end+1):
#         total=0
#         temp=n
#         while temp>0:
#             digit=temp%10
#             total+=digit
#             temp//=10
#         if n%total==0:
#             print(f'the range of harshad number is:{n}')
# range_harshad(1,100)


# automorphic number
def auto(num):
    sqr=num**2
    temp=num
    count=0
    while temp>0:
        temp//=10
        count+=1
    digits=sqr%(10**count)
    if num==digits:
        print(f'the number {num} is morphic')
    else:
        print('not morphic number')
auto(5)