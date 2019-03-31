#三天打鱼，两天晒网
dayup = 1
dayfactor = 0.01
k = 1

for i in range(365):
    if i % 5 in [1,2,3]:
        dayup = (1 + dayfactor) * dayup
    else:
        dayup = dayup * (1 - dayfactor)
print("{:.2f}".format(dayup))