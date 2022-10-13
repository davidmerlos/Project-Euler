#Enunciado:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number = 600851475143

list_of_prime_factors = []
i = 2

while number > 1:
    if number % i == 0:
        number = number / i
        list_of_prime_factors.append(i) 
    i = i + 1

print(list_of_prime_factors)
