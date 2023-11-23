data = open('sum_all_numbers.txt','r')

sum = 0

for row in data:
    el_row = row.split(' ')
    for element in el_row:
        sum += int(element)

data.close()

print(sum)