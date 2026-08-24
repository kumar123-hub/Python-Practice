# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
n=int(input('enter a number: '))           
for i in range(n):
    for j in range(n-i):
        print('*',end=" ")
    print()



#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=' ')
    for k in range(2*i+1):
        print("*",end=" ")
    print()   





# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()     



# *
# **
# * *
# *  *
# *****

n=5
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()        


  
# *
# **
# ***
# ****
# *****
# ******

n=6
for i in range(n): 
    for j in range(i+1):
        print("*",end='')
    print()    



# $
# $$
# $$$
# $$$$
# $$$$$
# $$$$$$
# $$$$$$$

n=7
for i in range(n):
    for j in range(i+1):
        print("$",end='')
    print()  # left angle triangle



#     *
#      **
#     ***
#    ****
#   *****
#  ******
# *******

n=7
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    print() #right angles triangle




# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 

n=6
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print() #square




# *******
# *      
# *      
# *      
# *      
# *      
# *******
n=7
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0:
            print("*",end='')
        else:
            print(' ',end='')
    print()





# ********
# *       
# *       
# *       
# ********
# *       
# *       
# ********

n=8
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print() 




# @      @
# @      @
# @      @
# @      @
# @@@@@@@@
# @      @
# @      @
# @      @


n=8
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('@',end='')
        else:
            print(' ',end='')
    print() 






# &               & 
# & &             & 
# &   &           & 
# &     &         & 
# &       &       & 
# &         &     & 
# &           &   & 
# &             & & 
# &               &


n=9
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print('&',end=' ')
        else:
            print(' ',end=' ')
    print() 



n = 5
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


