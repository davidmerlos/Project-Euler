#The sum of the squares of the first ten natural numbers is 385 (1^2 + 2^2 + ... + 10^2)
#The square of the sum of the first ten natural numbers is 3025 (1+2+...+10)^2
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def difference(x):
    sum_of_squares = 0
    sum_of_elements = 0


    for element in range(0,x+1):
        sum_of_squares += element ** 2
        sum_of_elements += element

    square_of_the_sum_of_elements = sum_of_elements ** 2
    diff = square_of_the_sum_of_elements - sum_of_squares
    
    print(sum_of_squares)
    print(sum_of_elements)
    print(square_of_the_sum_of_elements)
    print(diff)
    



difference(100)

    