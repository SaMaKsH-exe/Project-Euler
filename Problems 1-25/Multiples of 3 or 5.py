num = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        num.append(i)


print(sum(num))
        


