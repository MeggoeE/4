main_str = input()
count = 0
sum = 0
lenght_of_sequence = 0
while count < len(num):
    if main_str[count] == '0':
        sum += 1
        if sum > lenght_of_sequence:
            lenght_of_sequence = sum
    if main_str[count] == '1':
        sum = 0
    count += 1
print(lenght_of_sequence)
