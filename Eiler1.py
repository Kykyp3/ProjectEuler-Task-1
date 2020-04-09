potolok = 1000
summa = 0
for i in range(1, potolok):
    if  i % 5 == 0:
        summa = summa + i
    elif i % 3 == 0:
        summa = summa + i
    else:
        print("Перебор...{}".format(summa))
else:
    print(summa)
i