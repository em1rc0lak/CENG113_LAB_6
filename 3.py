cities = open('cities.txt','r')

count = 1

for city in cities:
    if city == 'Izmir\n':
        print(count)
        break
    else:
        count += 1

cities.close()

