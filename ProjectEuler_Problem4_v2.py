#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

x = []  
y = []  
product_x_y = []

def Palindrome(i, j):    
    num=i*j
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False


for i in range(100,999):
    for j in range(100,999):
        if Palindrome(i, j) == True:
            x.append(i)
            y.append(j)


for num1, num2 in zip(x, y):
    product_x_y.append(num1*num2)

print(product_x_y)
highest_number = max(product_x_y)
print(highest_number)
