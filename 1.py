data = open('sum_column_example.txt','r')
sum = 0

for number in data:
    sum += int(number)

data.close()

print(sum)