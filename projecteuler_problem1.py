

Below_1000 = range(0,1000)
total = 0

for i in Below_1000:
    if i%3 == 0 or i%5 == 0:
        total += i

print(total)
