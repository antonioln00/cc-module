list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
avg = 0

for index in list_of_numbers:
    count = index + count
    avg = count / len(list_of_numbers)
    avg

print(avg)
    
